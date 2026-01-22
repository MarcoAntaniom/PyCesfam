import textwrap
from models.usuarios import Usuario
from models.rol import Rol
from models.especialidad import Especialidad
from models.paciente import Paciente
from models.estado_paciente import Estado_paciente
from models.sexo import Sexo

# Menú del Administrador
def menu_admin(usuario):
    while True:
        print("\n" + "=" * 40)
        print(f"PANEL ADMINISTRADOR | Usuario: {usuario['nombre']} {usuario['apellido']}")
        print("="*40)
        print("1. Gestionar Usuarios")
        print("2. Gestionar pacientes")

        op = input("Ingrese una opción: ")

        if op == "1":
            u = Usuario()
            r = Rol()
            e = Especialidad()

            print("\n[!] Entrando al módulo de Gestión de Usuarios...")
            print("\n Ingrese una de las siguientes opciones: ")
            print("1. Agregar Usuario")
            print("2. Modificar Usuario")
            print("3. Deshabilitar Usuario")
            print("4. Consultar Usuarios")
            print("5. Agregar Especialidad a Médico")

            op_usuario = input("---> ")

            if op_usuario == "1":
                try:
                    u.rut = input("Ingresa el RUT del usuario: ")
                    u.nombre = input("Ingresa el nombre del usuario: ")
                    u.apellido = input("Ingresa el apellido del usuario: ")
                    u.password = input("Ingresa la contraseña del usuario: ")

                    roles = r.leer_roles()

                    for rol in roles:
                        print(f"ID: {rol[0]} | Nombre: {rol[1]}")

                    u.rol_id = int(input("Ingresa el rol del usuario: "))
                
                    if u.agregar_usuario():
                        print("Usuario agregado exitosamente.")
                
                except ValueError:
                    print("En el Rol solo se admiten valores númericos. Intentelo nuevamente")

            elif op_usuario == "2":
                usuarios = u.leer_usuarios()

                for usr in usuarios:
                    print(f"ID: {usr[0]} | RUT: {usr[1]} | Nombre: {usr[2]} | Apellido: {usr[3]} | Rol: {usr[4]} | Estado: {usr[5]}")

                rut = input("Ingresa el RUT del usuario que deseas modificar: ")

                u.obtener_por_rut(rut)

                if u.id:
                    # Todo input que se deje vacío se deja el valor que estaba almacenado en la Base de Datos.

                    print(f"\nEditando Usuario {u.nombre} {u.apellido}")
                    print("Presione 'Enter' para manter el valor actual.")

                    nuevo_nombre = input(f"Nombre actual {u.nombre}")
                    if nuevo_nombre.strip():
                        u.nombre = nuevo_nombre
                    
                    nuevo_apellido = input(f"Apellido actual {u.apellido}")
                    if nuevo_apellido.strip():
                        u.apellido = nuevo_apellido
                    
                    roles = r.leer_roles()

                    for rol in roles:
                        print(f"ID: {rol[0]} | Nombre: {rol[1]}")

                    nuevo_rol = input(f"Rol actual: {u.rol_id}")

                    if nuevo_rol.strip():
                        u.rol_id = int(nuevo_rol)

                    nueva_pass = input("Nueva contraseña (Dejar vacía para mantener): ")
                    
                    u.modificar_usuario(u.id, nueva_pass)

                else:
                    print("Usuario no encontrado.")

            elif op_usuario == "3":
                usuarios = u.leer_usuarios()

                for usr in usuarios:
                    print(f"ID: {usr[0]} | RUT: {usr[1]} | Nombre: {usr[2]} | Apellido: {usr[3]} | Rol: {usr[4]} | Estado: {usr[5]}")

                try:
                    id = int(input("Ingresa el ID del usuario que deseas deshabilitar: "))

                    u.deshabilitar_usuario(id)
                except ValueError:
                    print("Solo se aceptan números, no letras. Vuelva a intentarlo")
                finally:
                    print()

            elif op_usuario == "4":
                    usuarios = u.leer_usuarios()

                    for usr in usuarios:
                        print(f"ID: {usr[0]} | RUT: {usr[1]} | Nombre: {usr[2]} | Apellido: {usr[3]} | Rol: {usr[4]} | Estado: {usr[5]}")

            elif op_usuario == "5":
                medicos = u.leer_medicos()

                for medico in medicos:
                    print(f"ID: {medico[0]} | RUT: {medico[1]} | Nombre: {medico[2]} | Apellido: {medico[3]} | Rol: {medico[4]} | Estado: {medico[5]}")
                    
                try:
                    id_medico = int(input("Ingrese el ID del médico: "))

                    especialidades = e.leer_especialidades()

                    for especialidad in especialidades:
                        print(f"ID: {especialidad[0]} | Nombre: {especialidad[1]}")

                    id_especialidad = int(input("Ingrese el ID de la especialidad: "))

                    u.agregar_especialidad(id_medico, id_especialidad)

                except ValueError:
                    print("Solo se aceptan números, no letras. Vuelva a intentarlo")
                finally:
                    print()

        elif op == "2":
            p = Paciente()
            e_p = Estado_paciente()
            s = Sexo()

            print("\n[!] Entrando al módulo de Gestión de Pacientes...")
            print("\n Ingrese una de las siguientes opciones: ")
            print("1. Agregar Paciente")
            print("2. Modificar Paciente")
            print("3. Cambiar Estado Paciente")
            print("4. Consultar Pacientes")

            op_paciente = input("---> ")

            if op_paciente == "1":
                try:
                    p.rut = input("Ingrese el RUT del paciente: ")
                    p.nombres = input("Ingrese los nombres del paciente: ")
                    p.apellidos = input("Ingrese los apellidos del paciente: ")
                    p.direccion = input("Ingrese la dirección del paciente: ")
                    p.telefono = input("Ingrese el número de teléfono del paciente: ")
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (Ej: 1998-04-15): ")

                    sexos = s.leer_sexos()
                    print()
                    for sexo in sexos:
                        print(f"ID: {sexo[0]} | Nombre: {sexo[1]}")

                    p.sexo_id = int(input("Ingrese el ID del sexo del paciente: "))

                    if p.agregar_paciente(fecha_nacimiento):
                        print("Paciente agregado exitosamente.")
                
                except ValueError:
                    print("Error el Sexo solo recibe valores númericos. Intentelo nuevamente")
                finally:
                    print()

            elif op_paciente == "2":
                pacientes = p.leer_pacientes()

                for paciente in pacientes:
                    print(textwrap.dedent(f""" 
                        ID: {paciente[0]}
                        RUT: {paciente[1]}
                        Nombres: {paciente[2]}
                        Apellidos: {paciente[3]}
                        Dirección: {paciente[4]}
                        Teléfono: {paciente[5]}
                        Fecha Nacimiento: {paciente[6]}
                        Sexo: {paciente[7]}
                        Estado: {paciente[8]}
                        """))
