import sqlite3 as sql
import os

def conectar_bd():  
    # Obtener la ruta absoluta al archivo de base de datos
    current_directory = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_directory, "..", "serializar", "SGDS-VABD01.db")

    # Establecer conexión con la base de datos
    conn = sql.connect(db_path)
    return conn

def buscar_usuario(user, password):
    conn = sql.connect("serializar/SGDS-VABD01.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM Credencial WHERE user = ? AND password = ?",
            (user, password),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioDatos(nombre):
    conn = sql.connect("serializar/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT dni, telefono, direccion, fechaNacimiento FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioDonaciones(nombre):
    conn = sql.connect("serializar/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT ultimaDonacion FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def usuarioBeneficios(nombre):
    conn = sql.connect("serializar/SGDS-VABD01.db")    
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT beneficioActivo FROM Paciente WHERE nombre = ?",
            (nombre,),
        )

        usuario = cursor.fetchone()

        return usuario
    except sql.Error as e:
        print("Error al buscar usuario:", str(e))

    return None

def registrar_credencial(credencial):
    # Obtener la ruta absoluta del directorio actual
    current_dir = os.path.abspath("")
    # Construir la ruta absoluta del archivo de la base de datos
    db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
    # Establecer la conexión a la base de datos
    conn = sql.connect(db_path)
    cursor = conn.cursor()
    instruction = "INSERT INTO Credencial VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(instruction, (
        credencial.get_idCredencial(),
        credencial.get_fechaDeCreacion(),
        credencial.get_fechaDeExpiracion(),
        credencial.get_estado(),
        credencial.get_tipoDeUsuario(),
        credencial.get_username(),
        credencial.get_password()
    ))
    conn.commit()
    conn.close()

def registrar_donante(self, donante):
    # Obtener la ruta absoluta del directorio actual
    current_dir = os.path.abspath("")
    # Construir la ruta absoluta del archivo de la base de datos
    db_path = os.path.join(current_dir, "..", "serializar", "SGDS-VABD01.db")
    # Establecer la conexión a la base de datos
    conn = sql.connect(db_path)
    cursor = conn.cursor()

    try:
        instruction = "INSERT INTO Donante VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(
            instruction,
            (
                donante.get_id_donante(),
                donante.get_nombre(),
                donante.get_fecha_nacimiento(),
                donante.get_dni(),
                donante.get_telefono(),
                donante.get_direccion(),
                donante.get_beneficio_activo(),
                donante.get_grupo_sanguineo(),
                donante.get_rh(),
                donante.get_ultima_donacion(),
                donante.get_id_hospitalUltimo(),
            ),
        )

        conn.commit()
        print("Donante registrado exitosamente.")
    except sql.Error as e:
        print("Error al registrar el donante:", str(e))

    conn.close()