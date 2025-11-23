import sqlite3

conn = sqlite3.connect("biblioteca.db")
cur = conn.cursor()
cur.execute("ALTER TABLE llibre ADD COLUMN editorial TEXT")
conn.commit()
conn.close()

print("Columna 'editorial' afegida correctament a la taula llibre.")
