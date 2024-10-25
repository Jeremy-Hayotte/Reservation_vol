import unittest
from src.vol import Vol
from src.utilisateur import Utilisateur
from src.controleur import Controleur
from src.data_manager import (
    sauvegarder_vols, charger_vols,
    sauvegarder_utilisateurs, charger_utilisateurs,
    sauvegarder_reservations, charger_reservations
)

class TestSystemeReservationVols(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets pour chaque test
        self.vol = Vol("AF123", "Paris", "New York", 150)
        self.utilisateur = Utilisateur("Alison", 33, "alison@example.com")
        self.controleur = Controleur()

    def test_reservation_reduit_places_disponibles(self):
        # Test que le nombre de sièges diminue après une réservation
        places_avant = self.vol.nb_places_disponibles
        self.controleur.reserver_pour_utilisateur(self.utilisateur, self.vol)
        self.assertEqual(self.vol.nb_places_disponibles, places_avant - 1)

    def test_annulation_ajoute_places_disponibles(self):
        # Réservation initiale pour pouvoir tester l'annulation
        self.controleur.reserver_pour_utilisateur(self.utilisateur, self.vol)
        places_apres_reservation = self.vol.nb_places_disponibles
        # Annulation de la réservation
        reservation_id = self.utilisateur.reservations[0].id
        self.utilisateur.annuler_reservation(reservation_id)
        self.assertEqual(self.vol.nb_places_disponibles, places_apres_reservation + 1)

    def test_reservation_associee_utilisateur(self):
        # Vérifie que la réservation est bien associée à l'utilisateur
        self.controleur.reserver_pour_utilisateur(self.utilisateur, self.vol)
        self.assertEqual(len(self.utilisateur.reservations), 1)
        self.assertEqual(self.utilisateur.reservations[0].vol.numero_vol, "AF123")

    def test_annulation_reservation(self):
        # Réservation et annulation pour vérifier la gestion des annulations
        self.controleur.reserver_pour_utilisateur(self.utilisateur, self.vol)
        reservation_id = self.utilisateur.reservations[0].id
        message = self.utilisateur.annuler_reservation(reservation_id)
        self.assertIn("annulé", message)
        self.assertEqual(len(self.utilisateur.reservations), 0)

    def test_sauvegarde_vols_csv(self):
        # Teste la sauvegarde des vols dans un fichier CSV
        vols = [self.vol]
        sauvegarder_vols(vols, fichier="test_vols.csv")
        vols_charges = charger_vols(fichier="test_vols.csv")
        self.assertEqual(len(vols_charges), 1)
        self.assertEqual(vols_charges[0].numero_vol, self.vol.numero_vol)

    def test_sauvegarde_utilisateurs_csv(self):
        # Teste la sauvegarde des utilisateurs dans un fichier CSV
        utilisateurs = [self.utilisateur]
        sauvegarder_utilisateurs(utilisateurs, fichier="test_utilisateurs.csv")
        utilisateurs_charges = charger_utilisateurs(fichier="test_utilisateurs.csv")
        self.assertEqual(len(utilisateurs_charges), 1)
        self.assertEqual(utilisateurs_charges[0].email, self.utilisateur.email)

    def test_sauvegarde_reservations_csv(self):
        # Teste la sauvegarde des réservations dans un fichier CSV
        self.controleur.reserver_pour_utilisateur(self.utilisateur, self.vol)
        utilisateurs = [self.utilisateur]
        sauvegarder_reservations(utilisateurs, fichier="test_reservations.csv")
        vols = [self.vol]
        utilisateurs_charges = charger_utilisateurs(fichier="test_utilisateurs.csv")
        charger_reservations(utilisateurs_charges, vols, fichier="test_reservations.csv")
        self.assertEqual(len(utilisateurs_charges[0].reservations), 1)
        self.assertEqual(utilisateurs_charges[0].reservations[0].vol.numero_vol, self.vol.numero_vol)

if __name__ == "__main__":
    unittest.main()
