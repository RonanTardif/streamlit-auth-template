import yaml
from streamlit_authenticator.utilities.hasher import Hasher

# Informations d'identification des utilisateurs avec mots de passe en clair
credentials = {
    "credentials": {
        "usernames": {
            "admin": {
                "email": "admin@gmail.com",
                "name": "Admin",
                "password": "XXX"
            },
            "louisvuitton": {
                "email": "louisvuitton@gmail.com",
                "name": "Louis Vuitton",
                "password": "XXX"
            }
        }
    },
    "cookie": {
        "expiry_days": 7,
        "key": "random_signature_key",
        "name": "random_cookie_name"
    },
    "preauthorized": {
        "emails": [
            "melsby@gmail.com"
        ]
    }
}

# Hachage des mots de passe
plain_text_passwords = [info["password"] for info in credentials["credentials"]["usernames"].values()]
hashed_passwords = Hasher(plain_text_passwords).generate()

# Remplacement des mots de passe en clair par les mots de passe hachés dans les informations d'identification
for (username, info), hashed_password in zip(credentials["credentials"]["usernames"].items(), hashed_passwords):
    info["password"] = hashed_password

# Écriture des informations d'identification dans le fichier YAML
with open("config.yaml", "w") as file:
    yaml.dump(credentials, file, default_flow_style=False)

print("Le fichier config2.yaml a été généré avec succès.")
