
class Vol:
    def __init__(self, numero_vol, depart, destination, nb_places_disponibles):
        self.numero_vol = numero_vol
        self.depart = depart
        self.destination = destination
        self.nb_places_disponibles = nb_places_disponibles

    def __str__(self):
        return f"Vol {self.numero_vol} de {self.depart} vers {self.destination} - Places disponibles: {self.nb_places_disponibles}"
