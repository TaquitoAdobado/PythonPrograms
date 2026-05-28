## Notas de estudio sobre Flask

## Instalacion
Para que funcione flask se debe instalar su libreria mediante:
```bash
pip install flask
```


## Estructura minima de un proyecto Flask

En carpeta raiz tener:
- app.py → archivo principal de la aplicación
- carpeta static → para archivos estaticos (css, js, imagenes)
- carpeta templates → para archivos html
- carpeta instance → para configuraciones y bases de datos
- requirements.txt → archivo con las dependencias del proyecto
- .gitignore → archivo para ignorar archivos en git
- README.md → archivo con la documentacion del proyecto


# Estudio Flask
Este es el orden por el que yo mismo estoy estudiando Flask, cada punto es un archivo con ejemplos y explicaciones.
Asi mismo cada archivo tiene sus propios templates, recomiendo revisarlos a la par para entender mejor cada concepto.
(El nombre de los templates usados esta dentro de cada archivo .py)

## 01_basics
- flask-setup.py → configuración inicial
- renderizar_template.py → render básico
- tipos_parametros.py → parámetros dinámicos

## 02_templates
- condicionales_jinja.py → condicionales en Jinja
- extends_include.py → herencia de plantillas
- variables_dinamicas.py → variables en templates

## 03_http
- metodo_get.py → manejo de GET
- metodo_post.py → manejo de POST
- redirect.py → redirecciones
- errores_html.py → manejo de errores

## 04_flash
- flash_messages.py → Uso de mensajes flash

## 05_databases
 - sqlite_setup.py → configuración base de SQLite en Flask
 - crud.py → Creacion de CRUD basico
 - Flask_sqlalchemy/README.md → Flask con ORM SQLAlchemy para consultas mas limpias. Se separa en carpeta aparte para no combinar archivos ni librerias, vease como una rama alternativa entre usar sqlite3 y el ORM SQLAlchemy para consultas sin instrucciones SQL.

## 06_Autenticación y sesiones.
- hash_passwords.py → Uso de Hash con werkzeug.security usando generate_password_hash y check_password_hash.
- sign_up.py → Registro de sesion con Flask, sqlite3 y werkzeug.security.
- session.py → Uso de session para manejo de sesiones seguras.
- restriccion_de_rutas.py → Restriccion de rutas con decoradores.

## 07_APIS.
- endpoint_JSON.py → Crear enpoints JSON con jsonify.
- crud_api.py → CRUD via API (GET, POST, PUT, PATCH, DELETE) utilizando endpoints REST.
- crud_api_marshmallow.py → CRUD via API REST usando esquemas Marshmallow.
- consumir_api.py → Consumo de APIs usando libreria requests.

## 08 Blueprints y modularización.
- blueprint.py / routes/blueprint_page.py → Separar rutas en diferentes archivos usando Blueprint.
- config.py / app.py → Separar logica de configuraciones y leer claves desde .env

## 09 Testing con Pytest.
- tests/ -> Carpeta contenedora de pruebas unitarias y funcionales
- conftest.py / test_home.py -> Prueba unitaria de endpoint mediante simulacion de request usando pytest y app.test_client().

## Estructura avanzada de un proyecto Flask

project/
│── app.py                  # Punto de entrada: instancia Flask y registro de Blueprints
│── config.py               # Configuración global (Dev, Test, Prod)
│── .env                    # Variables sensibles (SECRET_KEY, claves API, DB URL)
│── instance/               # Datos locales (Bases de datos)
│   └── app.db
│── routes/                 # Endpoints
│   ├── home.py                 # Rutas que renderizan templates HTML
│   ├── weather.py              # Rutas que revuelven JSON
│── services/               # Lógica de negocio / APIs externas
│   ├── weather_service.py      # Consumo de APIs externas
│
│── models/                 # Datos / ORM / esquemas Marshmallow
│   ├── user.py             # Modelo de usuario
│── templates/              # HTML con Jinja2
│   ├── index.html
│── static/                 # Archivos estáticos (CSS, JS, imágenes)
│   ├── style.css
│   ├── script.js
│── tests/                  # Pruebas unitarias
│   ├── test_home.py
│   ├── conftest.py