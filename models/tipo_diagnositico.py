from config.conexion import ConexionDB

class Tipo_diagnostico:

    id: int
    nombre: str

    def leer_diagnosticos(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM tipo_diagnostico"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los tipos de diagnóstico: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
