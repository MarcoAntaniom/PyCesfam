import getpass
import sys
from models.usuarios import Usuario
from menus import *

def main():
    u = Usuario()
    print("\n" + "-" * 56)
    print("Bienvenido al Sistema de Control de Pacientes (PyCesfam)")
    print("-" * 56)

    rut = input("Ingrese RUT (0 'salir' para cerrar): ")
    
    if rut.lower() == "salir":
        print("Saliendo del sistema...")
        sys.exit()
    
    password = getpass.getpass("Ingrese contraseña: ")

    datos_usuario = u.login(rut, password)

    if datos_usuario:
        rol = datos_usuario["rol_id"]

        # Redirección en base al rol del usuario.
        if rol == 1:
            # Administrador
            menu_admin(datos_usuario)
        elif rol == 2:
            # Médico
            pass
        elif rol == 3:
            # SOME
            pass
        elif rol == 4:
            # Farmacéutico
            pass
        else:
            print("Error el rol no tiene un menú asignado.")


if __name__ == "__main__":
    main()