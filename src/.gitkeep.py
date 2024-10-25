import csv
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


def sauvegarder_donnees(vols, utilisateurs, fichier_vols=r'C:\Users\Utilisateur\Downloads\Reservation_vol\data\vols.xlsx', 
                            fichier_reservations=r'C:\Users\Utilisateur\Downloads\Reservation_vol\data\reservations.xlsx'):
    # Sauvegarder les vols
    with open(fichier_vols, mode='w', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['numero_vol', 'depart', 'destination', 'nb_places_disponibles'])
        for vol in vols:
            writer.writerow([vol.numero_vol, vol.depart, vol.destination, vol.nb_places_disponibles])
    print(f"Les informations des vols ont été sauvegardées dans {fichier_vols}.")

    # Sauvegarder les réservations
    with open(fichier_reservations, mode='w', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['email_utilisateur', 'numero_vol'])
        for utilisateur in utilisateurs:
            for vol in utilisateur.reservations:
                writer.writerow([utilisateur.email, vol.numero_vol])
    print(f"Les informations des réservations ont été sauvegardées dans {fichier_reservations}.")


    def __str__(self):
        return f"Utilisateur: {self.nom}, Âge: {self.age}, Email: {self.email}, Réservations: {len(self.reservations)} vols"
    
# Charger les données depuis un fichier CSV
def charger_donnees(fichier_vols=r'C:\Users\Utilisateur\Downloads\Reservation_vol\data\vols.xlsx', 
                    fichier_reservations=r'C:\Users\Utilisateur\Downloads\Reservation_vol\data\reservations.xlsx'):
    vols = {}
    utilisateurs = {}

    # Charger les vols
    try:
        with open(fichier_vols, mode='r') as fichier:
            reader = csv.DictReader(fichier)
            for row in reader:
                vol = Vol(row['numero_vol'], row['depart'], row['destination'], int(row['nb_places_disponibles']))
                vols[vol.numero_vol] = vol
        print("Les informations des vols ont été chargées.")
    except FileNotFoundError:
        print(f"Le fichier {fichier_vols} n'a pas été trouvé.")

    # Charger les réservations
    try:
        with open(fichier_reservations, mode='r') as fichier:
            reader = csv.DictReader(fichier)
            for row in reader:
                email = row['email_utilisateur']
                numero_vol = row['numero_vol']
                if email not in utilisateurs:
                    utilisateurs[email] = Utilisateur(email, 0, email)  # Placeholder, âge 0 et email comme nom
                if numero_vol in vols:
                    utilisateurs[email].reserver_vol(vols[numero_vol])
        print("Les informations des réservations ont été chargées.")
    except FileNotFoundError:
        print(f"Le fichier {fichier_reservations} n'a pas été trouvé.")

    return list(vols.values()), list(utilisateurs.values())

# Création d'exemples de données
vol1 = Vol("AF123", "Paris", "New York", 150)
vol2 = Vol("AF124", "Londres", "Tokyo", 200)

utilisateur1 = Utilisateur("Alison", 33, "alison@example.com")
utilisateur2 = Utilisateur("Bob", 40, "bob@example.com")

# Réservations
utilisateur1.reserver_vol(vol1)
utilisateur2.reserver_vol(vol2)

# Sauvegarder les données
sauvegarder_donnees([vol1, vol2], [utilisateur1, utilisateur2])

# Charger les données
vols_charges, utilisateurs_charges = charger_donnees()
print(vols_charges)
print(utilisateurs_charges)
