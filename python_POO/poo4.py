"""Escriba una clase de Python para implementar pow(x, n)."""

class PowerCalculator:
    def pow(self, x, n):
        """
        Calcula la potencia de un número dado.
        :param x: La base.
        :param n: El exponente.
        :return: El resultado de x elevado a la n.
        """
        return x ** n


mi_calculadora = PowerCalculator()
while True:
    try:
        base = float(input("Ingresa la base (x): "))
        exponente = int(input("Ingresa el exponente (n): "))
        break
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

resultado = mi_calculadora.pow(base, exponente)
print(f"{base} elevado a la {exponente} es igual a: {resultado}")
