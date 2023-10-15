"""Escriba una clase de Python llamada Rectangle construida por una longitud y anchura y un método que calculará el área de un rectángulo."""

class Rectangle:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def calcular_area(self):
        """
        Calcula el área del rectángulo.
        """
        area = self.longitud * self.anchura
        return area


while True:
    try:
        longitud = float(input("Ingresa la longitud del rectángulo: "))
        anchura = float(input("Ingresa la anchura del rectángulo: "))
        break
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

mi_rectangulo = Rectangle(longitud, anchura)
area = mi_rectangulo.calcular_area()
print(f"El área del rectángulo con longitud {longitud} y anchura {anchura} es: {area}")