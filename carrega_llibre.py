# carrega_llibre.py
from utils import importar_llibres, esborrar_tots_llibres

def main():
    print("=== Inici de la càrrega de llibres ===\n")

    # Opcional: esborrar tots els llibres existents abans d'importar
    resposta = input("Vols esborrar tots els llibres existents abans d'importar? (s/n): ").lower()
    if resposta == 's':
        esborrar_tots_llibres()
    else:
        print("No s'han esborrat els llibres existents.\n")

    # Importar llibres des de JSON o CSV
    fitxer = input("Introdueix el nom del fitxer per importar (ex: llibres.json o llibres.csv): ").strip()
    importar_llibres(fitxer)

    print("\n=== Càrrega de llibres finalitzada ===")

if __name__ == "__main__":
    main()
