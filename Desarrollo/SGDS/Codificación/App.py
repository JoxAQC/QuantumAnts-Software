
from modelo.SGDS_IVR08 import *
import json
import os

from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='vista/templates', static_folder='vista/static')

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

usuarioEnSesion = None  
carrito = []
user = None
password = None
txt = None
txt2 = None
tipo = None

@app.route('/login',methods=['POST', 'GET'])
def iniciar_sesion():
    # output = request.form.to_dict()
    # print(output)
    # global user
    # usuario = output["usuario"]
    # user = usuario
    # global password
    # contraseña = output["contraseña"]
    # password = contraseña

    # global usuarioEnSesion 
    # usuarioEnSesion = buscar_usuario([],usuario, contraseña)


    # if usuarioEnSesion is None:
    #     mensaje = "Usuario no registrado, inténtelo nuevamente, por favor"
    #     global txt
    #     txt = None
    #     global txt2
    #     txt2 = None
    #     return render_template("index.html", mensaje = mensaje)
    # else:
        return render_template("SGDS-IVUI.html")
    
   
@app.route('/crear_cuenta')
def crear_cuenta():
    # if txt != None and txt2 != None:
    #     return render_template("page.html", txt = txt, txt2 = txt2)
    # else:
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


if __name__ == "__main__":
    app.run(debug=True)