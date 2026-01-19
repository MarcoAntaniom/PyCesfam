from config.conexion import ConexionDB

class Especialidad:

    id: int
    nombre: str

    def leer_especialidades(self):
        c = ConexionDB()
        try:
            c = ConexionDB()
            sql = "SELECT * FROM especialidad"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer las especialidades: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
