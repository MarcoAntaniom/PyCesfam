from config.conexion import ConexionDB

class Detalle_cita:

    id: int
    id_cita: int
    motivo_cita: str
    observaciones: str
    indicaciones: str

    def registrar_atencion(self):
        c = None
        try:
            c = ConexionDB()
            sql = """INSERT INTO detalle_cita (id_cita, motivo_cita, observaciones, indicaciones)
                        VALUES (%s, %s, %s, %s)"""
            datos = [self.id_cita, self.motivo_cita, self.observaciones, self.indicaciones]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al registrar la atención: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def leer_detalle_por_cita(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM detalle_cita WHERE id_cita = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los datos de esa cita: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def modificar_detalle(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE detalle_cita SET motivo_cita = %s, observaciones = %s, indicaciones = %s WHERE id_cita = %s"
            datos = [self.motivo_cita, self.observaciones, self.indicaciones, id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al modificar el detalle: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def obtener_detalle_id(self, id):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM detalle_cita WHERE id_cita = %s"
            datos = [id]
            c.cursor.execute(sql, datos)
            fila = c.cursor.fetchone()

            if fila:
                self.id = fila[0]
                self.id_cita = fila[1]
                self.motivo_cita = fila[2]
                self.observaciones = fila[3]
                self.indicaciones = fila[4]

        except Exception as e:
            print(f"Error al obtener los datos de esa cita: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
