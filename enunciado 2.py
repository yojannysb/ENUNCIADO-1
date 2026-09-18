import math

class Figura:
    def area(self) -> float:
        return 0.0

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2

# Creación de la lista con las figuras geométricas
figuras = [
    Rectangulo(base=10, altura=5),
    Circulo(radio=3),
    Triangulo(base=6, altura=4)
]

# Recorrido de la lista y visualización de las áreas
for figura in figuras:
    nombre_clase = figura.__class__.__name__
    print(f"El área del {nombre_clase} es: {figura.area():.2f}")
    