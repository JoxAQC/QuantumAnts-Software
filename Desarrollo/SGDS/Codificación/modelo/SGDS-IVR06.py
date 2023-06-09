import sqlite3 as sql
import os 
import bcrypt
import re
import smtplib
from email.mime.text import MIMEText

def conectar_bd():  
        # Obtener la ruta absoluta al archivo de base de datos
        current_directory = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

        # Establecer conexión con la base de datos
        conn = sql.connect(db_path)
        return conn


def encriptar(contraseña):
    # Generar una sal aleatoria
    salt = bcrypt.gensalt()

    # Encriptar la contraseña utilizando la sal generada
    contraseña_encriptada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)

    return contraseña_encriptada


def verificar_contraseña(contraseña, contraseña_encriptada):
    # Verificar si la contraseña coincide con la contraseña encriptada
    if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada.encode('utf-8')):
        print("Contraseña válida. Acceso permitido.")
    else:
        print("Contraseña inválida. Acceso denegado.")


def encriptar_contrasenia(idCredencial):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        #Obtengo la contraseña registrada por el usuario y que se encuentra en la base de datos
        cursor.execute("SELECT password FROM Credencial WHERE idCredencial = ?",(idCredencial,))
        password_actual = cursor.fetchone()[0]
        #Encripto la contraseña
        contraseña_encriptada = encriptar(password_actual)
        #Hago el cambio de la acontraseña actual porla encriptada en la base de datos
        cursor.execute("UPDATE Credencial SET password = ? WHERE idCredencial = ?",(contraseña_encriptada,idCredencial))
        conn.commit()
        print("contrasenia encriptada correctamente.")
    except sql.Error as e:
        print("Error al encriptar contrasenia:",str(e))

    cursor.close()
    conn.close()



def validar_informacion(nick, contraseña):
    longitud_minima = 8
    tiene_mayusculas = bool(re.search(r'[A-Z]', contraseña))
    tiene_minusculas = bool(re.search(r'[a-z]', contraseña))
    tiene_numeros = bool(re.search(r'\d', contraseña))
    tiene_caracteres_especiales = bool(re.search(r'[!@#$%^&*()-=_+[\]{}|;:",./<>?]', contraseña))

    if len(contraseña) < longitud_minima:
        print(f"La contraseña debe tener al menos {longitud_minima} caracteres.")
        return False

    if nick.lower() in contraseña.lower():
        print("La contraseña no puede contener el nick del usuario.")
        return False

    if not tiene_mayusculas:
        print("La contraseña debe contener al menos una letra mayúscula.")
        return False

    if not tiene_minusculas:
        print("La contraseña debe contener al menos una letra minúscula.")
        return False

    if not tiene_numeros:
        print("La contraseña debe contener al menos un número.")
        return False

    if not tiene_caracteres_especiales:
        print("La contraseña debe contener al menos un carácter especial (por ejemplo, !@#$%^&*).")
        return False

    return True


import smtplib
from email.mime.text import MIMEText

def enviar_correo_confirmacion(correo_destino, codigo_confirmacion):
    # Configuración del servidor SMTP
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587
    correo_emisor = "correo@unmsm.edu.pe"
    contraseña_emisor = "password"

    # Crear el objeto del mensaje de correo
    mensaje = MIMEText(f"Hola, para confirmar tu registro, utiliza el siguiente código: {codigo_confirmacion}")

    # Configurar los detalles del mensaje
    mensaje["Subject"] = "Confirmación de registro"
    mensaje["From"] = correo_emisor
    mensaje["To"] = correo_destino

    try:
        # Iniciar conexión con el servidor SMTP
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()

        # Autenticar con el servidor SMTP
        servidor.login(correo_emisor, contraseña_emisor)

        # Enviar el mensaje de correo
        servidor.send_message(mensaje)

        # Cerrar la conexión con el servidor SMTP
        servidor.quit()

        print("Correo de confirmación enviado correctamente.")
    except Exception as e:
        print("Error al enviar el correo de confirmación:", str(e))