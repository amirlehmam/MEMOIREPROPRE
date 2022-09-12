import streamlit_authenticator as stauth

import database as db

usernames = ["AL", "SG", "JF"]
names = ["Amir Lehmam", "Sachith Galbokka", "Jim Fredrickson"]
passwords = ["azerty94", "azerty75", "azerty99"]
hashed_passwords = stauth.Hasher(passwords).generate()

for (username, name, hash_password) in zip(usernames, names, hashed_passwords):
    db.insert_user(username, name, hash_password)