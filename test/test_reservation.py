# tests/test_reservations.py

import pytest
from src.vol import Vol
from src.utilisateur import Utilisateur
from src.reservation import Reservation
from src.data_manager_test import charger_vols, charger_utilisateurs, sauvegarder_reservations, charger_reservations

@pytest.fixture
def vols_test():
    """Initialise la liste de vols en chargeant les données de test."""
    return charger_vols(fichier="data/vols_test.csv")

@pytest.fixture
def utilisateurs_test():
    """Initialise la liste d'utilisateurs en chargeant les données de test."""
    return charger_utilisateurs(fichier="data/utilisateurs_test.csv")

def test_reservation_valide(utilisateurs_test, vols_test):
    """Teste la réservation d'un vol pour un utilisateur avec des places disponibles."""
    utilisateur = utilisateurs_test[0]
    vol = vols_test[0]
    initial_places = vol.nb_places_disponibles
    resultat = utilisateur.reserver_vol(vol)
    sauvegarder_reservations(utilisateurs_test, fichier="data/reservations_test.csv")
    assert resultat == f"{utilisateur.nom} a réservé un siège sur le vol {vol.numero_vol} (ID réservation: {utilisateur.reservations[-1].id})."
    assert vol.nb_places_disponibles == initial_places - 1, "Le nombre de places disponibles doit être réduit de 1."

def test_reservation_deja_existante(utilisateurs_test, vols_test):
    """Teste le refus de réservation si l'utilisateur a déjà réservé le même vol."""
    utilisateur = utilisateurs_test[1]
    vol = vols_test[1]
    utilisateur.reserver_vol(vol) 
    resultat = utilisateur.reserver_vol(vol) 
    assert resultat == f"{utilisateur.nom} a déjà une réservation sur le vol {vol.numero_vol}.", "L'utilisateur ne devrait pas pouvoir réserver deux fois le même vol."

def test_reservation_vol_complet(utilisateurs_test, vols_test):
    """Teste le refus de réservation si le vol est complet."""
    vol = vols_test[2]
    vol.nb_places_disponibles = 0  
    utilisateur = utilisateurs_test[2]
    resultat = utilisateur.reserver_vol(vol)
    assert resultat == f"Aucune place disponible sur le vol {vol.numero_vol}.", "La réservation doit être refusée si le vol est complet."

def test_annulation_reservation(utilisateurs_test, vols_test):
    """Teste l'annulation d'une réservation pour un utilisateur."""
    utilisateur = utilisateurs_test[3]
    vol = vols_test[3]

    utilisateur.reserver_vol(vol)  
    initial_places = vol.nb_places_disponibles  
    reservation_id = utilisateur.reservations[-1].id  
    resultat = utilisateur.annuler_reservation(reservation_id)

    assert resultat == f"{utilisateur.nom} a annulé la réservation {reservation_id} sur le vol {vol.numero_vol}.", "La réservation doit être annulée correctement."
    assert vol.nb_places_disponibles == initial_places + 1, "Le nombre de places disponibles doit augmenter de 1 après annulation."
