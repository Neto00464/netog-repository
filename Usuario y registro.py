print("Bienvenido/a")
usuarios = {
    "admin":(
        "admin",
        "admin@ufide.com",
        "12345"
        )
    }

opcion = "0"

while (opcion != "3"):
    print("1. Ingresar")
    print("2. Crear usuario")
    print("3. Salir")
    opcion = input("---Ingrese una opcion: ")

    if (opcion == "1"):
        while True:
            nombreUsuario = input("Escriba su usuario: ")
            pin = input("Escriba su contraseña: ")

            if nombreUsuario in usuarios and pin == usuarios[nombreUsuario][2]:
                print("Bienvenido/a")

            else:
                print("Usuario incorrecto")


    elif (opcion == "2"):
        usuarios[input("Ingrese nombre de usuario: ")] = input("Ingrese nombre: "), input("Ingrese correo: "), input("Ingrese Pin: ")
        print("***Usuario registrado con exito***")

    elif (opcion == "3"):
        print("---Saliendo de SmartHouse App")


    else:
        print("Opcion no existe")




