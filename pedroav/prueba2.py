#coding:UTF-8 
'''
Created on 19/1/2015

@author: PC30
'''
'''mostrar en en navegador'''

from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")#su funcion es buscar desde el navegador 
def inicio():
    x="Interaccion entre python y HTML5"
    return render_template("prueba.html", dato=x)

@app.route("/itsae")#su funcion es buscar desde el navegador 
def Itsae():
    return "Hola Mundo ITSAE"
    

if __name__ == '__main__':
    app.run("127.0.0.1", 5050, True)