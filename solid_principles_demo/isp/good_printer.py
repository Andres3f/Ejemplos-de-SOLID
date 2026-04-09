# solid_principles_demo/isp/good_printer.py
"""
INTERFACE SEGREGATION PRINCIPLE (ISP) - Versión Buena

Este archivo demuestra el cumplimiento del ISP.
En lugar de una interfaz grande, segregamos en interfaces específicas:
- Printer: Solo impresión
- Scanner: Solo escaneo
- FaxMachine: Solo fax

Las clases implementan solo las interfaces que necesitan.
- SimplePrinter: Solo Printer
- MultiFunctionPrinter: Todas las interfaces

Beneficio: Las clases no están forzadas a implementar métodos innecesarios.
Los clientes dependen solo de lo que usan.
"""

from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class FaxMachine(ABC):
    @abstractmethod
    def fax(self):
        pass


class SimplePrinter(Printer):
    def print(self):
        print("SimplePrinter: Printing")


class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print(self):
        print("MultiFunctionPrinter: Printing")

    def scan(self):
        print("MultiFunctionPrinter: Scanning")

    def fax(self):
        print("MultiFunctionPrinter: Faxing")


# Ejemplo de uso
if __name__ == "__main__":
    simple = SimplePrinter()
    multi = MultiFunctionPrinter()

    simple.print()
    multi.print()
    multi.scan()
    multi.fax()