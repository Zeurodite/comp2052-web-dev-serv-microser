from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        'app': 'Proyecto Capstone',
        'version': '1.0',
        'autor': 'Tu Nombre'
    })

# Ruta POST
@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    mensaje = data.get('mensaje', 'No se envió mensaje')
    return jsonify({'respuesta': f'Recibí tu mensaje: {mensaje}'})

if __name__ == '__main__':
    app.run(debug=True)
