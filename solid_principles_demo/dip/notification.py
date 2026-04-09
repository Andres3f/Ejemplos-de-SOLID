# solid_principles_demo/dip/notification.py
"""
DEPENDENCY INVERSION PRINCIPLE (DIP)

Este archivo demuestra el DIP.
DIP establece que:
1. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
2. Las abstracciones no deben depender de detalles. Los detalles deben depender de abstracciones.

Ejemplo: Servicio de notificaciones.
- NotificationService (alto nivel) no depende de EmailSender o SmsSender (bajo nivel).
- Todos dependen de la abstracción NotificationSender.
- La dependencia se inyecta por constructor (Dependency Injection).

Beneficio: Fácil cambiar implementaciones (ej. agregar PushSender) sin modificar NotificationService.
El código es más flexible y testable.
"""

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailSender(NotificationSender):
    def send(self, message: str):
        print(f"Enviando email: {message}")


class SmsSender(NotificationSender):
    def send(self, message: str):
        print(f"Enviando SMS: {message}")


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str):
        self.sender.send(message)


# Ejemplo de uso
if __name__ == "__main__":
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SmsSender())

    email_service.notify("Hola por email")
    sms_service.notify("Hola por SMS")