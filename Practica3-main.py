
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
        max=7*int(numPersonas)
        if int(numb) > int(max):
            resp="No se pueden comprar más de 7 boletos por persona"
            return render_template("cinepolis.html",resp=resp)
        else:
            res=int(numb)*12
            if(int(numb) > 5):
                res= res*.85

            elif(int(numb) == 3 or int(numb) ==4 or int(numb) ==5):
                res= res*.90
            else: 
                res=res

        if (tarjeta == "si"):
                res = res * 0.90
        else:
            res=res 
        return render_template("cinepolis.html",nombre=nombre, numPersonas=numPersonas, numb=numb, res=res)

if __name__=="__main__":
    app.run(debug=True, port=3000)