# Actividad: Módulo 1 - Lección 2

Este repositorio contiene un ejemplo práctico de un servidor Flask diseñado como parte de la actividad sobre Arquitectura Cliente/Servidor y diseño de REST APIs. Incluye dos rutas principales y un diagrama básico de arquitectura del sistema.

## 📁 Estructura del proyecto

```
capstone_flask/
├── app.py                # Código del servidor Flask
├── requirements.txt      # Dependencias necesarias
├── test.http             # Archivo de pruebas con REST Client
└── diagrama_arquitectura.png  # Diagrama del sistema (sube tu imagen aquí)
```

## 🚀 Cómo ejecutar el servidor

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/capstone_flask.git
cd capstone_flask
```

2. Crea un entorno virtual y actívalo (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate     # En Linux/macOS
venv\Scripts\activate        # En Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta el servidor:

```bash
python app.py
```

El servidor correrá en `http://localhost:5000`.

## 📡 Endpoints

### GET `/info`

Devuelve información básica de la aplicación.

**Ejemplo de respuesta:**

```json
{
  "app": "Proyecto Capstone",
  "version": "1.0",
  "autor": "Tu Nombre"
}
```

### POST `/mensaje`

Recibe un mensaje en formato JSON y devuelve una respuesta personalizada.

**Body:**

```json
{
  "mensaje": "Hola desde el cliente"
}
```

**Respuesta:**

```json
{
  "respuesta": "Recibí tu mensaje: Hola desde el cliente"
}
```

## 🧪 Pruebas con REST Client

Usa el archivo `test.http` junto con la extensión **REST Client** en Visual Studio Code para probar fácilmente los endpoints.

## 🗂️ Diagrama de Arquitectura

El archivo `diagrama_arquitectura.png` representa la arquitectura básica del sistema incluyendo:

- Cliente
- Servidor Flask
- Base de Datos
- Flujo de comunicación (REST API)

## 📤 Entrega

Este repositorio debe subirse a GitHub como parte de la entrega de la actividad. Asegúrate de incluir:

- Código fuente (`app.py`)
- Archivo `test.http`
- Diagrama en formato imagen (`.png`, `.jpg`, etc.)
- Este archivo `README.md`

✍️ _Autor: Arodriguez 
📅 _Fecha: Abril 2025_
