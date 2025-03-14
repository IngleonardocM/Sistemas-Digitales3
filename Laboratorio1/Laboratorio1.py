
def mostrar_menu():
    print("\n=== Menú del Directorio Telefónico ===")
    print("1. Agregar un nuevo contacto")
    print("2. Buscar un contacto por teléfono")
    print("3. Eliminar un contacto")
    print("4. Salir")


def agregar_registro(base_datos):
    print("\n--- Agregar un nuevo contacto ---")
    persona = {}
    persona["Nombre y Apellido"] = input("Ingrese el nombre y apellido: ")
    persona["Teléfono celular"] = input("Ingrese el número de teléfono: ")
    persona["Cumpleaños"] = input("Ingrese la fecha de cumpleaños: ")
    persona["Correo"] = input("Ingrese el correo electrónico: ")
    base_datos.append(persona)
    print("Contacto agregado exitosamente.\n")


def buscar_por_telefono(base_datos):
    print("\n--- Buscar un contacto ---")
    telefono = input("Ingrese el número de teléfono a buscar: ")
    encontrado = False
    for persona in base_datos:
        if persona["Teléfono celular"] == telefono:
            print("Contacto encontrado:")
            print(f"Nombre: {persona['Nombre y Apellido']}")
            print(f"Teléfono: {persona['Teléfono celular']}")
            print(f"Cumpleaños: {persona['Cumpleaños']}")
            print(f"Correo: {persona['Correo']}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún contacto con ese número.\n")


def borrar_registro(base_datos):
    print("\n--- Eliminar un contacto ---")
    telefono = input("Ingrese el número de teléfono del contacto a eliminar: ")
    for persona in base_datos:
        if persona["Teléfono celular"] == telefono:
            base_datos.remove(persona)
            print("Contacto eliminado correctamente.\n")
            return
    print("No se encontró ningún contacto con ese número.\n")


# Lista para almacenar registros
base_datos = []

print("¡Bienvenido al directorio telefónico!")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregar_registro(base_datos)
    elif opcion == "2":
        buscar_por_telefono(base_datos)
    elif opcion == "3":
        borrar_registro(base_datos)
    elif opcion == "4":
        print("Gracias por usar el directorio. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.\n")






    