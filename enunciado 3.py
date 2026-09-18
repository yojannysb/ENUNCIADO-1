class Empleado:
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        return self.salario_base

class Gerente(Empleado):
    def __init__(self, nombre: str, salario_base: float):
        super().__init__(nombre, salario_base)

    def calcular_salario(self) -> float:
        # Salario base + bono del 30%
        return self.salario_base * 1.30

class Vendedor(Empleado):
    def __init__(self, nombre: str, salario_base: float, ventas: float):
        super().__init__(nombre, salario_base)
        self.ventas = ventas

    def calcular_salario(self) -> float:
        # Salario base + comisión del 10% sobre las ventas
        return self.salario_base + (self.ventas * 0.10)

# Lista de empleados
nomina = [
    Gerente(nombre="Yojannys Barrios", salario_base=450),
    Vendedor(nombre="Angel Benavides", salario_base=240, ventas=80),
    Empleado(nombre="Sophia Benavides", salario_base=180),
    Vendedor(nombre="Ethan Barrios", salario_base=120, ventas=40)
]

for empleado in nomina:
    puesto = empleado.__class__.__name__
    print(f"{puesto}: {empleado.nombre} tiene un salario total de: ${empleado.calcular_salario():.2f}")
    