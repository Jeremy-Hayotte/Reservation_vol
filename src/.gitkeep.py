class Vol:
    def __init__(self, numero_vol, depart, destination, nb_places_disponibles):
        self.numero_vol = numero_vol                   # Numéro unique du vol (ex: "AF123")
        self.depart = depart                           # Ville de départ (ex: "Paris")
        self.destination = destination                 # Ville de destination (ex: "New York")
        self.nb_places_disponibles = nb_places_disponibles  # Nombre de places disponibles initialement

    def __str__(self):
        return f"Vol {self.numero_vol} de {self.depart} vers {self.destination} - Places disponibles: {self.nb_places_disponibles}"


class Utilisateur:
    def __init__(self, nom, age, email):
        self.nom = nom                     # Nom de l'utilisateur (ex: "Alison")
        self.age = age                     # Âge de l'utilisateur
        self.email = email                 # Identifiant unique de l'utilisateur (ex: email)
        self.reservations = []             # Liste pour stocker les vols réservés par l'utilisateur

    def reserver_vol(self, vol):
        # Vérification si le vol est déjà réservé
        if vol in self.reservations:
            print(f"{self.nom} a déjà réservé un siège sur le vol {vol.numero_vol}.")
            return

        # Vérification des places disponibles
        if vol.nb_places_disponibles > 0:
            self.reservations.append(vol)
            vol.nb_places_disponibles -= 1
            print(f"{self.nom} a réservé un siège sur le vol {vol.numero_vol}.")
        else:
            print(f"Aucune place disponible sur le vol {vol.numero_vol}.")
            
    def annuler_reservation(self, vol):
        if vol in self.reservations:
            self.reservations.remove(vol)
            vol.nb_places_disponibles += 1
            print(f"{self.nom} a annulé sa réservation sur le vol {vol.numero_vol}.")
        else:
            print(f"{self.nom} n'a pas de réservation sur le vol {vol.numero_vol}.")

    def __str__(self):
        return f"Utilisateur: {self.nom}, Âge: {self.age}, Email: {self.email}, Réservations: {len(self.reservations)} vols"


# Exemple d'utilisation :
vol1 = Vol("AF123", "Paris", "New York", 150)
utilisateur1 = Utilisateur("Alison", 33, "alison@example.com")

# Affichage des informations
print(vol1)
print(utilisateur1)

# Réservation et annulation
utilisateur1.reserver_vol(vol1)    # Réserve un siège sur le vol AF123
print(vol1)                        # Vérifie le nombre de places disponibles

utilisateur1.annuler_reservation(vol1)  # Annule la réservation
print(vol1)                              # Vérifie le nombre de places après l'annulation
