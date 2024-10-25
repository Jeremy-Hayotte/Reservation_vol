# data_manager.py

import csv
from vol import Vol
from utilisateur import Utilisateur
from reservation import Reservation

# Fonctions pour les Vols
def sauvegarder_vols(vols, fichier="data/vols.csv"):
    with open(fichier, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Numero_vol", "Depart", "Destination", "Nb_places_disponibles"])
        for vol in vols:
            writer.writerow([vol.numero_vol, vol.depart, vol.destination, vol.nb_places_disponibles])

def charger_vols(fichier="data/vols.csv"):
    vols = []
    with open(fichier, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            vol = Vol(row["Numero_vol"], row["Depart"], row["Destination"], int(row["Nb_places_disponibles"]))
            vols.append(vol)
    return vols

# Fonctions pour les Utilisateurs
def sauvegarder_utilisateurs(utilisateurs, fichier="data/utilisateurs.csv"):
    with open(fichier, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Age", "Email"])
        for utilisateur in utilisateurs:
            writer.writerow([utilisateur.nom, utilisateur.age, utilisateur.email])

def charger_utilisateurs(fichier="data/utilisateurs.csv"):
    utilisateurs = []
    with open(fichier, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            utilisateur = Utilisateur(row["Nom"], int(row["Age"]), row["Email"])
            utilisateurs.append(utilisateur)
    return utilisateurs

# Fonctions pour les Réservations
def sauvegarder_reservations(utilisateurs, fichier="data/reservations.csv"):
    with open(fichier, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Reservation_ID", "Email_utilisateur", "Numero_vol"])
        for utilisateur in utilisateurs:
            for reservation in utilisateur.reservations:
                writer.writerow([reservation.id, utilisateur.email, reservation.vol.numero_vol])

def charger_reservations(utilisateurs, vols, fichier="data/reservations.csv"):
    with open(fichier, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            utilisateur = next((u for u in utilisateurs if u.email == row["Email_utilisateur"]), None)
            vol = next((v for v in vols if v.numero_vol == row["Numero_vol"]), None)
            if utilisateur and vol:
                reservation = Reservation(utilisateur, vol)
                utilisateur.reservations.append(reservation)
                vol.nb_places_disponibles -= 1  # Ajuster les places disponibles
