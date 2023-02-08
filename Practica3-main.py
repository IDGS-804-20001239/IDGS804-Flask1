
from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)

@app.route("/cinepolis")
def cine():
    return render_template("cinepolis.html")

@app.route("/cinepolis", methods=["post"])
def cineRes():
        nombre= request.form.get("nombre")
        numPersonas= request.form.get("numPersonas") 
        numb= request.form.get("numBoletos")
        tarjeta= request.form.get("tarjeta")
        
        if int(numb) > int(numPersonas)*7:
             res="No se pudo procesar la compra la cantidad de boletos por persona debe ser menor a 7"
        else:
            res=int(numb)*12
            if(int(numb) > 5):
                res= (res*.85)

            elif(int(numb) == 3 | int(numb)==4 | int(numb)==5):
                res= (res*.90)
            else: 
                res=res

        if (tarjeta == "si"):
                res=res*.90
        
        return render_template("cinepolis.html",nombre=nombre, numPersonas=numPersonas, numb=numb, res=res)

if __name__=="__main__":
    app.run(debug=True, port=3000)