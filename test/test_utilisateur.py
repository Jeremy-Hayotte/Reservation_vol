# tests/test_utilisateurs.py

import pytest
from src.utilisateur import Utilisateur
from src.data_manager_test import charger_utilisateurs, sauvegarder_utilisateurs

@pytest.fixture
def utilisateurs_test():
    """Initialise la liste d'utilisateurs en chargeant les données de test."""
    return charger_utilisateurs(fichier="data/utilisateurs_test.csv")

def test_ajouter_utilisateur_valide(utilisateurs_test):
    """Teste l'ajout d'un utilisateur avec des informations valides."""
    nouvel_utilisateur = Utilisateur("Jean", 30, "gerarementvuça@example.com")  
    Utilisateur.ajouter_utilisateur(utilisateurs_test, nouvel_utilisateur)
    sauvegarder_utilisateurs(utilisateurs_test, fichier="data/utilisateurs_test.csv")

    utilisateurs_apres_sauvegarde = charger_utilisateurs(fichier="data/utilisateurs_test.csv")
    assert any(u.email == "unique@example.com" for u in utilisateurs_apres_sauvegarde), "L'utilisateur devrait être ajouté."

def test_ajouter_utilisateur_email_existant(utilisateurs_test):
    """Teste l'ajout d'un utilisateur avec un email déjà existant dans le système."""
    utilisateur_existant = Utilisateur("Dupont", 40, "lea@example.com")  
    with pytest.raises(ValueError, match="Cet email est déjà utilisé par un autre utilisateur."):
        Utilisateur.ajouter_utilisateur(utilisateurs_test, utilisateur_existant)

def test_ajouter_utilisateur_champs_vides(utilisateurs_test):
    """Teste le refus de création d'un utilisateur avec des champs vides."""
    utilisateur_invalide = Utilisateur("", 25, "")  
    with pytest.raises(ValueError, match="Les champs Nom et Email ne doivent pas être vides."):
        Utilisateur.ajouter_utilisateur(utilisateurs_test, utilisateur_invalide)

def test_ajouter_utilisateur_age_invalide(utilisateurs_test):
    """Teste le refus de création d'un utilisateur avec un âge hors limites."""
    utilisateur_invalide = Utilisateur("Sophie", 200, "sophie@example.com") 
    with pytest.raises(ValueError, match="L'âge doit être compris entre 1 et 120 ans."):
        Utilisateur.ajouter_utilisateur(utilisateurs_test, utilisateur_invalide)
