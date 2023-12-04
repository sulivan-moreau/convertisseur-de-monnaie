from forex_python.converter import CurrencyRates
import pickle

historique = []

def sauvegarder_historique():
    with open('historique_conversions.pkl', 'wb') as fichier:
        pickle.dump(historique, fichier)

def charger_historique():
    try:
        with open('historique_conversions.pkl', 'rb') as fichier:
            return pickle.load(fichier)
    except FileNotFoundError:
        return []

def afficher_historique():
    print("\nHistorique des conversions:")
    for conversion in historique:
        print(f"{conversion['montant']} {conversion['devises'][0]} = {conversion['resultat']} {conversion['devises'][1]}")

def ajouter_devise_preferee():
    devise = input("Entrez le code de la devise à ajouter (par exemple, USD): ").upper()
    taux = float(input(f"Entrez le taux de conversion pour 1 {devise} vers l'unité de compte par défaut : "))
    return devise, taux

def convertir():
    montant = float(input("Entrez le montant à convertir : "))
    devise_source = input("Entrez la devise source (par exemple, USD) : ").upper()
    devise_cible = input("Entrez la devise cible (par exemple, EUR) : ").upper()

    taux_de_change = c.get_rate(devise_source, devise_cible)

    if taux_de_change is None:
        print("Erreur : Conversion impossible entre les devises spécifiées.")
        return

    resultat = montant * taux_de_change
    print(f"{montant} {devise_source} équivaut à {resultat} {devise_cible}")

    historique.append({
        'montant': montant,
        'devises': (devise_source, devise_cible),
        'resultat': resultat
    })

if __name__ == "__main__":
    c = CurrencyRates()
    historique = charger_historique()

    while True:
        print("\nConvertisseur de devises")
        print("1. Convertir")
        print("2. Ajouter une devise préférée")
        print("3. Afficher l'historique")
        print("4. Quitter")

        choix = input("Choisissez une option (1-4): ")

        if choix == '4':
            sauvegarder_historique()
            print("Au revoir !")
            break

        elif choix == '1':
            convertir()

        elif choix == '2':
            devise, taux = ajouter_devise_preferee()
            c.add_currency(devise, taux)

        elif choix == '3':
            afficher_historique()

        else:
            print("Erreur : Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
