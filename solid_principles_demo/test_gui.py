#!/usr/bin/env python3
"""
Script de prueba para verificar que la GUI funciona correctamente.
Ejecuta la aplicación GUI y muestra un mensaje de prueba.
"""

import tkinter as tk
from tkinter import messagebox

def test_gui():
    """Función de prueba para verificar la GUI."""
    root = tk.Tk()
    root.title("Test GUI")
    root.geometry("300x200")
    
    label = tk.Label(root, text="GUI Test - Tkinter funciona!", font=("Arial", 14))
    label.pack(pady=50)
    
    def show_message():
        messagebox.showinfo("Test", "La GUI está funcionando correctamente!")
    
    button = tk.Button(root, text="Probar MessageBox", command=show_message)
    button.pack(pady=10)
    
    def close_test():
        root.destroy()
        # Importar y ejecutar la GUI real
        try:
            from gui_app import main as gui_main
            gui_main()
        except Exception as e:
            print(f"Error ejecutando GUI real: {e}")
    
    launch_button = tk.Button(root, text="Lanzar GUI SOLID", command=close_test, bg="green", fg="white")
    launch_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    test_gui()
