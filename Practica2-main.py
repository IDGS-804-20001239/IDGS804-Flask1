
from flask import Flask
from flask import request
from flask import render_template
import math

app=Flask(__name__)

@app.route("/distancia")
def distancia():
    return render_template("distancia.html")

@app.route("/total", methods=["POST"])
def total():   
    x1=float(request.form.get("X1"))
    x2=float(request.form.get("X2"))
    y1=float(request.form.get("Y1"))
    y2=float(request.form.get("Y2"))
    res= math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    return render_template("resultadoDis.html",x1=x1,x2=x2,y1=y1,y2=y2,res=res)

if __name__=="__main__":
    app.run(debug=True,port=3000)