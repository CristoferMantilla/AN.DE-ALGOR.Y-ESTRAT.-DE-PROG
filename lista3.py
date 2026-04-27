#lista intensional haskell
lista = [ x*2 for x in range(1,10+1) if x*2 >= 12]
print (lista)
# a partir de los numeros del uno al cien, muestren solo los multiplos de 3
listas = [ x for x in range(1,100+1)if x % 3==0]
print (listas)