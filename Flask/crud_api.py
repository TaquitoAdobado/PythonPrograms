# En este script se implementaran los 4 metodos basicos de una API REST
# GET: Obtener recursos del servidor.
# POST: Crear un nuevo recurso
# PUT: Actualizar un recurso existente
# DELETE: Eliminar un recurso existente

from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos simulados:
usuarios = [
    {"id": 1, "nombre": "Daniel", "edad": 30},
    {"id": 2, "nombre": "Ana", "edad": 25}
]

# diccionario de usuarios indexado por id
usuarios_dict = {u["id"]: u for u in usuarios}  #  {1: {"id": 1, "nombre": "Daniel"}, 2: {"id": 2, "nombre": "Ana"},...}

# GET: Obtener lista completa
@app.route('/api/usuarios', methods=['GET'])
def get_users():
    """
    Devuelve la lista completa de usuarios
    """
    if not usuarios:
        return jsonify({"error": "No hay usuarios"}), 404   # 404 = Not Found
    return jsonify(usuarios), 200   # 200 = OK


# POST: Crear un nuevo usuario
@app.route('/api/usuarios', methods=['POST'])
def create_user():
    """
    Crea un nuevo usuario:
        Recibe de la solicitud los datos del usuario nuevo.
        Verifica que los datos no sean invalidos ni repetidos. 
        Agrega al usuario a la lista de usuarios y al diccionario de usuarios indexado por id.
        Finaliza devolviendo el recurso creado.
    """
    # Recibimos el json del cuerpo de la solicitud con el nuevo usuario
    data = request.get_json()

    # Validacion de datos
    if not data or "id" not in data or "nombre" not in data or "edad" not in data:
        return jsonify({"error": "Datos invalidos"}), 400    # 400 = Bad Request (Datos invalidos)
    
    # Validacion de id
    if data["id"] not in usuarios_dict:
        usuarios.append(data)
        usuarios_dict[data["id"]] = data

        # Respuesta con el recurso creado
        return jsonify(data), 201    # 201 = Recurso creado
    
    # ID duplicado
    else:
        return jsonify({"error": f"El id {data['id']} ya existe"}), 409    # 409 = Conflicto (id duplicado)
    

# PUT: Actualizacion TOTAL de un usuario
@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Actualizacion de un usuario existente (todos los datos)
    """
    # Traemos la informacion del usuario por id
    user = usuarios_dict.get(id)

    # Validacion de datos
    if not user:
        return jsonify({"error": f"El id {id} no existe"}), 404    # 404 = Not Found
    
    # Recibimos el json del cuerpo de la solicitud con los cambios
    changes = request.get_json()

    # Validacion de datos
    if not changes or "id" not in changes or "nombre" not in changes or "edad" not in changes:
        return jsonify({"error": "Datos invalidos"}), 400    # 400 = Bad Request (Datos invalidos)
    
    # Validamos que no se cambie el id
    if changes["id"] != id:
        return jsonify({"error": "No se puede cambiar el id"}), 400    # 400 = Bad Request (Datos invalidos)
    
    # Actualizamos el usuario en la lista de usuarios y en el diccionario indexado por id
    usuarios_dict[id].update(changes)
    for u in usuarios:
        if u["id"] == id:
            u.update(changes)
            break

    # Respuesta con el recurso actualizado
    return jsonify(usuarios_dict[id]), 200    # 200 = OK


# PATCH: Actualizacion PARCIAL de un usuario
@app.route('/api/usuarios/<int:id>', methods=['PATCH'])
def partial_update_user(id):
    """
    Actualiza datos de un usuario existente:
        Busca el usuario con el id de la solicitud.
        Verifica que los datos sean validos.
        Recibe de la solicitud los cambios del usuario.
        Verifica que los datos sean validos.
        Verifica que no se cambie el id.
        Actualiza el usuario en la lista de usuarios y en el diccionario indexado por id.
        Finaliza devolviendo el recurso actualizado. 
    """
    # Traemos la informacion actual del usuario
    user = usuarios_dict.get(id)

    # Validacion de id
    if not user:
        return jsonify({"error": f"El id {id} no existe"}), 404    # 404 = Not Found
    
    # Recibimos el json del cuerpo de la solicitud con los cambios
    changes = request.get_json()

    # Validacion de datos
    if not changes:
        return jsonify({"error": "Datos invalidos"}), 400    # 400 = Bad Request (Datos invalidos)
    
    # Validamos que no se cambie el id
    if "id" in changes and changes["id"] != id:
        return jsonify({"error": "No se puede cambiar el id"}), 400
    
    # Actualizamos los datos del usuario (en el diccionario indexado usuaios_dict)
    user.update(changes)
    # Tambien lo actualizamos en nuestra lista de usuarios de datos simulados
    for u in usuarios:
        if u["id"] == id:
            u.update(changes)
            break
    
    # Respuesta con el recurso actualizado
    return jsonify(user), 200    # 200 = OK


# DELETE: Eliminar un recurso existente
@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Elimina un usuario existente:
        Busca el usuario con el id de la solicitud.
        Elimina el usuario de la lista de usuarios y del diccionario indexado por id.
        Finaliza devolviendo el recurso eliminado.
    """
    # Traemos la informacion del usuario por id
    user = usuarios_dict.get(id)

    # Validacion de id
    if not user:
        return jsonify({"error": f"El id {id} no existe"}), 404    # 404 = Not Found
    
    # Eliminamos el usuario del diccionario indexado por id (usuarios_dict)
    del usuarios_dict[id]
    # Tambien lo eliminamos de nuestra lista de usuarios de datos simulados
    for u in usuarios:
        if u["id"] == id:
            usuarios.remove(u)
            break
    
    # Respuesta con el recurso eliminado
    return jsonify({"deleted_user": user}), 200    # 200 = OK


# Iniciamos el servidor
if __name__ == '__main__':  
    app.run(debug=True, port=5000, host='0.0.0.0')