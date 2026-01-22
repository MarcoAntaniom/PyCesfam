from config.conexion import ConexionDB

class Medicamento:

    id: int
    nombre: str
    concentracion: str
    forma_farmaceutica: int
    stock: int

    def leer_medicamentos(self):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM medicamento"
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los medicamentos: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def buscar_por_nombre(self, nombre):
        c = None
        try:
            c = ConexionDB()
            sql = "SELECT * FROM medicamento WHERE nombre LIKE %s"

            patron = f"%{nombre}%"

            datos = [patron]
            c.cursor.execute(sql, datos)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al buscar el medicamento: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def actualizar_stock(self, id, cant):
        c = None
        try:
            c = ConexionDB()
            sql = "UPDATE medicamento SET stock = stock - %s WHERE id = %s"
            datos = [cant, id]
            c.cursor.execute(sql, datos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al actualizar el stock del medicamento: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
