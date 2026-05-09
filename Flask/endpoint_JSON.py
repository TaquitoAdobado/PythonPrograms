# Un endpoint JSON es una ruta que devuelve datos en formato JSON, no HTML.
# Se usa jsonify() para convertir listas, diccionarios o estructuras de python en JSON valido.
# Esto permite que otras aplicaciones consuman tus datos.

from flask import Flask, jsonify
app = Flask(__name__)

# Datos simulados:
usuarios = [
    {"id": 1, "nombre": "Daniel"},
    {"id": 2, "nombre": "Ana"}
]

# Endpoint basico: devolver lista completa
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios), 200 #     200 = OK

# Endpoint con busqueda por id
    # Diccionario indexado por id
usuarios_dict = {u["id"]: u for u in usuarios}  #  {1: {"id": 1, "nombre": "Daniel"}, 2: {"id": 2, "nombre": "Ana"},...}

@app.route('/api/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = usuarios_dict.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404 #   404 = Not Found
    return jsonify(usuario), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')