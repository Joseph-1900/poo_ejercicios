"""Escriba una clase que represente un vehículo con métodos y atributos. 
Dentro atributos cree uno llamado “placa” y en los métodos cree uno que permita 
determinar de acuerdo con el día, si el vehículo tiene restricción por pico y placa o no, en la ciudad de Bogotá."""

class Vehiculo:
    def __init__(self, placa):
        self.placa = placa

    def tiene_restriccion_pico_placa(self, dia):
        """
        Determina si el vehículo tiene restricción por pico y placa en Bogotá en base al día.
        :param dia: El día de la semana en formato de número (1 para lunes, 2 para martes, etc.).
        """
        ultimo_digito = int(self.placa[-1])
        if dia in [1, 2, 3, 4, 5]:  
            if dia == 1:  
                return ultimo_digito in [1, 2]
            elif dia == 2:  
                return ultimo_digito in [3, 4]
            elif dia == 3:  
                return ultimo_digito in [5, 6]
            elif dia == 4:  
                return ultimo_digito in [7, 8]
            elif dia == 5:  
                return ultimo_digito in [9, 0]
        else:
            return False  


mi_vehiculo = Vehiculo("ABC123")
while True:
    try:
        dia_actual = int(input("Ingresa el número del día (1 para lunes, 2 para martes, etc.): "))
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

tiene_restriccion = mi_vehiculo.tiene_restriccion_pico_placa(dia_actual)
if tiene_restriccion:
    print("El vehículo tiene restricción por pico y placa hoy en Bogotá.")
else:
    print("El vehículo no tiene restricción por pico y placa hoy en Bogotá.")

