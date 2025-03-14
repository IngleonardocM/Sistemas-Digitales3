

# Definimos la clase Contacto
class Contacto:
    def __init__(self, nombre, telefono, cumpleanos, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.cumpleanos = cumpleanos
        self.correo = correo

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Cumpleaños: {self.cumpleanos}, Correo: {self.correo}"

# Lista para almacenar la base de datos de contactos
directorio = []

# Lista de textos a mostrar durante la ejecución del programa
mensajes = [
    "Bienvenido al directorio telefónico",
    "Digite el Nombre y Apellido: ",
    "Digite el Teléfono Celular: ",
    "Digite el Cumpleaños (DD/MM/AAAA): ",
    "Digite el Correo Electrónico: ",
    "1. Agregar un nuevo registro",
    "2. Buscar una persona por teléfono celular",
    "3. Borrar un registro",
    "4. Salir de la aplicación",
    "Opción no válida. Intente de nuevo.",
    "Gracias por usar el directorio telefónico"
]

def agregar_contacto():
    nombre = input(mensajes[1])
    telefono = input(mensajes[2])
    cumpleanos = input(mensajes[3])
    correo = input(mensajes[4])
    nuevo_contacto = Contacto(nombre, telefono, cumpleanos, correo)
    directorio.append(nuevo_contacto)
    print("Contacto agregado exitosamente.\n")

def buscar_contacto():
    telefono = input("Ingrese el número de teléfono a buscar: ")
    for contacto in directorio:
        if contacto.telefono == telefono:
            print("Contacto encontrado:", contacto.mostrar_info())
            return
    print("Contacto no encontrado.\n")

def borrar_contacto():
    telefono = input("Ingrese el número de teléfono a borrar: ")
    for contacto in directorio:
        if contacto.telefono == telefono:
            directorio.remove(contacto)
            print("Contacto eliminado correctamente.\n")
            return
    print("Contacto no encontrado.\n")

def mostrar_menu():
    print(mensajes[0])
    while True:
        print("\n" + "\n".join(mensajes[5:9]))
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            borrar_contacto()
        elif opcion == "4":
            print(mensajes[10])
            break
        else:
            print(mensajes[9])

# Ejecutar el programa
mostrar_menu()






    