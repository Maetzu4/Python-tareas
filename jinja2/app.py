from flask import Flask, render_template

app = Flask(__name__)

@app.route("/compra/<producto1>/<int:cantidad1>/<float:precio1>/<producto2>/<int:cantidad2>/<float:precio2>")
def calcular_compra(producto1, cantidad1, precio1, producto2, cantidad2, precio2):

    # Cálculo de subtotales
    subtotal1 = cantidad1 * precio1
    subtotal2 = cantidad2 * precio2
    total_sin_descuento = subtotal1 + subtotal2
    
    # Aplicación de reglas de descuento
    descuento_porcentaje = 0
    if total_sin_descuento > 200000:
        descuento_porcentaje = 20
    elif total_sin_descuento > 100000:
        descuento_porcentaje = 10
        
    descuento_valor = total_sin_descuento * (descuento_porcentaje / 100)
    total_con_descuento = total_sin_descuento - descuento_valor

    return render_template("resultado.html", 
                           producto1=producto1, cantidad1=cantidad1, precio1=precio1, subtotal1=subtotal1,
                           producto2=producto2, cantidad2=cantidad2, precio2=precio2, subtotal2=subtotal2,
                           total_sin_descuento=total_sin_descuento,
                           descuento_porcentaje=descuento_porcentaje,
                           descuento_valor=descuento_valor,
                           total_con_descuento=total_con_descuento)

if __name__ == "__main__":
    app.run(debug=True, port=5000)