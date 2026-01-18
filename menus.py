from models.usuarios import Usuario

# Menú del Administrador
def menu_admin(usuario):
    while True:
        print("\n" + "=" * 40)
        print(f"PANEL ADMINISTRADOR | Usuario: {usuario['nombre']} {usuario['apellido']}")
        print("="*40)
        print("1. Gestionar Usuarios")

        op = int(input("Ingrese una opción: "))

        if op == 1:
            u = Usuario()
            print("\n[!] Entrando al módulo de Gestión de Usuarios...")
            print("\n Ingrese una de las siguientes opciones: ")
            print("1. Agregar Usuario")
            print("2. Modificar Usuario")
            print("3. Deshabilitar Usuario")
            print("4 Consultar Usuarios")

            op_usuarios = int(input("---> "))

            if op_usuarios == 1:
                u.rut = input("Ingresa el RUT del usuario: ")
                u.nombre = input("Ingresa el nombre del usuario: ")
                u.apellido = input("Ingresa el apellido del usuario: ")
                u.password = input("Ingresa la contraseña del usuario: ")
                u.rol_id = input("Ingresa el rol del usuario: ")
                u.agregar_usuario()
                print("Usuario agregado exitosamente")
