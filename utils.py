import sqlite3
import json
import csv
import os

DB_PATH = 'biblioteca.db'

# -------------------------------------------------------------
# Importació de llibres des de JSON o CSV
# -------------------------------------------------------------
def importar_llibres(path_fitxer):
    """
    Importa llibres des de JSON o CSV a la base de dades SQLite.
    - path_fitxer: ruta al fitxer JSON o CSV
    """
    if not os.path.exists(path_fitxer):
        print(f"Fitxer no trobat: {path_fitxer}")
        return

    ext = os.path.splitext(path_fitxer)[1].lower()
    llibres = []

    # Llegir JSON
    if ext == '.json':
        with open(path_fitxer, 'r', encoding='utf-8') as f:
            llibres = json.load(f)

    # Llegir CSV
    elif ext == '.csv':
        with open(path_fitxer, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila['any_publicacio']:
                    fila['any_publicacio'] = int(fila['any_publicacio'])
                if not fila['isbn'] or fila['isbn'].strip() == '':
                    fila['isbn'] = None
                llibres.append(fila)
    else:
        print("Format de fitxer no suportat. Només CSV o JSON.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for llibre in llibres:
        try:
            # Comprovar si ja existeix ISBN
            if llibre['isbn']:
                cur.execute("SELECT isbn FROM llibre WHERE isbn = ?", (llibre['isbn'],))
                if cur.fetchone():
                    print(f"Llibre ja existent: {llibre['titol']} (ISBN: {llibre['isbn']})")
                    continue

            cur.execute('''
                INSERT INTO llibre (isbn, titol, id_autor, any_publicacio, idioma, disponible)
                VALUES (?, ?, NULL, ?, ?, 1)
            ''', (
                llibre['isbn'],
                llibre['titol'],
                llibre['any_publicacio'],
                llibre['idioma']
            ))
            print(f"Llibre afegit: {llibre['titol']}")
        except Exception as e:
            print(f"Error afegint llibre {llibre['titol']}: {e}")

    conn.commit()
    conn.close()
    print("Importació finalitzada.")


# -------------------------------------------------------------
# Esborrar tots els llibres
# -------------------------------------------------------------
def esborrar_tots_llibres():
    """
    Esborra tots els llibres de la base de dades.
    Útil per reiniciar la taula abans d'una nova importació.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM llibre")
    conn.commit()
    conn.close()
    print("Tots els llibres han estat esborrats de la base de dades.")

