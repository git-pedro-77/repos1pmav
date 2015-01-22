# coding:utf-8
'''
Created on 19/1/2015

@author: Programacion
'''

from ec.edu.itsae.conn import DBcon
import json 


class PersonaDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarPersona(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from personas ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada
    
    def insertarPersona(self, nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado):
        con=self.conexion().connect()
        sql= """insert into personas(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado)
                             values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %i)
                             """ %(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado) 
                            #porcentaje s es modleo strint o cadena
                            #i es solo numero
        print sql    #Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
        #deber actualizar y eliminar
    def eliminarPersona(self,datoeli):
        con=self.conexion().connect()
        sql=( """delete from personas where idpersona=('%s') """) %(datoeli)
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte
    
   
    
    def buscarPersonaNombre(self, datobusca):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(""" select CONCAT (nombre,' ', apell_paterno,' ', apell_materno) as value, idpersona as id from personas where upper(CONCAT (nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna,row))) #dict = diccionario, zip = para unir las las dos columnas
        return json.dumps(lista, indent=2) 
    
    def buscarPersonaDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        sql=""" select * from personas where upper(CONCAT (nombre,' ', apell_paterno,' ', apell_materno)) like upper('%s') """ %("%"+datobuscado+"%")
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 
    
    
    
    def validarUsuario(self, usuario,clave):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from trabajador where usuario='%s' and clave='%s' """ %(usuario, clave))
        reporte=con.fetchall() 
        return reporte 
    
    