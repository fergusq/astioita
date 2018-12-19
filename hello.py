from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

name = "Essi Esimerkki"

nlist = [1, 1, 2, 3, 5, 8, 11]

items = [Item("Eka"), Item("Toka"), Item("Kolmas"), Item("Neljäs")]

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", name=name, list=nlist, items=items)

if __name__ == "__main__":
    app.run(debug=True)
