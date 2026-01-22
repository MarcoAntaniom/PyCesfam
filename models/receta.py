import datetime
from config.conexion import ConexionDB

class Receta:

    id: int
    detalle_cita_id: int
    medicamento_id: int
    estado_entrega_id: int
    fecha_entrega: str
    cant_solicitada: int
    duracion: str
    frecuencia: str
    dosis: str
    estado_entrega: int

    def leer_recetas(self):
        c = None
        try:
            c = ConexionDB()
            sql = """SELECT 
                        r.id,
                        p.nombres AS nombre_paciente,
                        m.nombre AS nombre_medicamento,
                        r.fecha_entrega,
                        r.cant_solicitada,
                        r.duracion,
                        r.frecuencia,
                        r.dosis,
                        e.nombre AS nombre_estado
                    FROM recetas r
                    INNER JOIN detalle_cita d ON d.id = r.detalle_cita_id
                    INNER JOIN citas_medicas c ON c.id = d.id_cita
                    INNER JOIN pacientes p ON p.id = c.id_paciente
                    INNER JOIN medicamento m ON m.id = r.medicamento_id
                    INNER JOIN estado_entrega e ON e.id = r.estado_entrega
                    """
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer las recetas: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
    
    def leer_por_paciente(self, id_paciente):
        c = None
        try:
            c = ConexionDB()
            sql = """SELECT 
                        r.id,
                        p.nombres AS nombre_paciente,
                        m.nombre AS nombre_medicamento,
                        r.fecha_entrega,
                        r.cant_solicitada,
                        r.duracion,
                        r.frecuencia,
                        r.dosis,
                        e.nombre AS nombre_estado
                    FROM recetas r
                    INNER JOIN detalle_cita d ON d.id = r.detalle_cita_id
                    INNER JOIN citas_medicas c ON c.id = d.id_cita
                    INNER JOIN pacientes p ON p.id = c.id_paciente
                    INNER JOIN medicamento m ON m.id = r.medicamento_id
                    INNER JOIN estado_entrega e ON e.id = r.estado_entrega
                    WHERE c.id_paciente = %s
                    """
            datos = [id_paciente]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer las recetas de ese paciente: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
    
    def agregar_receta(self):
        c = None
        try:
            fecha_entrega = datetime.datetime.now()
            c = ConexionDB()
            sql = """INSERT INTO recetas (detalle_cita_id, medicamento_id, fecha_entrega,
                        cant_solicitada, duracion, frecuencia, dosis, estado_entrega)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 1)"""
            datos = [self.detalle_cita_id, self.medicamento_id, fecha_entrega,
                     self.cant_solicitada, self.duracion, self.frecuencia, self.dosis]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al agregar la receta: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def marcar_entregado(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE recetas SET estado_entrega = 2 WHERE id = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al marcar la receta como entregada: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def marcar_rechazado(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE recetas SET estado_entrega = 3 WHERE id = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al marcar la receta como rechazada: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def marcar_vencida(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE recetas SET estado_entrega = 5 WHERE id = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollbacK()
            print(f"Error al marcar como vencida la receta: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def obtener_por_id(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM recetas WHERE id = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            fila = c.cursor.fetchone()

            if fila:

                self.id = fila[0]
                self.detalle_cita_id = fila[1]
                self.medicamento_id = fila[2]
                self.fecha_entrega = fila[3]
                self.cant_solicitada = fila[4]
                self.duracion = fila[5]
                self.frecuencia = fila[6]
                self.dosis = fila[7]
                self.estado_entrega = fila[8]

        except Exception as e:
            print(f"Error al obtener los datos de la receta: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
