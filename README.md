# Gestionnaire de Réservations de Vols

Ce projet est un système de gestion de réservations de vols, écrit en Python. Il permet la gestion des vols disponibles, des utilisateurs, ainsi que leurs réservations. Le programme charge initialement des données depuis des fichiers CSV, génère des données par défaut si les fichiers sont vides, et permet l'ajout de nouvelles réservations. Toutes les informations sont ensuite sauvegardées dans les fichiers CSV, garantissant une persistance des données.

## Fonctionnalités

- **Gestion des Vols** :
  - Chargement des vols depuis un fichier CSV.
  - Création de vols supplémentaires pour tester le système.
  - Enregistrement des informations mises à jour des vols.

- **Gestion des Utilisateurs** :
  - Chargement des utilisateurs depuis un fichier CSV.
  - Génération d'utilisateurs supplémentaires pour le test.
  - Enregistrement des informations mises à jour des utilisateurs.

- **Réservations** :
  - Création de réservations de vols pour les utilisateurs.
  - Annulation de réservations existantes.
  - Chargement et sauvegarde des réservations dans des fichiers CSV.

## Structure du Projet

Le projet est structuré en modules pour faciliter l'organisation et la réutilisation des fonctionnalités :

- `main.py` : Point d'entrée principal de l'application, où les données sont chargées, les vols et utilisateurs sont générés, les réservations sont effectuées, et les sauvegardes sont lancées.
- `src/vol.py` : Définit la classe `Vol`, représentant un vol avec son numéro, départ, destination, et places disponibles.
- `src/utilisateur.py` : Contient la classe `Utilisateur`, qui gère les informations des utilisateurs et leurs réservations.
- `src/reservation.py` : Gère la classe `Reservation` qui crée une réservation unique entre un utilisateur et un vol.
- `src/controleur.py` : Gère la logique de réservation et d’annulation pour les utilisateurs.
- `src/data_manager.py` : Fournit des fonctions pour charger et sauvegarder les données des vols, utilisateurs, et réservations dans des fichiers CSV.

## Utilisation

Pour démarrer l'application, exécutez `main.py`. L'application tentera de charger les vols et les utilisateurs depuis les fichiers CSV ou en générera si ces fichiers sont absents. Elle affichera les vols et utilisateurs disponibles, puis essaiera de faire une réservation pour chaque utilisateur sur un vol. Les informations finales sont sauvegardées dans des fichiers CSV respectifs.

## Contributions

Les contributions pour améliorer ce projet sont les bienvenues ! Ouvrez une issue pour signaler un bug ou proposer une amélioration, et soumettez une pull request avec une description détaillée des modifications.

---

*Rédigé par Ayoub Taoussi*
