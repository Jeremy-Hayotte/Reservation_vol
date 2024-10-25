
class Vol:
    def __init__(self, numero_vol, depart, destination, nb_places_disponibles):
        self.numero_vol = numero_vol
        self.depart = depart
        self.destination = destination
        self.nb_places_disponibles = nb_places_disponibles

    @staticmethod
    def ajouter_vol(vols, nouveau_vol):
        """Ajoute un vol si le numéro est unique et si les champs sont valides."""

        if any(v.numero_vol == nouveau_vol.numero_vol for v in vols):
            raise ValueError("Ce numéro de vol existe déjà.")
        
        if not nouveau_vol.depart or not nouveau_vol.destination:
            raise ValueError("La ville de départ et la destination ne doivent pas être vides.")

        if nouveau_vol.nb_places_disponibles <= 0:
            raise ValueError("Le nombre de places doit être un entier positif.")
        
        vols.append(nouveau_vol)

    @staticmethod
    def supprimer_vol(vols, numero_vol):
        """Supprime un vol de la liste si le numéro de vol existe."""
        for vol in vols:
            if vol.numero_vol == numero_vol:
                vols.remove(vol)
                return f"Le vol {numero_vol} a été supprimé avec succès."
        raise ValueError("Aucun vol trouvé avec ce numéro.")


    def __str__(self):
        return f"Vol {self.numero_vol} de {self.depart} vers {self.destination} - Places disponibles: {self.nb_places_disponibles}"
