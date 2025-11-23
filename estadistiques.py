# estadistics.py
# Aquest mòdul calcula estadístiques de la biblioteca

import json  # Importem el mòdul json per poder llegir i escriure fitxers JSON

FITXER = 'llibres.json'  # Nom del fitxer on guardem la informació dels llibres

# --- Funció per carregar llibres ---
def carregar_llibres():
    # Intentem obrir el fitxer JSON i carregar les dades
    try:
        with open(FITXER, 'r', encoding='utf-8') as f:
            dades = json.load(f)  # Convertim el contingut JSON a un diccionari Python
        return dades.get('llibres', [])  # Tornem només la llista de llibres, o buida si no existeix
    except FileNotFoundError:
        return []  # Si el fitxer no existeix, tornem una llista buida

# --- Funció per mostrar estadístiques principals ---
def mostrar_estadistiques():
    llibres = carregar_llibres()  # Carreguem la llista de llibres

    if not llibres:
        # Si la llista està buida, informem a l'usuari i sortim
        print('La biblioteca està buida! Afegiu algun llibre primer.')
        return

    # Comptem el total de llibres
    total_llibres = len(llibres)
    # Sumem el total de pàgines de tots els llibres
    total_pagines = sum(l['pagines'] for l in llibres)
    # Calculem la mitjana de pàgines
    mitjana_pagines = total_pagines / total_llibres

    # Comptem quants llibres han estat llegits
    llegits = sum(1 for l in llibres if l.get('llegit', False))
    # Calculem el percentatge de llibres llegits
    percentatge_llegits = (llegits / total_llibres) * 100

    # Imprimim les estadístiques amb missatges clars
    print('--- Estadístiques de la teva biblioteca ---')
    print(f'Total de llibres: {total_llibres}')
    print(f'Mitjana de pàgines: {mitjana_pagines:.2f}')
    print(f'Percentatge de llibres llegits: {percentatge_llegits:.2f}%')
