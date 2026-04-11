# solid_principles_demo/gui_app.py
"""
Aplicación GUI para demostrar los 5 principios SOLID usando Tkinter.
Esta aplicación proporciona una interfaz gráfica para ejecutar y visualizar
los ejemplos de cada principio SOLID.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr

# Importar las funciones de demostración del main original
try:
    from .main import (
        demonstrate_srp,
        demonstrate_ocp, 
        demonstrate_lsp,
        demonstrate_isp,
        demonstrate_dip
    )
except ImportError:
    # Importación absoluta para ejecución directa
    from main import (
        demonstrate_srp,
        demonstrate_ocp, 
        demonstrate_lsp,
        demonstrate_isp,
        demonstrate_dip
    )


class SolidPrinciplesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de los 5 Principios SOLID")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Configurar estilos
        self.setup_styles()
        
        # Crear widgets
        self.create_widgets()
        
    def setup_styles(self):
        """Configurar estilos para la aplicación."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilo para botones grandes
        style.configure('Large.TButton', font=('Arial', 11, 'bold'), padding=10)
        
    def create_widgets(self):
        """Crear todos los widgets de la interfaz."""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Título principal
        title_label = ttk.Label(
            main_frame, 
            text="Demostración de los 5 Principios SOLID",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Frame para botones
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)
        buttons_frame.columnconfigure(2, weight=1)
        
        # Botones para cada principio
        self.create_principle_buttons(buttons_frame)
        
        # Frame para botones de control
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Botones de control
        ttk.Button(control_frame, text="Limpiar", command=self.clear_text).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Ejecutar Todos", command=self.run_all_principles).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Salir", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
        
        # Área de texto con scroll
        self.text_area = scrolledtext.ScrolledText(
            main_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=('Consolas', 10)
        )
        self.text_area.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.rowconfigure(3, weight=1)
        
    def create_principle_buttons(self, parent):
        """Crear los botones para cada principio SOLID."""
        buttons_info = [
            ("1. Single Responsibility\nPrinciple (SRP)", self.run_srp, 0, 0),
            ("2. Open/Closed\nPrinciple (OCP)", self.run_ocp, 0, 1),
            ("3. Liskov Substitution\nPrinciple (LSP)", self.run_lsp, 0, 2),
            ("4. Interface Segregation\nPrinciple (ISP)", self.run_isp, 1, 0),
            ("5. Dependency Inversion\nPrinciple (DIP)", self.run_dip, 1, 1),
        ]
        
        for text, command, row, col in buttons_info:
            btn = ttk.Button(
                parent,
                text=text,
                command=command,
                style='Large.TButton',
                width=20
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky=(tk.W, tk.E))
    
    def clear_text(self):
        """Limpiar el área de texto."""
        self.text_area.delete(1.0, tk.END)
        
    def append_text(self, text):
        """Añadir texto al área de texto."""
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)  # Auto-scroll al final
        self.root.update_idletasks()  # Actualizar la interfaz
        
    def capture_output(self, func, explanation=""):
        """
        Capturar la salida de una función y mostrarla en el área de texto.
        """
        self.clear_text()
        
        if explanation:
            self.append_text(explanation + "\n" + "="*50 + "\n\n")
        
        # Capturar salida estándar
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            func()
        except Exception as e:
            self.append_text(f"Error al ejecutar: {e}\n")
        finally:
            # Restaurar stdout
            sys.stdout = old_stdout
            output = captured_output.getvalue()
            if output:
                self.append_text(output)
            self.append_text("\n")
    
    def run_srp(self):
        """Ejecutar demostración del SRP."""
        explanation = """SINGLE RESPONSIBILITY PRINCIPLE (SRP)

¿Qué problema resuelve?
Evita que una clase tenga múltiples razones para cambiar. Cada clase debe tener una sola responsabilidad.

¿Cómo se aplica?
- ReportGenerator: Solo se encarga de generar reportes
- EmailSender: Solo se encarga de enviar emails
- ReportService: Coordina las operaciones pero no implementa la lógica específica

Beneficio: Si cambia la lógica de email, solo modificamos EmailSender. Si cambia la generación, solo ReportGenerator."""
        
        self.capture_output(demonstrate_srp, explanation)
    
    def run_ocp(self):
        """Ejecutar demostración del OCP."""
        explanation = """OPEN/CLOSED PRINCIPLE (OCP)

¿Qué problema resuelve?
Permite extender el comportamiento de una clase sin modificar su código existente.

¿Cómo se aplica?
- Discount es una clase abstracta que define el contrato
- ChristmasDiscount y VIPDiscount extienden sin modificar el código existente
- ShoppingCart depende de la abstracción, no de implementaciones concretas

Beneficio: Para agregar un nuevo descuento (ej. BlackFridayDiscount), solo creamos una nueva clase, sin tocar ShoppingCart ni las existentes.

Ejemplo de Código:

```python
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
```"""
        
        self.capture_output(demonstrate_ocp, explanation)
    
    def run_lsp(self):
        """Ejecutar demostración del LSP."""
        explanation = """LISKOV SUBSTITUTION PRINCIPLE (LSP)

¿Qué problema resuelve?
Asegura que las subclases puedan ser sustituidas por sus clases base sin alterar el comportamiento del programa.

¿Cómo se aplica?
- Shape define el contrato mínimo (método area)
- Rectangle y Square implementan Shape de manera compatible
- Cualquier código que use Shape funcionará correctamente con ambas

Beneficio: Square y Rectangle pueden usarse indistintamente donde se espere un Shape, sin romper el comportamiento esperado."""
        
        self.capture_output(demonstrate_lsp, explanation)
    
    def run_isp(self):
        """Ejecutar demostración del ISP."""
        explanation = """INTERFACE SEGREGATION PRINCIPLE (ISP)

¿Qué problema resuelve?
Evita que las clases se vean forzadas a implementar interfaces que no utilizan.

¿Cómo se aplica?
- Printer: Solo impresión
- Scanner: Solo escaneo  
- FaxMachine: Solo fax
- SimplePrinter implementa solo Printer
- MultiFunctionPrinter implementa todas las interfaces que necesita

Beneficio: Las clases no implementan métodos innecesarios. Los clientes dependen solo de lo que usan."""
        
        self.capture_output(demonstrate_isp, explanation)
    
    def run_dip(self):
        """Ejecutar demostración del DIP."""
        explanation = """DEPENDENCY INVERSION PRINCIPLE (DIP)

¿Qué problema resuelve?
Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.

¿Cómo se aplica?
- NotificationService (alto nivel) no depende de EmailSender o SmsSender (bajo nivel)
- Todos dependen de la abstracción NotificationSender
- La dependencia se inyecta por constructor (Dependency Injection)

Beneficio: Fácil cambiar implementaciones (ej. agregar PushSender) sin modificar NotificationService. El código es más flexible y testable."""
        
        self.capture_output(demonstrate_dip, explanation)
    
    def run_all_principles(self):
        """Ejecutar todas las demostraciones en secuencia."""
        self.clear_text()
        self.append_text("EJECUTANDO TODOS LOS PRINCIPIOS SOLID\n")
        self.append_text("="*60 + "\n\n")
        
        principles = [
            (self.run_srp, "SRP"),
            (self.run_ocp, "OCP"), 
            (self.run_lsp, "LSP"),
            (self.run_isp, "ISP"),
            (self.run_dip, "DIP")
        ]
        
        for i, (func, name) in enumerate(principles):
            self.append_text(f"\n--- {i+1}. Ejecutando {name} ---\n\n")
            self.root.update_idletasks()
            
            # Capturar salida sin limpiar el área de texto
            old_stdout = sys.stdout
            sys.stdout = captured_output = StringIO()
            
            try:
                func()
            except Exception as e:
                self.append_text(f"Error al ejecutar {name}: {e}\n")
            finally:
                sys.stdout = old_stdout
                output = captured_output.getvalue()
                if output:
                    self.append_text(output)
                self.append_text("\n" + "-"*40 + "\n")
                self.text_area.see(tk.END)
                self.root.update_idletasks()


def main():
    """Función principal para lanzar la aplicación GUI."""
    root = tk.Tk()
    app = SolidPrinciplesGUI(root)
    
    # Centrar ventana en pantalla
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
