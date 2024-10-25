# main.py

from src.vol import Vol
from src.utilisateur import Utilisateur
from src.controleur import Controleur
from src.data_manager import (
    sauvegarder_vols, charger_vols,
    sauvegarder_utilisateurs, charger_utilisateurs,
    sauvegarder_reservations, charger_reservations
)

def generer_vols_supplementaires():
    # Création de vols supplémentaires en plus de ceux chargés depuis le CSV
    vols_supplementaires = [
        Vol("AF111", "Paris", "Rome", 150),
        Vol("AF112", "Paris", "Lisbonne", 120),
        Vol("AF113", "Paris", "Madrid", 130),
        Vol("AF114", "Paris", "Bruxelles", 90),
        Vol("AF115", "Paris", "Amsterdam", 95),
    ]
    print(f"{len(vols_supplementaires)} vols supplémentaires générés.")
    return vols_supplementaires

def generer_utilisateurs_supplementaires():
    # Création d'utilisateurs supplémentaires en plus de ceux chargés depuis le CSV
    utilisateurs_supplementaires = [
        Utilisateur("Léa", 27, "lea@example.com"),
        Utilisateur("Nico", 34, "nico@example.com"),
        Utilisateur("Emma", 29, "emma@example.com"),
        Utilisateur("Paul", 31, "paul@example.com"),
        Utilisateur("Sophie", 45, "sophie@example.com"),
    ]
    print(f"{len(utilisateurs_supplementaires)} utilisateurs supplémentaires générés.")
    return utilisateurs_supplementaires

def main():
    # Charger les vols et utilisateurs depuis les fichiers CSV, ou en générer s'ils sont absents
    print("Chargement des vols et utilisateurs depuis les fichiers...")
    vols = charger_vols() + generer_vols_supplementaires()
    utilisateurs = charger_utilisateurs() + generer_utilisateurs_supplementaires()
    
    # Afficher les vols et utilisateurs après chargement et ajout
    print("\nVols disponibles (après ajout) :")
    for vol in vols:
        print(vol)

    print("\nUtilisateurs disponibles (après ajout) :")
    for utilisateur in utilisateurs:
        print(utilisateur)

    # Création du contrôleur
    controleur = Controleur()

    # Faire des réservations
    print("\nTentative de réservation d'un siège pour chaque utilisateur sur un vol différent :")
    for i, utilisateur in enumerate(utilisateurs):
        vol = vols[i % len(vols)]  # Boucle sur les vols si plus d'utilisateurs que de vols
        resultat = controleur.reserver_pour_utilisateur(utilisateur, vol)
        print(resultat)

    # Affichage de l'état des vols et des utilisateurs après les réservations
    print("\nÉtat des vols après réservations :")
    for vol in vols:
        print(vol)

    print("\nUtilisateurs et leurs réservations :")
    for utilisateur in utilisateurs:
        print(utilisateur)
        for reservation in utilisateur.reservations:
            print(f" - {reservation}")

    # Sauvegarde des données mises à jour dans les fichiers CSV
    print("\nSauvegarde des informations mises à jour dans les fichiers...")
    sauvegarder_vols(vols)
    sauvegarder_utilisateurs(utilisateurs)
    sauvegarder_reservations(utilisateurs)
    print("Sauvegarde terminée avec succès.")

if __name__ == "__main__":
    main()
