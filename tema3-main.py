
from flask import Flask




app=Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo!"

#Paramentros String
@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

#Parametron INT
@app.route("/numero/<int:n>")
def numero(n):
    return "Número {}".format(n)

# Más de un parametro
@app.route("/user/<int:id>/<string:username>")
def usern(id, username):
    return "ID: {} nombre: {}".format(id,username) 

#Suma
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es {} ".format(n1+n2)

if __name__=="__main__":
    app.run(debug=True, port=3000)