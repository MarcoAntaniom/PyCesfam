from config.conexion import ConexionDB

class Estado_usuario:

    id: int
    nombre: str

    def leer_estados(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM estado_usuario"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los estados de los usuarios: {e}")
        finally:
            c.cursor.close()
            c.conexion.close()
