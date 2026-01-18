from datetime import datetime
from config.conexion import ConexionDB

class Paciente:

    id: int
    rut: str
    nombres: str
    apellidos: str
    direccion: str
    telefono: str
    fecha_nacimiento: str
    sexo_id: int
    estado_id: int

    def leer_pacientes(self):
        c = None
        try:
            c = ConexionDB()
            sql = """SELECT
                        p.id,
                        p.rut,
                        p.nombres,
                        p.apellidos,
                        p.direccion,
                        p.telefono,
                        p.fecha_nacimiento,
                        s.nombre AS sexo,
                        e.nombre AS estado_nombre
                    FROM pacientes p
                    INNER JOIN sexo s ON s.id = p.sexo_id
                    INNER JOIN estado_paciente e ON e.id = p.estado_id
                    """
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer usuarios: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def agregar_paciente(self, fecha_nacimiento):
        c = None
        try:
            # Convierte la fecha de string a date.
            fecha_recibida = fecha_nacimiento
            fecha_valida = datetime.strptime(fecha_recibida, "%Y-%m-%d")
            fecha_bd = fecha_valida.strftime("%Y-%m-%d")

            c = ConexionDB()
            sql = """INSERT INTO pacientes (rut, nombres, apellidos, direccion,
                        telefono, fecha_nacimiento, sexo_id, estado_id)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"""
            datos = [self.rut, self.nombres, self.apellidos, self.direccion, self.telefono,
                     fecha_bd, self.sexo_id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al agregar el paciente: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def modificar_paciente(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = """UPDATE pacientes SET nombres = %s, apellidos = %s, direccion = %s, 
                        telefono = %s WHERE id = %s"""
            datos = [self.nombres, self.apellidos, self.direccion, self.telefono, id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al modificar el paciente: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def actualizar_estado_paciente(self, estado_id, id):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE pacientes SET estado_id = %s WHERE id = %s"
            datos = [estado_id, id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al cambiar el estado del paciente: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def obtener_por_rut(self, rut):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM pacientes WHERE rut = %s"
            rut_recibido = [rut]
            c.cursor.execute(sql, rut_recibido)
            fila = c.cursor.fetchone()

            if fila:
                self.id = fila[0]
                self.rut = fila[1]
                self.nombres = fila[2]
                self.apellidos = fila[3]
                self.direccion = fila[4]
                self.telefono = fila[5]
                self.fecha_nacimiento = fila[6]
                self.sexo_id = fila[7]
                self.estado_id = fila[8]
        except Exception as e:
            print(f"Error al obtener los datos del paciente: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
            