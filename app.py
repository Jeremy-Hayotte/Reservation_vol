# app.py

import streamlit as st
from src.vol import Vol
from src.utilisateur import Utilisateur
from src.data_manager import (
    charger_vols, charger_utilisateurs, charger_reservations,
    sauvegarder_vols, sauvegarder_utilisateurs, sauvegarder_reservations
)

vols = charger_vols()
utilisateurs = charger_utilisateurs()
charger_reservations(utilisateurs, vols)

st.title("Système de Réservation de Vols")

st.header("Faire une réservation")

utilisateur_email = st.selectbox("Sélectionnez un utilisateur existant", [u.email for u in utilisateurs])
utilisateur = next((u for u in utilisateurs if u.email == utilisateur_email), None)

vol_options = [f"Vol {v.numero_vol} de {v.depart} vers {v.destination}" for v in vols]
vol_selected = st.selectbox("Sélectionnez un vol existant", vol_options)


vol_index = vol_options.index(vol_selected)  
vol = vols[vol_index]  

if st.button("Réserver un siège"):
    if utilisateur and vol:
        resultat = utilisateur.reserver_vol(vol)
        st.success(resultat)
        sauvegarder_vols(vols)
        sauvegarder_utilisateurs(utilisateurs)
        sauvegarder_reservations(utilisateurs)
    else:
        st.error("Veuillez sélectionner un utilisateur et un vol valides.")

if st.button("Annuler la réservation"):
    if utilisateur and vol:
        reservation = next((res for res in utilisateur.reservations if res.vol.numero_vol == vol.numero_vol), None)
        if reservation:
            resultat = utilisateur.annuler_reservation(reservation.id)
            st.warning(resultat)
            sauvegarder_vols(vols)
            sauvegarder_utilisateurs(utilisateurs)
            sauvegarder_reservations(utilisateurs)
        else:
            st.error("Aucune réservation trouvée pour cet utilisateur sur ce vol.")
    else:
        st.error("Veuillez sélectionner un utilisateur et un vol valides.")

st.header("Ajouter un nouvel utilisateur")
with st.form("form_ajout_utilisateur"):
    nom = st.text_input("Nom")
    age = st.number_input("Âge", min_value=1, max_value=120, step=1)
    email = st.text_input("Email")

    if st.form_submit_button("Ajouter utilisateur"):
        if not nom or not email:
            st.error("Tous les champs (Nom, Âge, et Email) doivent être remplis.")
        elif any(u.email == email for u in utilisateurs):
            st.error("Cet email est déjà utilisé par un autre utilisateur.")
        else:
            nouvel_utilisateur = Utilisateur(nom, age, email)
            utilisateurs.append(nouvel_utilisateur)
            st.success(f"Utilisateur {nom} ajouté avec succès.")
            sauvegarder_utilisateurs(utilisateurs)

st.header("Ajouter un nouveau vol")
with st.form("form_ajout_vol"):
    numero_vol = st.text_input("Numéro de vol")
    depart = st.text_input("Ville de départ")
    destination = st.text_input("Ville de destination")
    nb_places = st.number_input("Nombre de places disponibles", min_value=1, step=1)

    if st.form_submit_button("Ajouter vol"):
        if not numero_vol or not depart or not destination:
            st.error("Tous les champs (Numéro de vol, Ville de départ, Ville de destination, Nombre de places) doivent être remplis.")
        elif any(v.numero_vol == numero_vol for v in vols):
            st.error("Ce numéro de vol existe déjà.")
        else:
            nouveau_vol = Vol(numero_vol, depart, destination, nb_places)
            vols.append(nouveau_vol)
            st.success(f"Vol {numero_vol} ajouté avec succès.")
            sauvegarder_vols(vols)

st.subheader("État des vols")
for vol in vols:
    st.text(f"{vol}")

st.subheader("Utilisateurs et leurs réservations")
for utilisateur in utilisateurs:
    st.text(f"{utilisateur}")
    for reservation in utilisateur.reservations:
        st.text(f"  - {reservation}")
