"""Escriba un clase padre llamada Ave que herede a clases hijas con tipos de aves"""

class Ave:
    def __init__(self, nombre, habitat):
        self.nombre = nombre
        self.habitat = habitat

    def descripcion(self):
        """
        Imprime una descripción de la ave.
        """
        print(f"Soy un {self.nombre} y vivo en {self.habitat}.")

class Pato(Ave):
    def __init__(self, nombre, habitat, color_plumaje):
        super().__init__(nombre, habitat)
        self.color_plumaje = color_plumaje

    def descripcion(self):
        """
        Imprime una descripción específica del pato.
        """
        print(f"Soy un {self.nombre} y vivo en {self.habitat}. Mi plumaje es de color {self.color_plumaje}.")

class Aguila(Ave):
    def __init__(self, nombre, habitat, envergadura_alas):
        super().__init__(nombre, habitat)
        self.envergadura_alas = envergadura_alas

    def descripcion(self):
        """
        Imprime una descripción específica del águila.
        """
        print(f"Soy un {self.nombre} y vivo en {self.habitat}. Mi envergadura de alas es de {self.envergadura_alas}.")


ave_generico = Ave("Ave Genérica", "diversos hábitats")
ave_generico.descripcion()

pato = Pato("Pato Silvestre", "lagos", "marrón")
pato.descripcion()

aguila = Aguila("Águila Real", "montañas", 2.5)
aguila.descripcion()
