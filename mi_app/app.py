from flask import Flask, render_template

app = Flask(__name__)

@app.route("/estudiante/<nombre>/<float:nota1>/<float:nota2>/<float:nota3>")
def calcular_promedio(nombre, nota1, nota2, nota3):
    promedio = round((nota1 + nota2 + nota3) / 3, 2)
    return render_template(
        "resultado.html",
        nombre=nombre,
        nota1=nota1,
        nota2=nota2,
        nota3=nota3,
        promedio=promedio
    )

if __name__ == "__main__":
    app.run(debug=True)
