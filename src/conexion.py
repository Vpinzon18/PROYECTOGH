import pyodbc
from getpass import getpass
import hashlib

# Configura la conexión a la base de datos
server = '10.20.110.77'
database = 'GHPROYECTO'
username = 'ccca'
password = 'ccca'  
# Asegúrate de almacenar y gestionar contraseñas de manera segura

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()

    # Realiza una consulta SQL para seleccionar todos los registros de la tabla "Usuario"
    consulta = "SELECT * FROM Usuario"

    # Ejecuta la consulta
    cursor.execute(consulta)

    # Recupera los resultados
    resultados = cursor.fetchall()

    # Imprime los resultados
    for fila in resultados:
        print(fila)

except Exception as e:
    print("Ocurrió un error:", str(e))
finally:
    # Cierra la conexión a la base de datos
    conn.close()
