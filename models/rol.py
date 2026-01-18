from config.conexion import ConexionDB

class Rol:

    id: int
    nombre: str

    def leer_roles(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM roles"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los roles: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
