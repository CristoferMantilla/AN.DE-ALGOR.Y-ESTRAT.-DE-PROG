class Perro:
    def __init__(self, nombre=""):
        self.nombre= nombre
        self.edad = 1
    def __str__(self):
        return f"Soy {self.nombre} y tengo {self.edad} años"
    def ladra(self):
        print(f"Guau, tengo {self.edad}")
    
fido =Perro("Fido")
print(fido)