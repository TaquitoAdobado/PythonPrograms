# Cada clase representa una tabla y cada atributo representa una columna de la tabla.

from extensions import db

# Definimos la clase User heredando de db.Model
# La clase Model aporta la capacidad de convertir una clase normal en una tabla de base de datos
class User(db.Model):
    __tablename__ = 'users' # Nombre de la tabla en la base de datos
    
    # Definimos las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        ''' Devuelve un string con la informacion del usuario '''
        return f"""
        Usuario {self.id}: {self.first_name} {self.last_name}
        Edad: {self.age}
        Email: {self.email}
        """