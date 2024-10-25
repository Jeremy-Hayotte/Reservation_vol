# data_manager.py

import csv
from src.vol import Vol
from src.utilisateur import Utilisateur
from src.reservation import Reservation

def sauvegarder_vols(vols, fichier="data/vols_test.csv"):
    """Sauvegarde les vols dans le fichier CSV en UTF-8."""
    with open(fichier, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Numero_vol", "Depart", "Destination", "Nb_places_disponibles"])
        for vol in vols:
            writer.writerow([vol.numero_vol, vol.depart, vol.destination, vol.nb_places_disponibles])

def charger_vols(fichier="data/vols_test.csv"):
    """Charge les vols depuis le fichier CSV en UTF-8."""
    vols = []
    with open(fichier, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            vol = Vol(row["Numero_vol"], row["Depart"], row["Destination"], int(row["Nb_places_disponibles"]))
            vols.append(vol)
    return vols

def sauvegarder_utilisateurs(utilisateurs, fichier="data/utilisateurs_test.csv"):
    """Sauvegarde les utilisateurs dans le fichier CSV en UTF-8."""
    with open(fichier, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Age", "Email"])
        for utilisateur in utilisateurs:
            writer.writerow([utilisateur.nom, utilisateur.age, utilisateur.email])

def charger_utilisateurs(fichier="data/utilisateurs_test.csv"):
    """Charge les utilisateurs depuis le fichier CSV en UTF-8."""
    utilisateurs = []
    with open(fichier, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            utilisateur = Utilisateur(row["Nom"], int(row["Age"]), row["Email"])
            utilisateurs.append(utilisateur)
    return utilisateurs

def sauvegarder_reservations(utilisateurs, fichier="data/reservations_test.csv"):
    """Sauvegarde les réservations dans le fichier CSV en UTF-8."""
    with open(fichier, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID_reservation", "Email_utilisateur", "Numero_vol"])
        for utilisateur in utilisateurs:
            for reservation in utilisateur.reservations:
                writer.writerow([reservation.id, utilisateur.email, reservation.vol.numero_vol])

def charger_reservations(utilisateurs, vols, fichier="data/reservations_test.csv"):
    """Charge les réservations depuis le fichier CSV en UTF-8."""
    with open(fichier, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            utilisateur = next((u for u in utilisateurs if u.email == row["Email_utilisateur"]), None)
            vol = next((v for v in vols if v.numero_vol == row["Numero_vol"]), None)
            if utilisateur and vol:
                reservation = Reservation(utilisateur, vol)
                utilisateur.reservations.append(reservation)
