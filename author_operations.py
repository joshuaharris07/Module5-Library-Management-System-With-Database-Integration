class AuthorOperations:
    def __init__(self):
        self.author_list = {
            "Tolkien": {"name": "Tolkien", "biography": "Wrote the Hobbit and the Lord of the Rings."},
            "Sanderson": {"name": "Sanderson", "biography": "Wrote the Mistborn trilogy."},
            "Butcher": {"name": "Butcher", "biography": "Wrote The Codex Alera."},
            "Orwell": {"name": "Orwell", "biography": "Wrote 1984."}
        }

    def add_author(self):
        while True:
            author_name = input("Please enter the author's name: ").title()
            if author_name.strip() == "":
                print("No name was entered. Returning to the menu.")
                break
            if author_name in self.author_list:
                print("That author is already in the system. Returning to the menu.")
                break
            biography = input("Please enter the biography or details you want to note about this author: ")
            if biography.strip() == "":
                print("No information was entered. Returning to the menu.")
                break
            else:
                self.author_list[author_name] = {"name": author_name, "biography": biography}
                print(f"{author_name} has been added to the library system. Returning to the menu.")
                break

    def view_author_details(self, author_name):
        if author_name in self.author_list:
            print(f"Name: {self.author_list[author_name]["name"]}\nBiography: {self.author_list[author_name]["biography"]}") 
        else:
            print(f"{author_name} is not in our library system. Returning to the menu.")

    def view_all_authors(self):
        for details in self.author_list.values():
            print(f"Author: {details["name"]}. Biography: {details["biography"]}")