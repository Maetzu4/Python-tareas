# Tareas de Python

Este repositorio contiene varios ejercicios y tareas de Python, incluyendo aplicaciones web con Flask.

## Proyectos incluidos
- `jinja2/`: Ejemplo de uso de plantillas Jinja2 con Flask.
- `mi_app/`: Ejercicio avanzado para calcular promedios de estudiantes recibiendo datos desde la URL.

## Requisitos previos
- [Python 3.x](https://www.python.org/downloads/) instalado en tu sistema.

## Configuración y ejecución local

Para correr estos proyectos correctamente, es muy recomendable utilizar un entorno virtual para no mezclar las dependencias de este proyecto con las de otros. Sigue estos pasos:

### 1. Clonar el repositorio (si estás descargando el proyecto)
Abre tu terminal y clona este repositorio en tu máquina local:
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd Tareas-de-python
```

### 2. Crear un entorno virtual
Crea un entorno virtual dentro de la carpeta del proyecto. Esto creará una carpeta llamada `.venv`:
```bash
# En Windows:
python -m venv .venv

# En macOS/Linux:
python3 -m venv .venv
```

### 3. Activar el entorno virtual
Antes de instalar paquetes o correr las aplicaciones, debes activar el entorno:
```bash
# En Windows:
.venv\Scripts\activate

# En macOS/Linux:
source .venv/bin/activate
```
*Nota: Sabrás que está activado porque verás `(.venv)` al inicio de la línea de comandos en tu terminal.*

### 4. Instalar las dependencias
Para estos proyectos se requiere Flask. Una vez activado el entorno, instálalo ejecutando:
```bash
pip install flask
```

### 5. Ejecutar las aplicaciones

**Para el proyecto de Jinja2:**
```bash
python jinja2/app.py
```

**Para el proyecto del Promedio (mi_app):**
```bash
python mi_app/app.py
```

Una vez que el servidor esté corriendo, la terminal te indicará que está funcionando (usualmente en `http://127.0.0.1:5000`). 
- Abre esa dirección en tu navegador.
- En el caso específico de `mi_app`, prueba navegando a: `http://localhost:5000/estudiante/Ana/3.5/4.0/2.8`

### 6. Desactivar el entorno
Cuando termines de trabajar y quieras salir del entorno virtual, simplemente ejecuta en la terminal:
```bash
deactivate
```
