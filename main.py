# main.py
# ---------------------------------------
# Gestió Biblioteca La Violeta
# Diana Urbano Fernandez
# ---------------------------------------

# Missatge de benvinguda per consola
def mostrar_benvinguda():
    print("---------------------------------------")
    print("Gestió Biblioteca La Violeta")
    print("Estudiant: Diana Urbano Fernandez")
    print("---------------------------------------\n")

if __name__ == "__main__":
    mostrar_benvinguda()


# ---------------------------------------
# IMPORTS
# ---------------------------------------
import tkinter as tk
from tkinter import messagebox

# Importem les interfícies gràfiques
from ui_llibres import crear_ui_llibres
from ui_autors import finestra_autors
from ui_alumnes import finestra_alumnes
from ui_prestecs import finestra_prestecs


# ---------------------------------------
# FUNCIONS DEL MENÚ PRINCIPAL
# ---------------------------------------
def obrir_autors():
    finestra = tk.Toplevel(root)
    finestra.title("Gestió d'Autors/es")
    finestra_autors(finestra)


def obrir_alumnes():
    finestra = tk.Toplevel(root)
    finestra.title("Gestió d'Alumnes")
    finestra_alumnes(finestra)


def obrir_llibres():
    finestra = tk.Toplevel(root)
    finestra.title("Gestió de Llibres")
    crear_ui_llibres(finestra)


def obrir_prestecs():
    finestra = tk.Toplevel(root)
    finestra.title("Gestió de Préstecs")
    finestra_prestecs(finestra)


# ---------------------------------------
# FINESTRA PRINCIPAL
# ---------------------------------------
root = tk.Tk()
root.title("Gestió Biblioteca La Violeta")
root.geometry("400x280")

tk.Label(root, text="Benvingut/da a la Biblioteca",
         font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="Selecciona una secció del menú",
         font=("Arial", 10)).pack(pady=10)

# Botons principals
tk.Button(root, text="Autors/es", width=20, command=obrir_autors).pack(pady=5)
tk.Button(root, text="Alumnes", width=20, command=obrir_alumnes).pack(pady=5)
tk.Button(root, text="Llibres", width=20, command=obrir_llibres).pack(pady=5)
tk.Button(root, text="Préstecs", width=20, command=obrir_prestecs).pack(pady=5)

root.mainloop()
