from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_mm2(lambda_, mu):
    # Perhitungan M/M/2
    rho = lambda_ / (2 * mu)  # Pemanfaatan pelayan
    if rho >= 1:
        return {"error": "Sistem tidak stabil. λ harus lebih kecil dari 2μ."}

    w = 1 / (mu - (lambda_ / 2))  # Waktu rata-rata dalam sistem
    wq = (lambda_ ** 2) / (2 * mu * (mu - (lambda_ / 2)))  # Waktu rata-rata dalam antrian

    # Kumpulan data hasil perhitungan dengan rumusnya
    return {
        "lambda_": lambda_,
        "mu": mu,
        "rho": rho,
        "rho_formula": f"ρ = λ / (2 * μ) = {lambda_} / (2 * {mu})",
        "w": w,
        "w_formula": f"W = 1 / (μ - (λ / 2)) = 1 / ({mu} - ({lambda_} / 2))",
        "wq": wq,
        "wq_formula": f"Wq = λ² / (2 * μ * (μ - (λ / 2))) = {lambda_}² / (2 * {mu} * ({mu} - ({lambda_} / 2)))"
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            lambda_ = float(request.form["lambda"])
            mu = float(request.form["mu"])
            result = calculate_mm2(lambda_, mu)
        except ValueError:
            result = {"error": "Input tidak valid. Pastikan Anda memasukkan angka."}

    return render_template("index_with_formula.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
