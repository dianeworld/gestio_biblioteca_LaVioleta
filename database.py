# database.py
# Gestió de la base de dades SQLite per al projecte Gestio-Biblioteca-LaVioleta

import sqlite3

DB_PATH = 'biblioteca.db'


# -------------------------------------------------------------
# CREACIÓ DE LA BASE DE DADES I TAULES
# -------------------------------------------------------------
def crear_bd():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Taula AUTOR
    cur.execute("""
        CREATE TABLE IF NOT EXISTS autor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            cognoms TEXT NOT NULL
        )
    """)

    # Taula ALUMNE
    cur.execute("""
        CREATE TABLE IF NOT EXISTS alumne (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            cognoms TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    # Taula LLIBRE (amb editorial)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS llibre (
            isbn TEXT PRIMARY KEY,
            titol TEXT NOT NULL,
            id_autor INTEGER,
            any_publicacio INTEGER,
            idioma TEXT NOT NULL,
            editorial TEXT,
            disponible INTEGER DEFAULT 1,
            FOREIGN KEY(id_autor) REFERENCES autor(id)
        )
    """)

    # Taula PRÉSTEC
    cur.execute("""
        CREATE TABLE IF NOT EXISTS prestec (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn_llibre TEXT NOT NULL,
            id_alumne INTEGER NOT NULL,
            data_inici TEXT NOT NULL,
            data_final TEXT NOT NULL,
            FOREIGN KEY(isbn_llibre) REFERENCES llibre(isbn),
            FOREIGN KEY(id_alumne) REFERENCES alumne(id)
        )
    """)

    conn.commit()
    conn.close()


# -------------------------------------------------------------
# FUNCIONS PER A AUTORS
# -------------------------------------------------------------
def afegir_autor(nom, cognoms):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO autor (nom, cognoms) VALUES (?, ?)", (nom, cognoms))
    conn.commit()
    conn.close()


def obtenir_autors():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, nom, cognoms FROM autor")
    dades = cur.fetchall()
    conn.close()
    return dades


# -------------------------------------------------------------
# FUNCIONS PER A ALUMNES
# -------------------------------------------------------------
def afegir_alumne(nom, cognoms, email):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO alumne (nom, cognoms, email)
        VALUES (?, ?, ?)
    """, (nom, cognoms, email))
    conn.commit()
    conn.close()


def obtenir_alumnes():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, nom, cognoms, email FROM alumne ORDER BY id ASC")
    dades = cur.fetchall()
    conn.close()
    return dades


# -------------------------------------------------------------
# FUNCIONS PER A LLIBRES
# -------------------------------------------------------------
def afegir_llibre(isbn, titol, autor_nom, any_publicacio, idioma, editorial):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Buscar si existeix un autor amb aquest nom
    cur.execute("SELECT id FROM autor WHERE nom = ?", (autor_nom,))
    resultat = cur.fetchone()

    # Si no existeix, es crea
    if resultat:
        id_autor = resultat[0]
    else:
        cur.execute("INSERT INTO autor (nom, cognoms) VALUES (?, '')", (autor_nom,))
        id_autor = cur.lastrowid

    # Inserir llibre
    cur.execute("""
        INSERT INTO llibre (isbn, titol, id_autor, any_publicacio, idioma, editorial, disponible)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    """, (isbn, titol, id_autor, any_publicacio, idioma, editorial))

    conn.commit()
    conn.close()


def obtenir_llibres():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT isbn, titol, id_autor, any_publicacio, idioma, editorial, disponible
        FROM llibre
    """)
    dades = cur.fetchall()
    conn.close()
    return dades


# -------------------------------------------------------------
# FUNCIONS PER A PRÉSTECS (per quan facis ui_prestecs)
# -------------------------------------------------------------
def afegir_prestec(isbn_llibre, id_alumne, data_inici, data_final):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO prestec (isbn_llibre, id_alumne, data_inici, data_final)
        VALUES (?, ?, ?, ?)
    """, (isbn_llibre, id_alumne, data_inici, data_final))

    # Marquem el llibre com "no disponible"
    cur.execute("UPDATE llibre SET disponible = 0 WHERE isbn = ?", (isbn_llibre,))

    conn.commit()
    conn.close()


def obtenir_prestecs():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT p.id, p.isbn_llibre, l.titol, p.id_alumne, a.nom, a.cognoms, 
               p.data_inici, p.data_final
        FROM prestec p
        JOIN llibre l ON p.isbn_llibre = l.isbn
        JOIN alumne a ON p.id_alumne = a.id
    """)

    dades = cur.fetchall()
    conn.close()
    return dades


# -------------------------------------------------------------
# PROVA
# -------------------------------------------------------------
def prova_bd():
    crear_bd()
    print("Base de dades creada i verificada correctament.")


if __name__ == "__main__":
    prova_bd()

