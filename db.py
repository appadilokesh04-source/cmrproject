import json, os, bcrypt

class Database:
    def __init__(self):
        if not os.path.exists("users.json"):
            with open("users.json", "w") as f:
                json.dump({}, f)

    def insert(self, name, email, password, user_type):
        with open("users.json", "r") as f:
            users = json.load(f)

        if email in users:
            return False

        # HASH PASSWORD HERE ✔
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        users[email] = {
            "name": name,
            "password": hashed,   # store HASHED password
            "user_type": user_type
        }

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        return True

    def search(self, email, password):
        with open("users.json", "r") as f:
            users = json.load(f)

        if email not in users:
            return False

        stored_hash = users[email]["password"].encode()
        print("DEBUG HASH:",users[email]["password"])
        stored_hash=stored_hash.encode()
        # CHECK HASH HERE ✔
        if bcrypt.checkpw(password.encode(), stored_hash):
            return users[email]["user_type"]
        else:
            return False
