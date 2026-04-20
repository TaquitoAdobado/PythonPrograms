from flask import Flask, render_template

app = Flask(__name__)

@app.route('/menu_hamburguesa')
def menu_hamburguesa():
    return render_template("menu_hamburguesa.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")