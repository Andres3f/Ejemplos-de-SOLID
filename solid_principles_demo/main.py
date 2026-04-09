# solid_principles_demo/main.py
"""
Ejecuta todos los ejemplos de los principios SOLID.
Este archivo importa y ejecuta un ejemplo demostrativo de cada principio.
"""

from .srp.good_report import ReportService, ReportGenerator, EmailSender
from .ocp.discount import ShoppingCart, ChristmasDiscount, VIPDiscount
from .lsp.good_shapes import Rectangle, Square
from .isp.good_printer import SimplePrinter, MultiFunctionPrinter
from .dip.notification import NotificationService, EmailSender as DipEmailSender, SmsSender


def demonstrate_srp():
    print("=" * 50)
    print("SINGLE RESPONSIBILITY PRINCIPLE (SRP)")
    print("=" * 50)
    print("Demostrando SRP con ReportService que separa generación y envío.")
    generator = ReportGenerator("Datos del reporte")
    sender = EmailSender()
    service = ReportService(generator, sender)
    service.process()
    print()


def demonstrate_ocp():
    print("=" * 50)
    print("OPEN/CLOSED PRINCIPLE (OCP)")
    print("=" * 50)
    print("Demostrando OCP con descuentos extensibles.")
    cart_christmas = ShoppingCart(ChristmasDiscount())
    cart_vip = ShoppingCart(VIPDiscount())
    price = 100.0
    print(f"Precio original: ${price}")
    print(f"Con descuento de Navidad: ${cart_christmas.checkout(price)}")
    print(f"Con descuento VIP: ${cart_vip.checkout(price)}")
    print()


def demonstrate_lsp():
    print("=" * 50)
    print("LISKOV SUBSTITUTION PRINCIPLE (LSP)")
    print("=" * 50)
    print("Demostrando LSP con formas geométricas.")
    rect = Rectangle(4, 5)
    square = Square(4)
    print(f"Área del rectángulo (4x5): {rect.area()}")
    print(f"Área del cuadrado (lado 4): {square.area()}")
    print()


def demonstrate_isp():
    print("=" * 50)
    print("INTERFACE SEGREGATION PRINCIPLE (ISP)")
    print("=" * 50)
    print("Demostrando ISP con impresoras.")
    simple_printer = SimplePrinter()
    multi_printer = MultiFunctionPrinter()
    simple_printer.print()
    multi_printer.print()
    multi_printer.scan()
    multi_printer.fax()
    print()


def demonstrate_dip():
    print("=" * 50)
    print("DEPENDENCY INVERSION PRINCIPLE (DIP)")
    print("=" * 50)
    print("Demostrando DIP con servicio de notificaciones.")
    email_service = NotificationService(DipEmailSender())
    sms_service = NotificationService(SmsSender())
    email_service.notify("Hola por email")
    sms_service.notify("Hola por SMS")
    print()


def main():
    print("Bienvenido a la demostración de los principios SOLID")
    print("Ejecutando todos los ejemplos...")
    print()

    demonstrate_srp()
    demonstrate_ocp()
    demonstrate_lsp()
    demonstrate_isp()
    demonstrate_dip()

    print("Demostración completada.")


if __name__ == "__main__":
    main()