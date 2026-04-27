"""
haz un programa en python que te muestre un menú con la primera opción
que te permita crear una persona con nombre y DNI y la agregué a una lista de personas.
El menú tendra una segunda opcion donde mostrará todas las personas.
El menú tendra una tercera opcion que perdira un DNI y eliminará a la persona con ese DNI
"""

class Persona:
    def __init__(self, dni=0, nombre="" ):
        self.nombre= nombre
        self.dni = dni
    def __str__(self):
        return f"dni: {self.dni} {self.nombre}"
    

lista=[]
opc=0
while opc!=9:

    print("Menú")
    print("1. Agregar persona")
    print("2. Mostrar personas")
    print("3. Eliminar por DNI")
    opc = int(input("Elije tu opcion "))
    if opc==1:
        print("nombre de la persona")
        nom = input()
        print("DNI de la persona")
        dni = input()
        nuevo =Persona(dni, nom)
        lista.append(nuevo)
    elif opc==2:
        for p in lista:
            print(p)
    elif opc==3:
        dniB=input("ingres dni a borrar:\n")
        for idx, p in enumerate(lista):
            if p.dni == dniB:
                del lista[idx]
                break
    else :
        break