lista=[7,6,5,4,3,2]

print(len(lista))
# agregar elementos al final de la lista append
lista.append(9)
print(lista)
lista.insert(1,8)
print(lista)

# quitar elementos de la lista
del lista[3]
print(lista)
lista.remove(4)
print(lista)
lista.pop()
print(lista)
#averigua info de elementos //posicion en donde se encuentran los elementos y pones el digito que quieres saber
#en que posicion se encuentra
print(lista.index(7))

lista[0]=1
print(lista)