from config.conexion import ConexionDB

class Estado_paciente:

    id: int
    nombre: str

    def leer_estados(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM estado_paciente"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los estados de los pacientes: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
