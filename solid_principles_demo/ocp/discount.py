# solid_principles_demo/ocp/discount.py
"""
OPEN/CLOSED PRINCIPLE (OCP)

Este archivo demuestra el OCP.
El principio establece que las entidades de software (clases, módulos, funciones, etc.)
deben estar abiertas para extensión pero cerradas para modificación.

Ejemplo: Sistema de descuentos.
- Usamos una clase abstracta Discount que define el contrato.
- Implementaciones concretas (ChristmasDiscount, VIPDiscount) extienden sin modificar el código existente.
- ShoppingCart depende de la abstracción Discount, no de implementaciones concretas.

Beneficio: Para agregar un nuevo descuento (ej. BlackFridayDiscount), solo creamos una nueva clase,
sin tocar ShoppingCart ni las existentes.
"""

from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        pass


class ChristmasDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.9  # 10% descuento


class VIPDiscount(Discount):
    def apply(self, price: float) -> float:
        return price * 0.8  # 20% descuento


class ShoppingCart:
    def __init__(self, discount: Discount):
        self.discount = discount

    def checkout(self, price: float) -> float:
        return self.discount.apply(price)


# Ejemplo de uso
if __name__ == "__main__":
    cart_christmas = ShoppingCart(ChristmasDiscount())
    cart_vip = ShoppingCart(VIPDiscount())
    price = 100.0
    print(f"Precio original: ${price}")
    print(f"Con descuento de Navidad: ${cart_christmas.checkout(price)}")
    print(f"Con descuento VIP: ${cart_vip.checkout(price)}")