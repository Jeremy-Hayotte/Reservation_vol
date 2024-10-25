# tests/test_vols.py

import pytest
from src.vol import Vol
from src.data_manager_test import charger_vols, sauvegarder_vols

@pytest.fixture
def vols_test():
    """Initialise la liste de vols en chargeant les données de test."""
    return charger_vols(fichier="data/vols_test.csv")

def test_ajouter_vol_valide(vols_test):
    """Teste l'ajout d'un vol avec des informations valides."""
    nouveau_vol = Vol("AF200", "Paris", "Londres", 150)
    vols_test.append(nouveau_vol)
    sauvegarder_vols(vols_test, fichier="data/vols_test.csv")

    vols_apres_sauvegarde = charger_vols(fichier="data/vols_test.csv")
    assert any(v.numero_vol == "AF200" for v in vols_apres_sauvegarde), "Le vol devrait être ajouté."

def test_ajouter_vol_numero_existant(vols_test):
    """Teste l'ajout d'un vol avec un numéro de vol déjà existant."""
    vol_existant = Vol("AF111", "Lyon", "Berlin", 100)  
    with pytest.raises(ValueError, match="Ce numéro de vol existe déjà."):
        Vol.ajouter_vol(vols_test, vol_existant)

def test_ajouter_vol_champs_vides_ou_invalides(vols_test):
    """Teste le refus de création d'un vol avec des champs vides ou invalides."""
    vol_places_invalides = Vol("AF300", "Nice", "Milan", 0)
    with pytest.raises(ValueError, match="Le nombre de places doit être un entier positif."):
        Vol.ajouter_vol(vols_test, vol_places_invalides)

    vol_depart_vide = Vol("AF400", "", "Madrid", 50)
    with pytest.raises(ValueError, match="La ville de départ et la destination ne doivent pas être vides."):
        Vol.ajouter_vol(vols_test, vol_depart_vide)

    vol_destination_vide = Vol("AF500", "Lisbonne", "", 60)
    with pytest.raises(ValueError, match="La ville de départ et la destination ne doivent pas être vides."):
        Vol.ajouter_vol(vols_test, vol_destination_vide)
