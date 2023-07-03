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


@app.route('/perfil', methods=['POST', 'GET'])
def mostrar_perfil():
    if usuarioEnSesion is None:
        return render_template("SGDS-IVUI.html")  # Redirige al inicio de sesión si no ha iniciado sesión
    
    # Obtener datos personales del usuario
    usuario_datos = usuarioDatos1(usuarioEnSesion[0], usuarioEnSesion[1])  # Reemplaza "usuarioDatos" con la función adecuada para obtener los datos personales del usuario

    if usuario_datos is None:
        return "Usuario no encontrado en la base de datos 0"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos personales del usuario
    nombre = usuario_datos [0]
    dni = usuario_datos[1]
    telefono = usuario_datos[2]
    direccion = usuario_datos[3]
    fechaNacimiento = usuario_datos[4]

    # Obtener datos de donaciones del usuario
    usuario_donaciones = usuarioDonaciones(nombre)  # Reemplaza "usuarioDonaciones" con la función adecuada para obtener los datos de donaciones del usuario

    if usuario_donaciones is None:
        return "Usuario no encontrado en la base de datos 1"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos de donaciones del usuario
    donacion = usuario_donaciones[0]

    # Obtener datos de beneficios del usuario
    usuario_beneficios = usuarioBeneficios(nombre)  # Reemplaza "usuarioBeneficios" con la función adecuada para obtener los datos de beneficios del usuario

    if usuario_beneficios is None:
        return "Usuario no encontrado en la base de datos 2"  # Maneja el caso en el que el usuario no se encuentre en la base de datos

    # Obtén los datos de beneficios del usuario
    beneficio = usuario_beneficios[0]

    return render_template("perfil.html", nombre=nombre, dni=dni, telefono=telefono, direccion=direccion, fechaNacimiento=fechaNacimiento, donacion=donacion, beneficio=beneficio)


if __name__ == "__main__":
    app.run(debug=True)