# utilisateur.py

from src.reservation import Reservation

class Utilisateur:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        self.reservations = []  # Liste des objets Reservation

    def reserver_vol(self, vol):
        # Vérifie si l'utilisateur a déjà une réservation pour ce vol
        if any(reservation.vol == vol for reservation in self.reservations):
            return f"{self.nom} a déjà une réservation sur le vol {vol.numero_vol}."

        # Crée une nouvelle réservation si aucune réservation existante pour ce vol
        if vol.nb_places_disponibles > 0:
            reservation = Reservation(self, vol)
            self.reservations.append(reservation)
            vol.nb_places_disponibles -= 1
            return f"{self.nom} a réservé un siège sur le vol {vol.numero_vol} (ID réservation: {reservation.id})."
        return f"Aucune place disponible sur le vol {vol.numero_vol}."

    def annuler_reservation(self, reservation_id):
        reservation = next((res for res in self.reservations if res.id == reservation_id), None)
        if reservation:
            self.reservations.remove(reservation)
            reservation.vol.nb_places_disponibles += 1
            return f"{self.nom} a annulé la réservation {reservation_id} sur le vol {reservation.vol.numero_vol}."
        return f"Aucune réservation trouvée avec l'ID {reservation_id}."

    def __str__(self):
        return f"Utilisateur: {self.nom}, Âge: {self.age}, Email: {self.email}, Réservations: {len(self.reservations)} vols"
