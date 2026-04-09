# solid_principles_demo/README.md

# SOLID Principles Demo

Este proyecto demuestra los 5 principios SOLID en Python de manera clara y educativa. Cada principio se ilustra con ejemplos prácticos en una aplicación de consola.

## Integrantes del Grupo
José Andrés 

## Instrucciones para Ejecutar
1. Asegúrate de tener Python 3.6+ instalado.
2. Navega al directorio del proyecto.
3. Ejecuta: `python -m solid_principles_demo.main`

## Principios SOLID

### 1. Single Responsibility Principle (SRP)
- **Carpeta**: [srp/](srp/)
- **Descripción**: Una clase debe tener una sola responsabilidad. Se demuestra separando la generación de reportes del envío de emails.

### 2. Open/Closed Principle (OCP)
- **Carpeta**: [ocp/](ocp/)
- **Descripción**: Las entidades deben estar abiertas para extensión pero cerradas para modificación. Se muestra con un sistema de descuentos extensible.

### 3. Liskov Substitution Principle (LSP)
- **Carpeta**: [lsp/](lsp/)
- **Descripción**: Los objetos de subclases deben poder reemplazar a objetos de la clase base sin alterar el comportamiento. Se ilustra con formas geométricas.

### 4. Interface Segregation Principle (ISP)
- **Carpeta**: [isp/](isp/)
- **Descripción**: Los clientes no deben depender de interfaces que no usan. Se demuestra segregando interfaces de impresión.

### 5. Dependency Inversion Principle (DIP)
- **Carpeta**: [dip/](dip/)
- **Descripción**: Depender de abstracciones, no de implementaciones concretas. Se muestra con un servicio de notificaciones usando inyección de dependencias.