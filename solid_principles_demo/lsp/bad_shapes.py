# solid_principles_demo/lsp/bad_shapes.py
"""
LISKOV SUBSTITUTION PRINCIPLE (LSP) - Versión Mala

Este archivo demuestra una violación del LSP.
LSP establece que los objetos de una subclase deben poder reemplazar a los objetos de la clase base
sin alterar el comportamiento esperado del programa.

Problema: Square hereda de Rectangle, pero cambia el comportamiento.
En Rectangle, width y height son independientes.
En Square, cambiar width también cambia height, lo que rompe la expectativa.

Si un código espera un Rectangle y llama set_width(5) luego set_height(10),
espera área 50, pero con Square sería 100, causando bugs.
"""

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def set_width(self, width: float):
        self.width = width
        self.height = width  # Fuerza igualdad

    def set_height(self, height: float):
        self.width = height
        self.height = height  # Fuerza igualdad


# Ejemplo problemático
if __name__ == "__main__":
    def calculate_area(rect: Rectangle) -> float:
        rect.set_width(5)
        rect.set_height(10)
        return rect.area()

    rect = Rectangle(0, 0)
    square = Square(0)

    print(f"Área Rectangle: {calculate_area(rect)}")  # Esperado: 50
    print(f"Área Square: {calculate_area(square)}")    # Resultado: 100 (incorrecto)