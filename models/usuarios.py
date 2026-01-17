import bcrypt
from config.conexion import ConexionDB

class Usuario:

    id: int
    rut: str
    nombre: str
    apellido: str
    password: str
    rol_id: int
    estado_id: int

    def leer_usuarios(self):
        c = None
        try:
            c = ConexionDB()
            sql = """SELECT
                        u.id,
                        u.rut,
                        u.nombre,
                        u.apellido,
                        r.nombre,
                        e.nombre
                    FROM usuarios u
                    INNER JOIN roles r ON r.id = u.rol_id
                    INNER JOIN estado_usuario e ON e.id = u.estado_id
                """
            c.cursor.execute(sql)
            return c.cursor.fetchall()
        except Exception as e:
            print(f"Error al leer los usuarios: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def agregar_usuario(self):
        c = None
        try:
            c = ConexionDB()

            password = self.password
            password_code = password.encode("utf-8")
            password_hash = bcrypt.hashpw(password_code, bcrypt.gensalt())
            password_hash = password_hash.decode("utf-8")

            sql = """INSERT INTO usuarios (rut, nombre, apellido, password, rol_id, estado_id)
                        VALUES (%s, %s, %s, %s, %s, 1)"""
            datos_recibidos = [self.rut, self.nombre, self.apellido, password_hash, self.rol_id]
            c.cursor.execute(sql, datos_recibidos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al insertar el usuario: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def modificar_usuario(self, id, password_ingresada = None):
        c = None
        try:
            c = ConexionDB()

            password_hash = None

            if password_ingresada and password_ingresada.strip() != "":
                password_nueva = password_ingresada
                password_code = password_nueva.encode("utf-8")
                password_hash = bcrypt.hashpw(password_code, bcrypt.gensalt())
                password_hash = password_hash.decode("utf-8")

            sql = """UPDATE usuarios SET nombre = %s, apellido = %s, password = COALESCE(%s, password),
                        rol_id = %s WHERE id = %s"""
            datos_recibidos = [self.nombre, self.apellido, password_hash, self.rol_id, id]
            c.cursor.execute(sql, datos_recibidos)
            c.conexion.commit()
        except Exception as e:
            c.conexion.rollback()
            print(f"Error al modificar el usuario: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()

    def obtener_por_rut(self, rut):
        c = None
        try:
            c = ConexionDB()
            sql = """SELECT * FROM usuarios WHERE rut = %s"""
            rut_recibido = [rut]
            c.cursor.execute(sql, rut_recibido)
            fila = c.cursor.fetchone()
            
            if fila:
                self.id = fila[0]
                self.rut = fila[1]
                self.nombre = fila[2]
                self.apellido = fila[3]
                self.password = ""
                self.rol_id = fila[5]
                self.estado_id = fila[6]
        except Exception as e:
            print(f"Error al obtener los datos del usuario: {e}")
        finally:
            if c is not None:
                c.cursor.close()
                c.conexion.close()
