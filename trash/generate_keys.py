import pickle
from pathlib import Path 
from streamlit_authenticator.utilities.hasher import Hasher

names = ["Louis Vuitton", "Admin"]
usernames = ['louisvuitton', 'admin']
passwords = ['lv123', 'admin123']

hashed_passwords = Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
