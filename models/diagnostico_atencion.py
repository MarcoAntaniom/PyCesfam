from config.conexion import ConexionDB

class Diagnostico_atencion:

    id: int
    detalle_cita_id: int
    diagnostico_id: int
    tipo_diagnostico: int
    observaciones: str

    def agregar_diagnostico_atencion(self):
        c = None
        try:
            c = ConexionDB()
            sql = """INSERT INTO diagnosticos_atencion (detalle_cita_id, diagnostico_id,
                        tipo_diagnostico, observaciones)
                        VALUES (%s, %s, %s, %s)"""
            datos = [self.detalle_cita_id, self.diagnostico_id, self.tipo_diagnostico, self.observaciones]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al ingresar el diagnóstico de la atención: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def obtener_diagnostico_por_detalle(self, id_detalle):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM diagnosticos_atencion WHERE detalle_cita_id = %s"
            datos = [id_detalle]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener el diagnóstico del detalle buscado: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
