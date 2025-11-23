# ui_prestecs.py
# Finestra Tkinter per gestionar Préstecs

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime, timedelta

# Funció per obtenir alumnes ----------------------------------------
def obtenir_alumnes():
    conn = sqlite3.connect('biblioteca.db')
    cur = conn.cursor()
    cur.execute('SELECT id, nom, cognoms FROM alumne')
    resultats = cur.fetchall()
    conn.close()
    return resultats


# Funció per obtenir llibres disponibles -----------------------------
def obtenir_llibres_disponibles():
    conn = sqlite3.connect('biblioteca.db')
    cur = conn.cursor()
    cur.execute('SELECT isbn, titol FROM llibre WHERE disponible = 1')
    resultats = cur.fetchall()
    conn.close()
    return resultats


# Funció per registrar préstec ---------------------------------------
def registrar_prestec(id_alumne, isbn_llibre, data_inici, data_final):
    conn = sqlite3.connect('biblioteca.db')
    cur = conn.cursor()
    try:
        # Insertar el préstec
        cur.execute('INSERT INTO prestec (isbn_llibre, id_alumne, data_inici, data_final) VALUES (?, ?, ?, ?)',
                    (isbn_llibre, id_alumne, data_inici, data_final))
        # Marcar el llibre com no disponible
        cur.execute('UPDATE llibre SET disponible = 0 WHERE isbn = ?', (isbn_llibre,))
        conn.commit()
        messagebox.showinfo('Èxit', 'Préstec registrat correctament')
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Error a la base de dades: {e}')
    finally:
        conn.close()

# Finestra principal de préstecs -------------------------------------
def finestra_prestecs():
    win = tk.Toplevel()
    win.title('Registrar Préstec')
    win.geometry('500x300')

    # Labels i desplegables
    tk.Label(win, text='Alumne/Usuari:').grid(row=0, column=0, padx=5, pady=5)
    combo_alumnes = ttk.Combobox(win, state='readonly')
    combo_alumnes.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text='Llibre disponible:').grid(row=1, column=0, padx=5, pady=5)
    combo_llibres = ttk.Combo_

'''
1. obtenir_alumnes → retorna tots els alumnes per desplegable.
2. obtenir_llibres_disponibles → retorna llibres amb disponible = 1.
3. registrar_prestec → desa el préstec i marca el llibre com no disponible.
4. finestra_prestecs → finestra Tkinter amb:
    - Selecció d’alumne i llibre
    - Entrades per data d’inici i final
    - Botó “Registrar Préstec”
    - Actualitza automàticament llibres disponibles després de registrar

'''