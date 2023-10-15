"""Escriba una clase de Python llamada Circle construida por un radio y dos métodos que calcularán el área y el perímetro de un círculo."""

import math

class Circle:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """
        Calcula el área del círculo.
        """
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        """
        Calcula el perímetro del círculo.
        """
        perimetro = 2 * math.pi * self.radio
        return perimetro


while True:
    try:
        radio = float(input("Ingresa el radio del círculo: "))
        break
    except ValueError:
        print("Por favor, ingresa un valor numérico válido.")

mi_circulo = Circle(radio)
area = mi_circulo.calcular_area()
perimetro = mi_circulo.calcular_perimetro()
print(f"El área del círculo con radio {radio} es: {area}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro}")

