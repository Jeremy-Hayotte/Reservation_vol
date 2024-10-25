# tests/test_persistence.py

import pytest
from src.utilisateur import Utilisateur
from src.vol import Vol
from src.reservation import Reservation
from src.data_manager_test import (
    sauvegarder_utilisateurs, charger_utilisateurs,
    sauvegarder_vols, charger_vols,
    sauvegarder_reservations, charger_reservations
)

@pytest.fixture
def utilisateurs_test():
    """Initialise la liste d'utilisateurs pour les tests."""
    utilisateurs = charger_utilisateurs(fichier="data/utilisateurs_test.csv")
    return utilisateurs

@pytest.fixture
def vols_test():
    """Initialise la liste de vols pour les tests."""
    vols = charger_vols(fichier="data/vols_test.csv")
    return vols

def test_persistance_utilisateur(utilisateurs_test):
    """Teste la persistance d'un utilisateur en ajoutant, sauvegardant, et rechargeant les données."""
    nouvel_utilisateur = Utilisateur("TestUser", 25, "testuser@example.com")
    utilisateurs_test.append(nouvel_utilisateur)
    sauvegarder_utilisateurs(utilisateurs_test, fichier="data/utilisateurs_test.csv")
    utilisateurs_apres_sauvegarde = charger_utilisateurs(fichier="data/utilisateurs_test.csv")
    assert any(u.email == "testuser@example.com" for u in utilisateurs_apres_sauvegarde), "L'utilisateur ajouté doit être présent après chargement."

def test_persistance_vol(vols_test):
    """Teste la persistance d'un vol en ajoutant, sauvegardant, et rechargeant les données."""
    nouveau_vol = Vol("TEST123", "CityA", "CityB", 100)
    vols_test.append(nouveau_vol)
    sauvegarder_vols(vols_test, fichier="data/vols_test.csv")
    vols_apres_sauvegarde = charger_vols(fichier="data/vols_test.csv")
    assert any(v.numero_vol == "TEST123" for v in vols_apres_sauvegarde), "Le vol ajouté doit être présent après chargement."

def test_persistance_reservation(utilisateurs_test, vols_test):
    """Teste la persistance d'une réservation en ajoutant, sauvegardant, et rechargeant les données."""
    utilisateur = utilisateurs_test[0]
    vol = vols_test[0]
    Reservation.creer_reservation(utilisateur, vol)
    sauvegarder_reservations(utilisateurs_test, fichier="data/reservations_test.csv")
    utilisateurs_apres_sauvegarde = charger_utilisateurs(fichier="data/utilisateurs_test.csv")
    vols_apres_sauvegarde = charger_vols(fichier="data/vols_test.csv")
    charger_reservations(utilisateurs_apres_sauvegarde, vols_apres_sauvegarde, fichier="data/reservations_test.csv")
    utilisateur_charge = next((u for u in utilisateurs_apres_sauvegarde if u.email == utilisateur.email), None)
    vol_charge = next((v for v in vols_apres_sauvegarde if v.numero_vol == vol.numero_vol), None)
    assert utilisateur_charge is not None, "L'utilisateur doit être retrouvé après chargement."
    assert vol_charge is not None, "Le vol doit être retrouvé après chargement."
    assert any(res.vol.numero_vol == vol.numero_vol for res in utilisateur_charge.reservations), "La réservation doit être retrouvée après chargement."
