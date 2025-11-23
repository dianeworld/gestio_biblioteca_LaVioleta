# ui_autors.py
# Interfície Tkinter per gestionar autors/es
# Funciona amb database.py

import tkinter as tk
from tkinter import messagebox

import database  # utilitzem el mòdul unificat


# -------------------------------------------------------------
# FUNCIONS DE LA UI
# -------------------------------------------------------------
def afegir_autor_ui(nom_entry, cognoms_entry, llista):
    """Llegeix els camps, valida i afegeix un autor/a a la base de dades."""
    nom = nom_entry.get().strip()
    cognoms = cognoms_entry.get().strip()

    if not nom or not cognoms:
        messagebox.showerror("Error", "Cal omplir nom i cognoms.")
        return

    try:
        database.afegir_autor(nom, cognoms)
        messagebox.showinfo("Correcte", "Autor/a afegit correctament.")
        nom_entry.delete(0, tk.END)
        cognoms_entry.delete(0, tk.END)
        carregar_autors(llista)
    except Exception as e:
        messagebox.showerror("Error", f"No s'ha pogut afegir l'autor/a:\n{e}")


def carregar_autors(llista):
    """Actualitza la llista d'autors/es al Listbox."""
    llista.delete(0, tk.END)
    autors = database.obtenir_autors()
    for autor in autors:
        id_autor, nom, cognoms = autor
        llista.insert(tk.END, f"{id_autor} - {nom} {cognoms}")


# -------------------------------------------------------------
# FINESTRA PRINCIPAL D’AUTORS/ES
# -------------------------------------------------------------
def finestra_autors():
    """Crea una finestra Toplevel per gestionar autors/es."""
    win = tk.Toplevel()
    win.title("Gestió d'Autors/es")
    win.geometry("420x320")
    win.resizable(False, False)

    # ---- Formulari ----
    tk.Label(win, text="Nom:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    nom_entry = tk.Entry(win, width=25)
    nom_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Cognoms:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    cognoms_entry = tk.Entry(win, width=25)
    cognoms_entry.grid(row=1, column=1, padx=5, pady=5)

    # Botó Afegir
    boto_afegir = tk.Button(
        win,
        text="Afegir Autor/a",
        width=20,
        command=lambda: afegir_autor_ui(nom_entry, cognoms_entry, llista)
    )
    boto_afegir.grid(row=2, column=0, columnspan=2, pady=10)

    # ---- Llista d’autors ----
    tk.Label(win, text="Llista d'autors/es registrats:").grid(
        row=3, column=0, columnspan=2, pady=5
    )

    llista = tk.Listbox(win, width=50, height=10)
    llista.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    # Carregar dades inicials
    carregar_autors(llista)
