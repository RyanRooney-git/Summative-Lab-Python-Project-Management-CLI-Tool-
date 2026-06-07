import json
from models.project import Project

DATA_FILE = "data/storage.json"

class User:
    all_users = []

    def __init__(self, name, email=None):
        self.name = name
        self.email = email
        self.projects = []
        User.all_users.append(self)

    def add_project(self, project):
        self.projects.append(project)

    @classmethod
    def find(cls, name):
        for user in cls.all_users:
            if user.name == name:
                return user
        return None

    @classmethod
    def load(cls):
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for u in data.get("users", []):
                    cls(u["name"], u.get("email"))
        except FileNotFoundError:
            pass

    @classmethod
    def save(cls):
        data = {"users": [{"name": u.name, "email": u.email} for u in cls.all_users]}
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)