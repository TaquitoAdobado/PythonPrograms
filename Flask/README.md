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

## 04_databases
 - sqlite_setup.py → configuración base de SQLite en Flask
 - crud.py → Creacion de CRUD basico