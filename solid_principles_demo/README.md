# SOLID Principles Demo

Este proyecto demuestra los 5 principios SOLID en Python de manera clara y educativa. Cada principio se ilustra con ejemplos prácticos en una aplicación de consola y con una interfaz gráfica interactiva usando Tkinter.

## Integrantes del Grupo

- José Andres Alvarez Cardona 0907-22-11608
- Juana Yessenia Ramírez Santiago 0907-22-13755
- Diana Paola Rivas Arana 0907-22-15036
- Jorge Antonio Hernández Nájera 0907-20-23870

## Instrucciones para Ejecutar

### Interfaz Gráfica (Recomendado)

1. Asegúrate de tener Python 3.6 o superior instalado (Tkinter viene incluido).
2. Navega al directorio del proyecto:
cd solid_principles_demo
text3. Ejecuta la aplicación gráfica:
python gui_app.py
texto
python main.py
text### Versión Consola

1. Asegúrate de tener Python 3.6 o superior instalado.
2. Navega al directorio del proyecto.
3. Ejecuta:
python -m solid_principles_demo.main
text### Script de Prueba (Tkinter)

Para verificar que Tkinter funciona correctamente:
```bash
python test_gui.py
Características de la GUI

Ventana principal con título "Demostración de los 5 Principios SOLID"
5 botones grandes para cada principio con explicaciones detalladas
Área de texto con scroll para visualizar la salida de cada ejemplo
Botón "Ejecutar Todos" para correr todas las demostraciones en secuencia
Botón "Limpiar" para borrar el área de texto
Botón "Salir" para cerrar la aplicación

Principios SOLID
1. Single Responsibility Principle (SRP)

Carpeta: srp/
Descripción: Una clase debe tener una sola responsabilidad. Se demuestra separando la generación de reportes del envío de emails.

2. Open/Closed Principle (OCP)

Carpeta: ocp/
Descripción: Las entidades deben estar abiertas para extensión pero cerradas para modificación. Se muestra con un sistema de descuentos extensible.

Ejemplo de Código:
Pythonfrom abc import ABC, abstractmethod

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
3. Liskov Substitution Principle (LSP)

Carpeta: lsp/
Descripción: Los objetos de subclases deben poder reemplazar a objetos de la clase base sin alterar el comportamiento. Se ilustra con formas geométricas.

4. Interface Segregation Principle (ISP)

Carpeta: isp/
Descripción: Los clientes no deben depender de interfaces que no usan. Se demuestra segregando interfaces de impresión.

5. Dependency Inversion Principle (DIP)

Carpeta: dip/
Descripción: Depender de abstracciones, no de implementaciones concretas. Se muestra con un servicio de notificaciones usando inyección de dependencias.