
from flask import Flask
from flask import request
from flask import render_template


app=Flask(__name__)

@app.route("/datos")
def datos():
    nombre: "Amanda"
    lista1=["uno","dos","tres","cuatro"]
    return render_template("datos.html",nombre=nombre,lista=lista1)
if __name__=="__main__":
    app.run(debug=True,port=3000)