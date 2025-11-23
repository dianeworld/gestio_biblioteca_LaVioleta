"""
models.py
---------
Defineix les classes principals del projecte:
Llibre, Autor i Prestec.

Cada classe conté:
- __init__ per inicialitzar atributs
- Atributs que coincideixen amb la base de dades
- __str__ per mostrar informació llegible a la UI

Aquest fitxer forma part de la programació orientada a objectes (POO)
demanada a la Parte 1 del projecte.
"""


# -------------------------------------------------------------
# Classe Autor/a
# -------------------------------------------------------------
class Autor:
    """
    Representa un autor/a dins la biblioteca.
    Guarda només informació essencial:
    - id_autor (clau primària)
    - nom
    - cognoms
    """

    def __init__(self, id_autor, nom, cognoms):
        self.id_autor = id_autor
        self.nom = nom
        self.cognoms = cognoms

    def __str__(self):
        return f"{self.nom} {self.cognoms}"


# -------------------------------------------------------------
# Classe Llibre
# -------------------------------------------------------------
class Llibre:
    """
    Representa un llibre del catàleg.
    Guarda:
    - isbn
    - títol
    - id_autor (relació amb taula autors)
    - any_publicacio
    - idioma
    - disponible (booleà)
    """

    def __init__(self, isbn, titol, id_autor, any_publicacio, idioma, disponible=True):
        self.isbn = isbn
        self.titol = titol
        self.id_autor = id_autor
        self.any_publicacio = any_publicacio
        self.idioma = idioma
        self.disponible = disponible

    def __str__(self):
        return f"{self.titol} ({self.idioma})"


# -------------------------------------------------------------
# Classe Préstec
# -------------------------------------------------------------
class Prestec:
    """
    Representa el préstec d’un llibre.
    Guarda:
    - id_prestec
    - isbn_llibre (relació amb Llibre)
    - data_inici
    - data_final (pot ser None si encara no s’ha retornat)
    """

    def __init__(self, id_prestec, isbn_llibre, data_inici, data_final):
        self.id_prestec = id_prestec
        self.isbn_llibre = isbn_llibre
        self.data_inici = data_inici
        self.data_final = data_final


# -------------------------------------------------------------
# INSTÀNCIES DE PROVA (no obligatòries per al projecte final)
# -------------------------------------------------------------
if __name__ == "__main__":
    autor1 = Autor(1, "J.K.", "Rowling")
    print("Autor:", autor1)

    llibre1 = Llibre(
        isbn="9788491021234",
        titol="La Gran Teranyina",
        id_autor=1,
        any_publicacio="2017",
        idioma="Català",
        disponible=True
    )
    print("Llibre:", llibre1)

    prestec1 = Prestec(
        id_prestec=1,
        isbn_llibre="9788491021234",
        data_inici="2025-01-10",
        data_final="2025-01-20"
    )
    print("Préstec creat:", prestec1.__dict__)


"""
NOTES:
1. Autor/a només guarda informació bàsica i el seu ID per relacions.
2. Llibre inclou idioma i camp 'disponible'.
3. Préstec relaciona un llibre amb un ISBN.
4. A la UI es mostraran noms inclusius (“Autor/a”).
"""
