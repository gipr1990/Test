"""cadena  = (("hola","estop","es",1,))

print(type(cadena))

encontrado = cadena.index(1)

print (encontrado)

print(dir(cadena))"""

"""
claves = diccionario.keys()

print (claves)
"""

diccionario = {
    "nombre" : "Gonzalo", 
    "Apellido" : "Ibarra",
    "DNI" : "uruguay"

}
getter = diccionario.get("nombre")
print (getter)

"""borrar = diccionario.clear()

print (borrar)
"""

diccionario_iterable = diccionario.items()

print (diccionario_iterable)