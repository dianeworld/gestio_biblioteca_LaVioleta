# ui_llibres.py
# Interfície gràfica per gestionar llibres

import tkinter as tk
from tkinter import ttk, messagebox

import database
import validacions


# -------------------------------------------------------------
# FUNCIONS DE LA UI
# -------------------------------------------------------------
def afegir_llibre_ui(isbn_entry, titol_entry, autor_entry, any_entry, idioma_entry, editorial_entry, tree):
    """Llegeix els camps, valida i afegeix un llibre a la base de dades."""

    isbn = isbn_entry.get()
    titol = titol_entry.get()
    autor_nom = autor_entry.get()       # <--- Ara és el nom, no un ID
    any_publicacio = any_entry.get()
    idioma = idioma_entry.get()
    editorial = editorial_entry.get()

    # Validació
    if not validacions.validar_llibre(isbn, titol, autor_nom, any_publicacio, idioma):
        return

    try:
        # Nou: passem també editorial
        database.afegir_llibre(isbn, titol, autor_nom, int(any_publicacio), idioma, editorial)

        messagebox.showinfo("Correcte", "Llibre afegit correctament!")

        mostrar_llibres(tree)

        # Netejar camps
        for entry in [isbn_entry, titol_entry, autor_entry, any_entry, idioma_entry, editorial_entry]:
            entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"No s'ha pogut afegir el llibre:\n{e}")


def mostrar_llibres(tree):
    """Mostra tots els llibres de la base de dades al Treeview."""
    for fila in tree.get_children():
        tree.delete(fila)

    llibres = database.obtenir_llibres()

    for llibre in llibres:
        disponible = "Sí" if llibre[6] else "No"

        tree.insert(
            "",
            tk.END,
            values=(
                llibre[0],   # ISBN
                llibre[1],   # Títol
                llibre[2],   # ID Autor (només id, però ja funciona)
                llibre[3],   # Any
                llibre[4],   # Idioma
                llibre[5],   # Editorial
                disponible
            )
        )


# -------------------------------------------------------------
# CREAR FINESTRA LLIBRES
# -------------------------------------------------------------
def crear_ui_llibres(root):
    """Crea la finestra i widgets per gestionar llibres (amb editorial)."""

    root.geometry('750x420')
    root.resizable(False, False)

    # ----------- FORMULARI SUPERIOR ------------------
    frame_form = tk.Frame(root)
    frame_form.pack(padx=10, pady=10, fill=tk.X)

    labels = ["ISBN:", "Títol:", "Autor:", "Any publicació:", "Idioma:", "Editorial:"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(frame_form, text=text).grid(row=i, column=0, sticky=tk.W, pady=2)
        entry = tk.Entry(frame_form, width=40)
        entry.grid(row=i, column=1, pady=2)
        entries.append(entry)

    isbn_entry, titol_entry, autor_entry, any_entry, idioma_entry, editorial_entry = entries

    afegir_btn = tk.Button(
        frame_form,
        text="Afegir Llibre",
        width=20,
        command=lambda: afegir_llibre_ui(
            isbn_entry, titol_entry, autor_entry,
            any_entry, idioma_entry, editorial_entry, tree
        )
    )
    afegir_btn.grid(row=len(labels), column=0, columnspan=2, pady=8)

    # ------------------ TAULA -------------------------
    frame_tree = tk.Frame(root)
    frame_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    cols = ("ISBN", "Títol", "Autor", "Any", "Idioma", "Editorial", "Disponible")

    tree = ttk.Treeview(frame_tree, columns=cols, show="headings", height=12)

    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor=tk.CENTER)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame_tree, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    mostrar_llibres(tree)
