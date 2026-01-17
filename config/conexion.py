import mysql.connector

class ConexionDB:

    def __init__(self):
        try:
            config = {
                "user": "marco_antoniom",
                "password": "RiSFs0r76bU4dkWv",
                "host": "localhost",
                "db": "py_cesfam",
                "port": 3306
            }

            self.conexion = mysql.connector.connect(**config)
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f"Error en la base de datos: {e}")
