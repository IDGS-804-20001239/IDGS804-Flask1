
from flask import Flask
from flask import request
from flask import render_template
from datetime import date
import os

app=Flask(__name__)

@app.route("/datos")
def signo():
    return render_template("signoZodiacal.html")


@app.route("/datos", methods=["POST"])
def datos():
    nombre=request.form.get("nombre")
    apaterno=request.form.get("apaterno") 
    amaterno=request.form.get("amaterno")

    dia=request.form.get("dia")
    diaActual = date.today().day
    mes=request.form.get("mes") 
    mesActual = date.today().month
    anio=request.form.get("anio") 
    anioActual = date.today().year

    edad= anioActual - int(anio)
    #Calcular Edad
    if int(mes) > mesActual:
          if int(dia) > diaActual:
               edad = edad - 1

    p1=request.form.get("p1")
    p2=request.form.get("p2") 
    p3=request.form.get("p3") 
    p4=request.form.get("p4") 
    p5=request.form.get("p5") 
    

   #Signo Zodiacal
    if int(anio) == 1912 or int(anio) == 1924 or int(anio) == 1936 or int(anio) == 1948 or int(anio) == 1960 or int(anio) == 1972 or int(anio) == 1984 or int(anio) == 1996 or int(anio) == 2008 or int(anio) == 2020 :
         zodiacal="Rata"
    elif int(anio) == 1913 or int(anio) == 1925 or int(anio) == 1937 or int(anio) == 1949 or int(anio) == 1961 or int(anio) == 1973 or int(anio) == 1985 or int(anio) == 1997 or int(anio) == 2009 or int(anio) == 2021 :
         zodiacal="Buey"
    elif int(anio) == 1914 or int(anio) == 1926 or int(anio) == 1938 or int(anio) == 1950 or int(anio) == 1962 or int(anio) == 1974 or int(anio) == 1986 or int(anio) == 1998 or int(anio) == 2010 or int(anio) == 2022 :
         zodiacal="Tigre"
    elif int(anio) == 1915 or int(anio) == 1927 or int(anio) == 1939 or int(anio) == 1951 or int(anio) == 1963 or int(anio) == 1975 or int(anio) == 1987 or int(anio) == 1999 or int(anio) == 2011 or int(anio) == 2023 :
         zodiacal="Conejo"
    elif int(anio) == 1916 or int(anio) == 1928 or int(anio) == 1940 or int(anio) == 1952 or int(anio) == 1964 or int(anio) == 1976 or int(anio) == 1988 or int(anio) == 2000 or int(anio) == 2012 :
         zodiacal="Dragon"
    elif int(anio) == 1917 or int(anio) == 1929 or int(anio) == 1941 or int(anio) == 1953 or int(anio) == 1965 or int(anio) == 1977 or int(anio) == 1989 or int(anio) == 2001 or int(anio) == 2013 :
         zodiacal="Serpiente"
    elif int(anio) == 1918 or int(anio) == 1930 or int(anio) == 1942 or int(anio) == 1954 or int(anio) == 1966 or int(anio) == 1978 or int(anio) == 1990 or int(anio) == 2002 or int(anio) == 2014 :
         zodiacal="Caballo"
    elif int(anio) == 1919 or int(anio) == 1931 or int(anio) == 1943 or int(anio) == 1955 or int(anio) == 1967 or int(anio) == 1979 or int(anio) == 1991 or int(anio) == 2003 or int(anio) == 2015 :
         zodiacal="Oveja"    
    elif int(anio) == 1920 or int(anio) == 1932 or int(anio) == 1944 or int(anio) == 1956 or int(anio) == 1968 or int(anio) == 1980 or int(anio) == 1992 or int(anio) == 2004 or int(anio) == 2016 :
         zodiacal="Mono"
    elif int(anio) == 1921 or int(anio) == 1933 or int(anio) == 1945 or int(anio) == 1957 or int(anio) == 1969 or int(anio) == 1981 or int(anio) == 1993 or int(anio) == 2005 or int(anio) == 2017 :
         zodiacal="Gallo"
    elif int(anio) == 1922 or int(anio) == 1934 or int(anio) == 1946 or int(anio) == 1958 or int(anio) == 1970 or int(anio) == 1982 or int(anio) == 1994 or int(anio) == 2006 or int(anio) == 2018 :
         zodiacal="Perro"
    elif int(anio) == 1923 or int(anio) == 1935 or int(anio) == 1947 or int(anio) == 1959 or int(anio) == 1971 or int(anio) == 1983 or int(anio) == 1995 or int(anio) == 2007 or int(anio) == 2019 :
         zodiacal="Cerdo"
    cont=0

    #Preguntas y Respuestas correctas
    if p1=="b":
        cont=1

    if p2=="b":
        cont=cont+1
    
    if p3=="b":
        cont=cont+1
    
    if p4=="b":
        cont=cont+1
    
    if p5=="b":
        cont=cont+1
    
    return render_template("respuestaSigno.html", 
    edad=edad,zodiacal=zodiacal, nombre=nombre,apaterno=apaterno,amaterno=amaterno, cont=cont)
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    clearConsole = lambda: os.system('cls' if os.name in ('nombre', 'apaterno') else 'clear')

    clearConsole()
    
if __name__=="__main__":
    app.run(debug=True, port=3000)