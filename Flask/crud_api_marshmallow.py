# En este script se implementaran los 4 metodos basicos de una API REST
# Tambien se implementa el uso de marshmallow para definir esquemas de validacion.
# De esta forma no se podra crear o modificar un recurso con datos fuera de los esquemas.

from flask import Flask, request, jsonify

#Se importa la libreria marshmallow
from marshmallow import Schema, fields, ValidationError


app = Flask(__name__)

# Datos simulados:
usuarios = [
    {"id": 1, "name": "Daniel", "age": 30},
    {"id": 2, "name": "Ana", "age": 25}
]


# diccionario de usuarios indexado por id
usuarios_dict = {u["id"]: u for u in usuarios}  #  {1: {"id": 1, "nombre": "Daniel"}, 2: {"id": 2, "nombre": "Ana"},...}


# Se crea el esquema que tendran los datos.
class UserSchema(Schema):
    id = fields.Int(required = True) # El id es requerido
    name = fields.Str(required = True) # El name es requerido
    age = fields.Int(required = True) # El age es requerido

# Se crea la instancia del esquema
user_schema = UserSchema()


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
    try:
        data = user_schema.load(request.get_json()) # Recibe el JSON y valida las entradas con las del esquema.
    
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400    # 400 = Bad Request
    
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
    
    # Recibimos el json del cuerpo de la solicitud con los cambios y los validamos con el esquema.
    try:
        changes = user_schema.load(request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400    # 400 = Bad Request
    
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
    
    # Recibimos el json del cuerpo de la solicitud con los cambios y los validamos con el esquema
    try:
        changes = user_schema.load(request.get_json(), partial = True)  # partial=True para permitir cambios parciales
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400    # 400 = Bad Request
    
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