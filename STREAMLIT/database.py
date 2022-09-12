from deta import Deta

# 1) key database

DETA_KEY = "a0682mg1_xJhrfdvkPyhYjNjEvu33YYKCwkVuvFxa"

# 2) initialize with a project key
deta = Deta(DETA_KEY)

# 3) create and use as many DBs as you want!
db = deta.Base("users_db")

def insert_user(username, name, password):
    return db.put({"key": username, "name": name, "password": password})

def fetch_all_users():
    res = db.fetch()
    return res.items

def get_user(username):
    return db.get(username)

def update_user(username, updates):
    return db.update(username, updates)

def delete_user(username):
    return db.delete(username)