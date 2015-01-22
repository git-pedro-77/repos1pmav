# coding:utf-8
'''
Created on 19/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import PersonaDao
from flask import render_template, request, redirect, url_for




@app.route("/mainpersona")# para entar a la pagina por main persona al metodo
def mainpersona():
    objR=PersonaDao.PersonaDao().reportarPersona()#llamar al reporte
    return render_template("prueba.html", data=objR)#enviando al archivo html y ahi organizarlo


@app.route("/addPersona", methods=['POST'])
def addPersona():
    nombre=request.form.get('nombre', type=str)
    apell_paterno=request.form.get('apaterno', type=str)
    apell_materno=request.form.get('amaterno', type=str)
    dni=request.form.get('Cedula', type=str)
    fecha_nacimiento=request.form.get('fecha_nacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)
    
    
    PersonaDao.PersonaDao().insertarPersona(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('mainpersona'))

@app.route("/buscarauto")# para entar a la pagina por main persona al metodo
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objR=PersonaDao.PersonaDao().buscarPersonaNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objR #enviando al archivo html y ahi organizarlo

@app.route("/eliminardato")# para entar a la pagina por main persona al metodo
def eliminarPersonaDato():
    datoeli=str(request.args.get('btneliminar'))
    objR=PersonaDao.PersonaDao().eliminarPersona(datoeli)
    return objR


@app.route("/buscardato")# para entar a la pagina por main persona al metodo
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=PersonaDao.PersonaDao().buscarPersonaDato(nombre)
    return render_template("prueba.html", data=objR)
