from flask import Flask, render_template

app = Flask(__name__)

pacientes = [
    {
        "id": 1,
        "nombre": "Carlos Pérez",
        "edad": 70,
        "prioridad": "Alta",
        "especialidad": "Cardiología",
        "estado": "En espera"
    },
    {
        "id": 2,
        "nombre": "Ana Gómez",
        "edad": 25,
        "prioridad": "Media",
        "especialidad": "Traumatología",
        "estado": "Atendido"
    },
    {
        "id": 3,
        "nombre": "Luis Silva",
        "edad": 45,
        "prioridad": "Baja",
        "especialidad": "Medicina General",
        "estado": "En espera"
    },
    {
        "id": 4,
        "nombre": "María López",
        "edad": 65,
        "prioridad": "Alta",
        "especialidad": "Neurología",
        "estado": "Atendido"
    },
    {
        "id": 5,
        "nombre": "Jorge Medina",
        "edad": 35,
        "prioridad": "Media",
        "especialidad": "Gastroenterología",
        "estado": "En espera"
    },
    {
        "id": 6,
        "nombre": "Elena Castro",
        "edad": 80,
        "prioridad": "Alta",
        "especialidad": "Cardiología",
        "estado": "En espera"
    },
    {
        "id": 7,
        "nombre": "Pedro Ruiz",
        "edad": 50,
        "prioridad": "Baja",
        "especialidad": "Traumatología",
        "estado": "Atendido"
    },
    {
        "id": 8,
        "nombre": "Sofía Morales",
        "edad": 22,
        "prioridad": "Alta",
        "especialidad": "Pediatría",
        "estado": "En espera"
    },
    {
        "id": 9,
        "nombre": "Ricardo Torres",
        "edad": 62,
        "prioridad": "Media",
        "especialidad": "Medicina Interna",
        "estado": "En espera"
    },
    {
        "id": 10,
        "nombre": "Valentina Rivas",
        "edad": 15,
        "prioridad": "Baja",
        "especialidad": "Pediatría",
        "estado": "Atendido"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pacientes")
def mostrar_pacientes():
    return render_template("pacientes.html", pacientes=pacientes)

@app.route("/prioridad/<nivel>")
def pacientes_prioridad(nivel):
    filtrados = [p for p in pacientes if p['prioridad'].lower() == nivel.lower()]
    return render_template("prioridad.html", pacientes=filtrados, nivel=nivel.capitalize())

@app.route("/estadisticas")
def estadisticas():
    total = len(pacientes)
    prioridad_counts = {}
    for p in pacientes:
        prioridad_counts[p['prioridad']] = prioridad_counts.get(p['prioridad'], 0) + 1
        
    atendidos = sum(1 for p in pacientes if p['estado'] == 'Atendido')
    en_espera = sum(1 for p in pacientes if p['estado'] == 'En espera')
    
    return render_template("estadisticas.html", 
                           total=total, 
                           prioridad_counts=prioridad_counts, 
                           atendidos=atendidos, 
                           en_espera=en_espera)

if __name__ == "__main__":
    app.run(debug=True)
