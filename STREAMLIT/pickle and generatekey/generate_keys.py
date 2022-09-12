import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Amir Lehmam", "Sachith Galbokka", "Jim Fredrickson"]
usernames = ["AL", "SG", "JF"]
passwords = ["azerty94", "azerty75", "azerty99"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)