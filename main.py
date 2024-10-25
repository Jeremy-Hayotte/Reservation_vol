# main.py

from src.vol import Vol
from src.utilisateur import Utilisateur
from src.reservation import Reservation
from src.controleur import Controleur



def main():
    # Initialisation des objets
    utilisateur = Utilisateur("Alison", 33, "alison@example.com")
    vol = Vol("AF101", "Paris", "New York", 150)

    # Création du contrôleur
    controleur = Controleur()

    # Première réservation
    print("\nPremière tentative de réservation d'un siège pour Alison sur le vol AF101...")
    resultat = utilisateur.reserver_vol(vol)
    print(resultat)  # Devrait réussir

    # Deuxième réservation sur le même vol
    print("\nDeuxième tentative de réservation d'un siège pour Alison sur le même vol...")
    resultat = utilisateur.reserver_vol(vol)
    print(resultat)  # Devrait indiquer que la réservation existe déjà

if __name__ == "__main__":
    main()
