"""
validacions.py
--------------
Funcions de validació per al projecte Gestió Biblioteca La Violeta.

Inclou:
- camps obligatoris
- tipus de dades
- ISBN
- emails senzills
- dates
- missatges d'error amb Tkinter
"""

from tkinter import messagebox
from datetime import datetime


# -------------------------------------------------------------
# CAMP OBLIGATORI
# -------------------------------------------------------------
def camp_obligatori(valor, nom_camp="Camp"):
    """Comprova que un camp no estigui buit."""
    if not valor or str(valor).strip() == "":
        messagebox.showerror("Error", f"{nom_camp} és obligatori.")
        return False
    return True


# -------------------------------------------------------------
# VALIDAR EMAIL SENSE RE
# -------------------------------------------------------------
def validar_email(email):
    """
    Comprova de manera bàsica que l'email conté '@' i '.'.
    Retorna True si sembla correcte.
    """
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Email invàlid.")
        return False
    return True


# -------------------------------------------------------------
# VALIDAR ISBN
# -------------------------------------------------------------
def validar_isbn(isbn):
    """
    Comprova que l'ISBN sigui de 13 dígits i només números.
    """
    if not isbn.isdigit() or len(isbn) != 13:
        messagebox.showerror("Error", "ISBN invàlid (ha de tenir 13 dígits numèrics).")
        return False
    return True


# -------------------------------------------------------------
# VALIDAR DATA
# -------------------------------------------------------------
def validar_data(data_str):
    """
    Comprova que la data tingui format YYYY-MM-DD.
    """
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        messagebox.showerror("Error", f"Data invàlida: {data_str} (format YYYY-MM-DD).")
        return False


# -------------------------------------------------------------
# VALIDAR ANY PUBLICACIÓ
# -------------------------------------------------------------
def validar_any(any_publicacio):
    """Comprova que l'any de publicació sigui un enter vàlid."""
    try:
        any_int = int(any_publicacio)
        if 1000 <= any_int <= datetime.now().year:
            return True
        else:
            messagebox.showerror("Error", "Any de publicació invàlid.")
            return False
    except ValueError:
        messagebox.showerror("Error", "Any de publicació ha de ser un número.")
        return False


# -------------------------------------------------------------
# FUNCIO GENERAL PER VALIDAR LLIBRE
# -------------------------------------------------------------
def validar_llibre(isbn, titol, id_autor, any_publicacio, idioma):
    """
    Valida tots els camps obligatoris d'un llibre abans d'afegir-lo.
    Retorna True si tot és correcte.
    """
    return (camp_obligatori(isbn, "ISBN") and
            camp_obligatori(titol, "Títol") and
            camp_obligatori(id_autor, "Autor") and
            camp_obligatori(any_publicacio, "Any de publicació") and
            camp_obligatori(idioma, "Idioma") and
            validar_isbn(isbn) and
            validar_any(any_publicacio))
