# src/reservation.py

import uuid

class Reservation:
    def __init__(self, utilisateur, vol):
        self.id = str(uuid.uuid4())  
        self.utilisateur = utilisateur
        self.vol = vol

    @classmethod
    def creer_reservation(cls, utilisateur, vol):
        """Crée une réservation pour l'utilisateur si les conditions sont respectées (pas de réservation existante, places disponibles)."""
        if any(reservation.vol == vol for reservation in utilisateur.reservations):
            return f"{utilisateur.nom} a déjà une réservation sur le vol {vol.numero_vol}."
        
        if vol.nb_places_disponibles > 0:
            reservation = cls(utilisateur, vol)  
            utilisateur.reservations.append(reservation)  
            vol.nb_places_disponibles -= 1  
            return f"{utilisateur.nom} a réservé un siège sur le vol {vol.numero_vol} (ID réservation: {reservation.id})."
        
        return f"Aucune place disponible sur le vol {vol.numero_vol}."

    @classmethod
    def annuler_reservation(cls, utilisateur, reservation_id):
        """Annule la réservation si elle existe pour l'utilisateur."""
        reservation = next((res for res in utilisateur.reservations if res.id == reservation_id), None)
        if reservation:
            utilisateur.reservations.remove(reservation)  
            reservation.vol.nb_places_disponibles += 1 
            return f"{utilisateur.nom} a annulé la réservation {reservation_id} sur le vol {reservation.vol.numero_vol}."
        
        return f"Aucune réservation trouvée avec l'ID {reservation_id}."

    def __str__(self):
        return f"Réservation ID: {self.id} - Vol: {self.vol.numero_vol} pour {self.utilisateur.nom}"
