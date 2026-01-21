from config.conexion import ConexionDB

class Sexo:

    id: int
    nombre: str

    def leer_sexos(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM sexo"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los sexos: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
