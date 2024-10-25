
class Controleur:
    def reserver_pour_utilisateur(self, utilisateur, vol):
        message = utilisateur.reserver_vol(vol)
        print(message)

    def annuler_pour_utilisateur(self, utilisateur, vol):
        message = utilisateur.annuler_reservation(vol)
        print(message)
