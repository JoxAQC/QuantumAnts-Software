from modelo.Donante import Donante
from modelo.Credencial import Credencial
from modelo.SGDS_IVR08 import *
from controlador.ControlPerfil import *
import json
import os

from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='vista/templates', static_folder='vista/static')

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

usuarioEnSesion = None  

@app.route('/login')
def inciar_sesion():
    return render_template("SGDS-IVUI.html")
<<<<<<< HEAD

@app.route('/loginin',methods=['POST', 'GET'])
def ingresar():
    output = request.form.to_dict()
    global user
    usuario = output["usuario"]
    user = usuario
    global password
    contraseña = output["contraseña"]
    password = contraseña

    global usuarioEnSesion 
    usuarioEnSesion = buscar_usuario(usuario, contraseña)


    if usuarioEnSesion is None:
        mensaje = "Usuario no registrado, inténtelo nuevamente, por favor"
        return render_template("SGDS-IVUI.html", mensaje = mensaje)
    else:
        return render_template("index.html")
    
=======

@app.route('/loginin',methods=['POST', 'GET'])
def ingresar():
    output = request.form.to_dict()
    global user
    usuario = output["usuario"]
    user = usuario
    global password
    contraseña = output["contraseña"]
    password = contraseña

    global usuarioEnSesion 
    usuarioEnSesion = buscar_usuario(usuario, contraseña)


    if usuarioEnSesion is None:
        mensaje = "Usuario no registrado, inténtelo nuevamente, por favor"
        return render_template("SGDS-IVUI.html", mensaje = mensaje)
    else:
        return render_template("index.html")



>>>>>>> 334e096af6dfa21503b2556a55eb48e60916cdae
   
@app.route('/crear_cuenta')
def crear_cuenta():
    # output = request.form.to_dict()
    # user = output["usuario"]
    # password = output["contraseña"]
    # name = output["nombre"]
    # lastname = output["apellido"]
    # mail = output["correo"]

    # new_User = Donante(user, password, name, lastname, mail)
    # new_User.registrar()

    # register = "Registrado correctamente, inicie sesión para continuar"

    # return render_template("SGDS-IVUI.html", register = register)
        return render_template("crear_cuenta.html")

@app.route('/conocenos')
def conocenos():
    return render_template("conocenos.html")

@app.route('/transparencia')
def transparencia():
    return render_template("transparencia.html")

@app.route('/contactanos')
def contactanos():
    return render_template("contactanos.html")

@app.route('/sedes')
def sedes():
    return render_template("sedes.html")

@app.route('/solicitud')
def solicitud():
    return render_template("solicitud.html")

# @app.route('/registrar',methods=['POST', 'GET'])
# def registrar():
#     output = request.form.to_dict()
#     user = output["usuario"]
#     password = output["contraseña"]
#     name = output["nombre"]
#     lastname = output["apellido"]
#     mail = output["correo"]

#     new_User = Donante(user, password, name, lastname, mail)
#     new_User.registrar()

#     register = "Registrado correctamente, inicie sesión para continuar"

#     return render_template("SGDS-IVUI.html", register = register)


@app.route('/perfil',methods=['POST', 'GET'])
def mostrar_perfil():
       return render_template("perfil.html")

@app.route('/perfil1',methods=['POST', 'GET'])
def datosPersonales():
    if usuarioEnSesion is None:
        return render_template("SGDS-IVUI.html")  # Redirige al inicio de sesión si no ha iniciado sesión

    nombre = usuarioEnSesion[1]  # Obtén el nombre del usuario desde la sesión (asegúrate de que el índice sea correcto)
    usuario = usuarioDatos(nombre)  # Reemplaza "buscar_usuario" con la función adecuada para buscar los datos del usuario en la base de datos

    if usuario is None:
        return "Usuario no encontrado en la base de datos"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos del usuario de la variable "usuario"
    dni = usuario[0]
    telefono = usuario[1]
    direccion = usuario[2]
    fechaNacimiento = usuario[3]

    return render_template("perfil.html", nombre=nombre, dni=dni, telefono=telefono, direccion=direccion, fechaNacimiento=fechaNacimiento)     

@app.route('/perfil2', methods=['POST', 'GET'])
def datosDonaciones():
    if usuarioEnSesion is None:
            return render_template("SGDS-IVUI.html")  # Redirige al inicio de sesión si no ha iniciado sesión

    nombre = usuarioEnSesion[1]  # Obtén el nombre del usuario desde la sesión (asegúrate de que el índice sea correcto)
    usuario = usuarioDonaciones(nombre)  # Reemplaza "buscar_usuario" con la función adecuada para buscar los datos del usuario en la base de datos

    if usuario is None:
        return "Usuario no encontrado en la base de datos"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos del usuario de la variable "usuario"
    donacion = usuario[0]

    return render_template("perfil.html", nombre=nombre, donacion = donacion)

@app.route('/perfil3', methods=['POST', 'GET'])
def datosBeneficios():
    if usuarioEnSesion is None:
            return render_template("SGDS-IVUI.html")  # Redirige al inicio de sesión si no ha iniciado sesión

    nombre = usuarioEnSesion[1]  # Obtén el nombre del usuario desde la sesión (asegúrate de que el índice sea correcto)
    usuario = usuarioBeneficios(nombre)  # Reemplaza "buscar_usuario" con la función adecuada para buscar los datos del usuario en la base de datos

    if usuario is None:
        return "Usuario no encontrado en la base de datos"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos del usuario de la variable "usuario"
    beneficio = usuario[0]

    return render_template("perfil.html", nombre=nombre, benficio = beneficio)


if __name__ == "__main__":
    app.run(debug=True)