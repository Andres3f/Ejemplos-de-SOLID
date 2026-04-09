# solid_principles_demo/isp/bad_printer.py
"""
INTERFACE SEGREGATION PRINCIPLE (ISP) - Versión Mala

Este archivo demuestra una violación del ISP.
ISP establece que los clientes no deben depender de interfaces que no usan.

Problema: La interfaz Printer es "gorda" con métodos que no todos los clientes necesitan.
SimplePrinter implementa scan() y fax() lanzando NotImplementedError,
lo que indica que la interfaz es demasiado amplia.

Esto fuerza a las clases a implementar métodos innecesarios.
"""

class Printer:
    def print(self):
        print("Printing")

    def scan(self):
        print("Scanning")

    def fax(self):
        print("Faxing")


class SimplePrinter(Printer):
    def print(self):
        print("SimplePrinter: Printing")

    def scan(self):
        raise NotImplementedError("SimplePrinter no puede escanear")

    def fax(self):
        raise NotImplementedError("SimplePrinter no puede enviar fax")


# Ejemplo de uso
if __name__ == "__main__":
    printer = SimplePrinter()
    printer.print()
    # printer.scan()  # Esto lanzaría error