# solid_principles_demo/srp/bad_report.py
"""
SINGLE RESPONSIBILITY PRINCIPLE (SRP) - Versión Mala

Este archivo demuestra una violación del SRP.
La clase Report tiene múltiples responsabilidades: generar el reporte y enviarlo por email.
Esto viola SRP porque una clase debería tener una sola razón para cambiar.

Problema: Si cambia la lógica de envío de email, o la generación del reporte,
la clase Report necesita modificarse, mezclando responsabilidades.
"""

class Report:
    def __init__(self, data: str):
        self.data = data

    def generate(self) -> str:
        # Responsabilidad: Generar el reporte
        return f"Reporte generado con datos: {self.data}"

    def send_email(self, content: str):
        # Responsabilidad: Enviar por email (mezclada con generación)
        print(f"Enviando email con contenido: {content}")


# Ejemplo de uso
if __name__ == "__main__":
    report = Report("Datos del reporte")
    content = report.generate()
    report.send_email(content)