# Implemente una aplicación web en Python con Flask que permita gestionar un sistema básico de estudiantes y notas.

# El código base ya está definido y no debe ser modificado en su estructura principal.
# El estudiante debe completar la lógica en las secciones marcadas con # TODO.

# El archivo resultante es extensión .py  el cual se debe adjuntar en el aula.

# Requisitos del sistema

# 1. Página principal ("/")

# Mostrar un menú con opciones:
# Registrar un estudiante (ejemplo de ruta: /registrar/001/Ana/4/3/5)
# Listar estudiantes (/listar)
# Buscar estudiante (/buscar/<codigo>)

# 2. Registro de estudiantes (/registrar/<codigo>/<nombre>/<nota1>/<nota2>/<nota3>)

# Cada estudiante debe almacenarse como un diccionario dentro de una lista llamada estudiantes.
# La estructura será:

{

   "codigo": "001",

   "nombre": "Ana",

   "notas": [4, 3, 5]

}


# 3. Listar estudiantes (/listar)

# Usar un bucle FOR para recorrer la lista estudiantes.
# Crear e implementar una función calcular_promedio(notas) que reciba la lista de notas y retorne el promedio.
# Usar un IF para mostrar si cada estudiante está:
# Aprobado (promedio >= 3.0)
# Reprobado (promedio < 3.0)
# El listado debe desplegarse en formato HTML (ul/li).

# 4. Buscar estudiante (/buscar/<codigo>)

# Usar un bucle WHILE para recorrer la lista de estudiantes y detenerse cuando encuentre el código solicitado.
# Si el estudiante existe, mostrar su nombre y notas.
# Si no existe, mostrar un mensaje indicando que no fue encontrado.
 

# 5. Estructuras de datos

# Debe usar en el programa al menos:
# Lista: para almacenar estudiantes.
# Tupla: ya está definida en el código con las asignaturas ("Matemáticas", "Programación", "Bases de Datos").
# Diccionario: para almacenar la información de cada estudiante.
# Código base (a completar)

from flask import Flask


app = Flask(__name__)


# -----------------------------

# Estructuras de datos iniciales

# -----------------------------

# Lista para almacenar estudiantes

estudiantes = []

 

# Tupla fija con asignaturas

asignaturas = ("Matemáticas", "Programación", "Bases de Datos")

 

# -----------------------------

# Funciones auxiliares

# -----------------------------

def calcular_promedio(notas):
    # TODO: implementar cálculo de promedio
    promedio = 0
    for nota in notas:
        promedio += nota

    promedio /= len(notas)
    return promedio

 

 

# -----------------------------

# Rutas de la aplicación

# -----------------------------

@app.route("/")

def index():

    return """

        <h1>Sistema de Estudiantes</h1>

        <ul>

            <li><a href='/registrar/001/Ana/4/3/5'>Registrar estudiante (Ejemplo)</a></li>

            <li><a href='/listar'>Listar estudiantes</a></li>

            <li><a href='/buscar/001'>Buscar estudiante (Ejemplo)</a></li>

        </ul>

    """

 

 

@app.route("/registrar/<codigo>/<nombre>/<int:nota1>/<int:nota2>/<int:nota3>")

def registrar(codigo, nombre, nota1, nota2, nota3):

    # TODO: agregar el estudiante como diccionario dentro de la lista 'estudiantes'

    # Estructura: {"codigo": codigo, "nombre": nombre, "notas": [nota1, nota2, nota3]}

    estudiantes.append({"codigo": codigo, "nombre": nombre, "notas": [nota1, nota2, nota3]})

    return f"Estudiante {nombre} registrado correctamente. <a href='/'>Volver</a>"

 

 

@app.route("/listar")

def listar():

    # TODO: recorrer la lista de estudiantes con un FOR

    # TODO: usar la función calcular_promedio

    # TODO: usar un IF para mostrar si aprueba o reprueba

    salida = "<h2>Listado de estudiantes</h2><ul>"

    # Aquí deben ir los estudiantes
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
        salida += f"<li>{estudiante['nombre']} - Promedio: {promedio:.2f} - {estado}</li>"

    salida += "</ul><a href='/'>Volver</a>"

    return salida

 

 

@app.route("/buscar/<codigo>")

def buscar(codigo):

    i = 0

    encontrado = None

   

    # TODO: usar un WHILE para buscar el estudiante por código en la lista
    
    while i < len(estudiantes):
        if estudiantes[i]["codigo"] == codigo:
            encontrado = estudiantes[i]
            break
        i += 1


    if encontrado:

        return f"Estudiante encontrado: {encontrado['nombre']} - Notas: {encontrado['notas']} <br><a href='/'>Volver</a>"

    else:

        return "Estudiante no encontrado. <a href='/'>Volver</a>"

 

 

# -----------------------------

# Ejecutar la aplicación

# -----------------------------

if __name__ == "__main__":

    app.run(debug=True, port=5000)

 