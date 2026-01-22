from config.conexion import ConexionDB

class Estado_entrega:

    id: int
    nombre: str

    def leer_estados(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM estado_entrega"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los estados de entrega: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
