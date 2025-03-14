# LABORATORIO I
## Integrantes
[David Leonardo Castaño Madrigal](https://github.com/IngleonardocM) 
 
 ## Documentación
En el archivo [Laboratorio1.py](/Laboratorio1/Laboratorio1.py) Es un directorio telefónico que permite al usuario agregar, buscar y eliminar contactos de una base de datos temporal mientras el programa está en ejecución.
Cuando el usuario ejecuta el programa, se muestra un mensaje de bienvenida y se entra en un bucle donde se muestra un menú con las siguientes opciones:

Agregar un nuevo contacto
Buscar un contacto por número de teléfono
Eliminar un contacto
Salir del programa
El programa sigue ejecutándose hasta que el usuario elija la opción de salir.

Si el usuario elige agregar un contacto, el programa le pedirá:

Nombre y Apellido
Número de Teléfono
Fecha de Cumpleaños
Correo Electrónico

Estos datos se almacenan en un diccionario, que es una estructura de datos que permite guardar información en formato clave-valor (por ejemplo, "Teléfono celular": "3124565345").
Este diccionario con la información del contacto se añade a una lista, que funciona como la base de datos del programa.
Ejemplo: Si el usuario ingresa los datos de "leo", el programa guarda la información en la lista como un nuevo contacto.

Si el usuario quiere buscar un contacto, el programa le pedirá que ingrese un número de teléfono, Luego recorrerá la lista donde están almacenados los contactos, si encuentra un contacto con ese número, mostrará su información en pantalla, si el número no existe en la base de datos, mostrará un mensaje de error.
Ejemplo: Si el usuario busca el número 3212333333, el programa mostrará el nombre, cumpleaños y correo de la persona asociada a ese número.

Si el usuario quiere eliminar un contacto, el programa le pedirá el número de teléfono de la persona a eliminar,recorrerá la lista de contactos hasta encontrar el número ingresado, si el número existe eliminará el contacto de la lista y mostrará un mensaje de confirmación, si el número no existe informará al usuario que no encontró el contacto.
Ejemplo: Si el usuario elimina el número 3212333333, el contacto con ese número desaparecerá de la lista.

Si el usuario elige la opción de salir, el programa mostrará un mensaje de despedida y cierra el programa.

[IMAGEN1](/Laboratorio1/IMAGENES/LABPARTE1.png)
[IMAGEN2](/Laboratorio1/IMAGENES/LABPARTE2.png)
