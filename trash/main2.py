import pickle 
from pathlib import Path 

import streamlit as st
from streamlit_authenticator import st_authenticator

import pandas as pd
import numpy as np

# Fonction pour générer des données simulées
def generate_data(num_rows):
    np.random.seed(0)
    cout_matiere = np.random.uniform(0, 150, size=num_rows)
    quantite_matiere = np.random.uniform(0, 150, size=num_rows)
    type_sac = np.random.choice(['SLG', 'BAG'], size=num_rows)
    matieres_principales = np.random.choice(['Cuir', 'Canvas'], size=num_rows)
    data = {
        'COUT_MATIERE': cout_matiere,
        'QUANTITE_MATIERE': quantite_matiere,
        'TYPE_SAC': type_sac,
        'MATIERES_PRINCIPALES': matieres_principales
    }
    return pd.DataFrame(data)

# Fonction pour calculer le coût total
def calculate_total_cost(df):
    total_cost = (df['COUT_MATIERE'] * df['QUANTITE_MATIERE']).sum()
    return total_cost

# Interface utilisateur avec Streamlit
def main():

    # --- USER AUTHENTICATION ---
    names = ["Louis Vuitton", "Admin"]
    usernames = ["louisvuitton", "admin"]

    # Load hashed passwords from file
    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    # Initialisation de l'authentification avec les données des utilisateurs et les mots de passe hachés
    authenticator = st_authenticator.Authenticator()
    authenticator.add_users(names, usernames, hashed_passwords)
    authenticator.set_template("louis_vuitton_quick_costing")

    # Authentification de l'utilisateur avec cookies pour 7 jours
    auth_status, username = authenticator.authenticate_user("Login", cookie_expiry_days=7)

    if auth_status:
        st.title('Calculateur de Coût de Produit')

        st.sidebar.header('Paramètres')
        num_rows = st.sidebar.number_input('Nombre de lignes de données simulées', min_value=1, value=100)

        df = generate_data(num_rows)

        st.subheader('Données Simulées')
        st.write(df)

        st.subheader('Calcul du Coût Total')

        st.write("Entrez les informations du produit :")
        cout_input = st.number_input("Coût de la matière par gramme :", min_value=0.0, max_value=150.0)
        quantite_input = st.number_input("Quantité de matière (en grammes) :", min_value=0.0, max_value=150.0)
        type_sac_input = st.selectbox("Type de sac :", ['SLG', 'BAG'])
        matieres_principales_input = st.selectbox("Matières principales :", ['Cuir', 'Canvas'])

        if st.button('Calculer'):
            new_data = {
                'COUT_MATIERE': [cout_input],
                'QUANTITE_MATIERE': [quantite_input],
                'TYPE_SAC': [type_sac_input],
                'MATIERES_PRINCIPALES': [matieres_principales_input]
            }
            new_df = pd.DataFrame(new_data)
            st.write("Le coût total du produit est :", calculate_total_cost(new_df))
    else:
        st.error("Nom d'utilisateur ou mot de passe incorrect")

if __name__ == '__main__':
    main()
