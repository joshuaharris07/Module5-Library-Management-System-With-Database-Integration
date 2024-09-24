class BookOperations:
    def __init__(self):
        self.books = {
            "Lord Of The Rings": {"title": "Lord Of The Rings", "author": "Tolkien", "genre": "Fantasy", "publication year": 1954, "availability": True},
            "Mistborn": {"title": "Mistborn", "author": "Sanderson", "genre": "Fantasy", "publication year": 2006, "availability": False},
            "The Codex Alera": {"title": "The Codex Alera", "author": "Butcher", "genre": "Fantasy", "publication year": 2004, "availability": False},
            "1984": {"title": "1984", "author": "Orwell", "genre": "Fiction", "publication year": 2004, "availability": True}
            }
    
    def add_book(self):
        while True:
            title = input("Enter the title of the book: ").title()
            if title.strip() == "":
                print("No book title was entered. Returning to the main menu.")
                break
            if title in self.books:
                print("That book is already in the library. Returning to the menu.")
            author = input("Enter the author's last name: ").title()
            if author.strip() == "":
                print("No author was entered. Returning to the main menu.")
                break
            genre = input("Enter the genre of the book: ").title()
            if genre.strip() == "":
                print("No genre was entered. Returning to the main menu.")
                break
            try: 
                publication_year = int(input("Enter the year the book was published: "))  
            except: 
                print("Invalid publication year. Returning to the menu.")
                break
            self.books[title] = {"title": title, "author": author, "genre": genre, "publication year": publication_year, "availability": True}
            print(f"{title} was successfully added to the system.")
            break

    def borrow_book(self, title, library_id, user_operations):
        if title in self.books and self.books[title]["availability"]:
            if library_id in user_operations.users: 
                user_operations.borrow_book(library_id, title)
                print(f"You have checked {title} out. Returning to the menu")
                self.books[title]["availability"] = False
            else:
                print("Library ID is invalid.")
        elif title in self.books:
            print(f"{title} is already checked out and is not currently available.")
        else:
            print(f"{title} is not currently in our library system. Returning to the menu.")

    def return_book(self, title, user_operations):
        if title in self.books and not self.books[title]["availability"]:
            self.books[title]["availability"] = True
            for details in user_operations.users.values():
                if title in details["borrowed books"]:
                    details["borrowed books"].remove(title)
                    print(f"{title} has been successfully returned. Returning to the menu.")
        elif title in self.books:
            print(f"That book wasn't checked out yet! Returning to the menu.")
        else:
            print(f"{title} was not found in the library's system. Returning to the menu.")

    def search_book(self, title):
        if title in self.books:
            print("Currently available for checkout.") if self.books[title]["availability"] else print("This book is currently checked out.")
            print(f"{title}, Author {self.books[title]["author"]}, Genre {self.books[title]["genre"]}, Publication Year: {self.books[title]["publication year"]}")
        else:
            print(f"{title} is not currently in our library.")

    def display_all_books(self):
        available_books = []
        not_available_books = []
        for book in self.books.values():
            available_books.append(book) if book["availability"] else not_available_books.append(book)
        print("\nCurrently available books:")
        for book in available_books:
            print(f"{book["title"]}, Author: {book["author"]}, Genre: {book["genre"]}, Publication Year: {book["publication year"]}")
        print("\nBooks that are currently checked out:")
        for book in not_available_books:
            print(f"{book["title"]}, Author: {book["author"]}, Genre: {book["genre"]}, Publication Year: {book["publication year"]}")