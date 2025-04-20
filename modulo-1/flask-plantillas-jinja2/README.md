# Aplicación Flask con Plantillas Jinja2

Este proyecto es una aplicación web básica creada con Flask que utiliza plantillas HTML con Jinja2 para mostrar contenido dinámico. Forma parte de una actividad académica enfocada en comprender la separación entre lógica y presentación en una aplicación web moderna.

## 📁 Estructura del Proyecto

```
flask-plantillas-jinja2/
├── app.py
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── pagina1.html
│   └── pagina2.html
├── requirements.txt
└── README.md
```

## 🚀 Cómo Ejecutar

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/flask-plantillas-jinja2.git
cd flask-plantillas-jinja2
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`.

## 🌐 Funcionalidad

- **Página principal**: Muestra un mensaje de bienvenida.
- **Página de Tecnologías** (`/pagina1`): Lista de tecnologías enviadas desde el back-end.
- **Página de Usuarios** (`/pagina2`): Tabla con datos dinámicos de usuarios.

## 🧱 Uso de Plantillas

Se utiliza una plantilla base (`base.html`) y las páginas heredan su estructura con `{% extends %}` y bloques `{% block %}`. Esto permite mantener un diseño coherente y modular.

## 🖼️ Capturas de Pantalla

Capturas incluidas en el documento `DOCUMENTACION.pdf`.

## 📄 Documento de Entrega

El archivo `DOCUMENTACION.pdf` explica el funcionamiento de la app e incluye capturas de las distintas vistas.

## 📌 Autor

**Abdiel Rodríguez**  
Abril 2025  
Repositorio: [GitHub](https://github.com/tu_usuario/flask-plantillas-jinja2)
