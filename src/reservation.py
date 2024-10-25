# reservation.py

import uuid

class Reservation:
    def __init__(self, utilisateur, vol):
        self.id = str(uuid.uuid4())  # Génère un identifiant unique pour chaque réservation
        self.utilisateur = utilisateur
        self.vol = vol  # Vol associé à cette réservation

    def __str__(self):
        return f"Réservation ID: {self.id} - Vol: {self.vol.numero_vol} pour {self.utilisateur.nom}"
