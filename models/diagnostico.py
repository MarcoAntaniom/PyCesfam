from config.conexion import ConexionDB

class Diagnostico:

    id: int
    nombre: str

    def buscar_por_nombre(self, nombre):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM diagnostico WHERE nombre LIKE %s"

            patron = f"%{nombre}%"

            datos = [patron]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer el diagnóstico buscado: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
