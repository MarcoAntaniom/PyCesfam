from datetime import datetime
from config.conexion import ConexionDB

class Cita_medica:

    id: int
    id_medico: int
    id_paciente: int
    estado_id: int
    fecha_hora: str

    def leer_por_fecha(self, fecha):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM citas_medicas WHERE fecha = %s"
            datos = [fecha]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer las citas de la fecha buscada: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def leer_por_medico(self, id_medico):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM citas_medicas WHERE id_medico = %s"
            datos = [id_medico]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer las citas del médico buscado: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
    
    def agregar_cita(self, id_medico, id_paciente, fecha_hora):
        c = None
        try:
            # Obtiene la fecha y hora en string, y la convierte a datetime.
            fecha_hora_recibida = fecha_hora
            fecha_hora_valida = datetime.strptime(fecha_hora_recibida, "%Y-%m-%d %H:%M")
            fecha_hora_bd = fecha_hora_valida.strftime("%Y-%m-%d %H:%M")

            c = ConexionDB()
            sql = """INSERT INTO citas_medicas (id_medico, id_paciente, fecha_hora, estado_cita)
                        VALUES (%s, %s, %s, 1)"""
            datos = [id_medico, id_paciente, fecha_hora_bd]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al agregar la cita: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
