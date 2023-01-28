
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route("/operacion", methods=["GET","POST"])
def operaciones():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        operacion= request.form.get("operaciones")
        if(operacion == "suma"):
            return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif(operacion == "resta"):
            return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif(operacion == "multiplicacion"):
            return "<h1> La multiplicacion es: {} </h1>".format(str(int(num1)*int(num2)))
        elif(operacion == "division"):
            return "<h1> La division es: {} </h1>".format(str(int(num1)/int(num2)))
            
    else: 
        return '''
            <form action = '/operacion' method="POST">
            <label>N1: </label>
            <input type="text" name="num1"/></br></br>
            <label>N2: </label>
            <input type="text" name="num2"/></br></br>
            <input type="radio" name="operaciones" value="suma">
            <label>Suma</label>
            <input type="radio" name="operaciones" value="resta">
            <label>Resta</label>
            <input type="radio" name="operaciones" value="multiplicacion">
            <label>Multiplicacion</label>
            <input type="radio"name="operaciones" value="division">
            <label>Division</label></br></br>
            <input type="submit" value="Calcular"/></br></br> 
            </form>
        '''
    
if __name__=="__main__":
    app.run(debug=True, port=3000)