# ui_alumnes.py
# Interfície Tkinter per gestionar alumnes/usuaris
# Funciona amb database.py

import tkinter as tk
from tkinter import messagebox
import database   # Fem servir les funcions del teu mòdul


# -------------------------------------------------------------
# FUNCIONS DE LA UI
# -------------------------------------------------------------
def afegir_alumne_ui(nom_entry, cognoms_entry, email_entry, llista):
    """Llegeix els camps i afegeix un alumne a la BD."""
    nom = nom_entry.get().strip()
    cognoms = cognoms_entry.get().strip()
    email = email_entry.get().strip()

    if not nom or not cognoms or not email:
        messagebox.showerror("Error", "Cal omplir nom, cognoms i email.")
        return

    try:
        database.afegir_alumne(nom, cognoms, email)
        messagebox.showinfo("Correcte", "Alumne/Usuari afegit correctament.")

        # Netejar camps
        nom_entry.delete(0, tk.END)
        cognoms_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        carregar_alumnes(llista)

    except Exception as e:
        messagebox.showerror("Error", f"No s'ha pogut afegir l'alumne:\n{e}")


def carregar_alumnes(llista):
    """Carrega i mostra tots els alumnes al Listbox."""
    llista.delete(0, tk.END)
    alumnes = database.obtenir_alumnes()

    for alumne in alumnes:
        id_alumne, nom, cognoms, email = alumne
        llista.insert(tk.END, f"{id_alumne} - {nom} {cognoms} ({email})")


# -------------------------------------------------------------
# FINESTRA PRINCIPAL
# -------------------------------------------------------------
def finestra_alumnes():
    """Crea una finestra Toplevel per gestionar alumnes/usuaris."""
    win = tk.Toplevel()
    win.title("Gestió d'Alumnes/Usuaris")
    win.geometry("500x360")
    win.resizable(False, False)

    # Formulari ------------------------------------------------
    tk.Label(win, text="Nom:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    nom_entry = tk.Entry(win, width=30)
    nom_entry.grid(row=0, column=1, pady=5)

    tk.Label(win, text="Cognoms:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    cognoms_entry = tk.Entry(win, width=30)
    cognoms_entry.grid(row=1, column=1, pady=5)

    tk.Label(win, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    email_entry = tk.Entry(win, width=30)
    email_entry.grid(row=2, column=1, pady=5)

    # Botó afegir ----------------------------------------------
    btn_afegir = tk.Button(
        win,
        text="Afegir Alumne/Usuari",
        width=25,
        command=lambda: afegir_alumne_ui(nom_entry, cognoms_entry, email_entry, llista)
    )
    btn_afegir.grid(row=3, column=0, columnspan=2, pady=10)

    # Llista d'alumnes -----------------------------------------
    llista = tk.Listbox(win, width=65, height=12)
    llista.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    # Carregar llista inicial
    carregar_alumnes(llista)
