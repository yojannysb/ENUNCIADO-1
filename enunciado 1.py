class Animal:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace un sonido genérico.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Muuuu!")

# Creación de la lista con un objeto de cada tipo
animales = [
    Perro("Lazzy", 3),
    Gato("Michi", 2),
    Vaca("Candy", 5)
]

# Recorrido de la lista llamando al método hacer_sonido()
for animal in animales:
    animal.hacer_sonido()
    