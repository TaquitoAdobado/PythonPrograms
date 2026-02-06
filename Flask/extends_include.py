"""
Este archivo se relaciona con los templates:
- padre.html
- hijo.html
- footer.html

Todos los templates se almacenaron en la carpeta templates/extends_input/ por temas de organizacion personal
por lo cual se especifica como parametro la instancia de Flask llamada app

En este ejemplo se renderiza el template hijo.html que extiende de padre.html, o sea, hereda su estructura y contenido reemplazando bloques definidos.
Para mas informacion revisar los comentarios en los archivos de los templates relacionados listados arriba.
"""
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates/extends_include/")

@app.route('/')
def home():
    return render_template("hijo.html")

if __name__=="__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")