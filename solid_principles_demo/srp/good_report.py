# solid_principles_demo/srp/good_report.py
"""
SINGLE RESPONSIBILITY PRINCIPLE (SRP) - Versión Buena

Este archivo demuestra el cumplimiento del SRP.
Separamos las responsabilidades en clases distintas:
- ReportGenerator: Solo genera el reporte.
- EmailSender: Solo envía emails.
- ReportService: Coordina las dos responsabilidades.

Beneficio: Cada clase tiene una sola razón para cambiar.
Si cambia la lógica de email, solo modificamos EmailSender.
Si cambia la generación, solo ReportGenerator.
"""

from typing import Protocol


class ReportGenerator:
    def __init__(self, data: str):
        self.data = data

    def generate(self) -> str:
        return f"Reporte generado con datos: {self.data}"


class EmailSender:
    def send(self, content: str):
        print(f"Enviando email con contenido: {content}")


class ReportService:
    def __init__(self, generator: ReportGenerator, sender: EmailSender):
        self.generator = generator
        self.sender = sender

    def process(self):
        content = self.generator.generate()
        self.sender.send(content)


# Ejemplo de uso
if __name__ == "__main__":
    generator = ReportGenerator("Datos del reporte")
    sender = EmailSender()
    service = ReportService(generator, sender)
    service.process()