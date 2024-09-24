import random

class UserOperations:
    def __init__(self):
        self.users = {
            "1234567": {"library id": "1234567", "name": "John Doe", "borrowed books": []},
            "7777777": {"library id": "7777777", "name": "Moby Dog", "borrowed books": ["Mistborn", "The Codex Alera"]}
        }
    
    def add_user(self, name):
        while True:  
            library_id_generator = [str(random.randint(0, 9)) for _ in range(7)]   # If additional numbers are needed, increase the range.
            library_id = "".join(library_id_generator)
            if library_id not in self.users: 
                break
        self.users[library_id] = {"library id": library_id, "name": name, "borrowed books": []}
        print(f"New user: {name} has been assigned the following library ID: {library_id}")

    def borrow_book(self, library_id, title):
        self.users[library_id]["borrowed books"].append(title)

    def view_user(self, library_id): 
        if library_id in self.users:
            print(f"Name: {self.users[library_id]["name"]}. Currently borrowing: {", ".join(self.users[library_id]["borrowed books"])}")
        else:
            print("That library ID was not found in the system. Returning to the menu.")

    def view_all_users(self):
        for details in self.users.values():
            print(f"Library ID: {details["library id"]}, Name: {details["name"]}, Borrowed Books: {", ".join(details["borrowed books"])}")
