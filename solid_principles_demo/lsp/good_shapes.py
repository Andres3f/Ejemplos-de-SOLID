# solid_principles_demo/lsp/good_shapes.py
"""
LISKOV SUBSTITUTION PRINCIPLE (LSP) - Versión Buena

Este archivo demuestra el cumplimiento del LSP.
En lugar de heredar Square de Rectangle (que viola LSP),
usamos una abstracción común Shape.

- Shape define el contrato mínimo (area).
- Rectangle y Square implementan Shape de manera que cualquier código
  que use Shape funcionará correctamente con ambas subclases.

Beneficio: Ahora Square y Rectangle pueden usarse indistintamente donde se espere un Shape,
sin romper el comportamiento esperado.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


# Ejemplo correcto
if __name__ == "__main__":
    def calculate_area(shape: Shape) -> float:
        return shape.area()

    rect = Rectangle(5, 10)
    square = Square(5)

    print(f"Área Rectangle: {calculate_area(rect)}")  # 50
    print(f"Área Square: {calculate_area(square)}")    # 25