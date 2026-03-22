# Flask + SQLAlchemy

Este repositorio no es un proyecto en producción, sino un conjunto de **notas personales** para aprender cómo estructurar una aplicación Flask con SQLAlchemy y SQLite.
La idea es documentar cada paso, cada archivo y cada concepto para tener una referencia clara en el futuro.

## Estructura actual
```
flask_sqlalchemy/
|
|── app.py               # Archivo principal de la aplicación Flask
├── extensions.py        # Centraliza las extensiones (ej. SQLAlchemy)
├── models/              # Carpeta que contiene los modelos de la base de datos
│   ├── __init__.py      # Importa y centraliza los modelos
│   └── user.py          # Modelo User con sus columnas y métodos
├── instance/            # Carpeta donde se guarda la base de datos SQLite
│   └── database.db      # Archivo físico de la base de datos (se crea aquí)
├── static/              # Archivos estáticos (CSS, JS, imágenes)
├── templates/           # Plantillas HTML renderizadas por Flask
├── requirements.txt     # Dependencias del proyecto
├── README.md            # Notas de aprendizaje y documentación
└── .gitignore           # Exclusiones (venv, __pycache__, *.db, etc.)
```

## Pasos documentados

1. **Creación de modelos**  
   - Se definen las clases en `models/` heredando de `db.Model`.  
   - Cada clase representa una tabla y cada atributo una columna.  
   - Ejemplo: `User`.

2. **Configuración de la aplicación (`app.py`)**  
   - Se crea la instancia de Flask.  
   - Se configura la URI de conexión:  
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///instance/database.db"
     ```
   - Se desactiva el rastreo de modificaciones:  
     ```python
     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
     ```
   - Se vincula la extensión con la app:  
     ```python
     db.init_app(app)
     ```

3. **Creación de la base de datos**  
   - Se generan las tablas dentro del contexto de la aplicación:  
     ```python
     with app.app_context():
         db.create_all()
     ```

4. **Validación inicial**  
   - Confirmar que el archivo `database.db` existe en la carpeta `instance`.  
   - Verificar que la tabla `users` fue creada correctamente.