from src.reservation import Reservation

class Utilisateur:
    def __init__(self, nom, age, email):
        self.nom = nom
        self.age = age
        self.email = email
        self.reservations = []  

    @staticmethod
    def ajouter_utilisateur(utilisateurs, nouvel_utilisateur):
        """Ajoute un utilisateur si les conditions sont respectées (champs non vides, âge valide, email unique)."""
        if not nouvel_utilisateur.nom or not nouvel_utilisateur.email:
            raise ValueError("Les champs Nom et Email ne doivent pas être vides.")

        if nouvel_utilisateur.age < 1 or nouvel_utilisateur.age > 120:
            raise ValueError("L'âge doit être compris entre 1 et 120 ans.")

        if any(u.email == nouvel_utilisateur.email for u in utilisateurs):
            raise ValueError("Cet email est déjà utilisé par un autre utilisateur.")
        
        utilisateurs.append(nouvel_utilisateur)

    def reserver_vol(self, vol):
        return Reservation.creer_reservation(self, vol)

    def annuler_reservation(self, reservation_id):
        return Reservation.annuler_reservation(self, reservation_id)

    def __str__(self):
        return f"Utilisateur: {self.nom}, Âge: {self.age}, Email: {self.email}, Réservations: {len(self.reservations)} vols"

