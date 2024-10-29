import author_operations as author_ops
import book_operations as book_ops
import user_operations as user_ops

print("Welcome to the Library Management System!")
book_operations = book_ops.BookOperations() 
user_operations = user_ops.UserOperations()
author_operations = author_ops.AuthorOperations()

while True:
    menu_action = input("""\nMain Menu:\n
1. Book Operations
2. User Operations
3. Author Operations
4. Quit\n""")
    if menu_action == "1":
        menu_action = input("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n")
        if menu_action == "1": 
            book_operations.add_book()
        elif menu_action == "2":
            title = input("Enter the title of the book you wish to check out: ").title()
            library_id = input("Please enter your library ID: ").strip()
            book_operations.borrow_book(title, library_id)
        elif menu_action == "3":
            title = input("Enter the title of the book you wish to return: ").title()
            book_operations.return_book(title)
        elif menu_action == "4":
            title = input("Enter the title of the book (or part of the title) you wish to look for: ").title()
            book_operations.search_book(title)
        elif menu_action == "5":
            book_operations.display_all_books()
    elif menu_action == "2":
        menu_action = input("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users\n")
        if menu_action == "1": 
            name = input("Please put in your full name: ").title()
            if name.strip() == "":
                print("No name was entered.")
            else:
                user_operations.add_user(name)
        elif menu_action == "2":
            library_id = input("Please enter your library ID: ").strip()
            user_operations.view_user(library_id)
        elif menu_action == "3":
            user_operations.view_all_users()
    elif menu_action == "3":
        menu_action = input("\nAuthor Operations:\n1. Add a new author\n2. View author detais\n3. Display all authors\n")
        if menu_action == "1": 
            author_operations.add_author()
        elif menu_action == "2":
            author_name = input("Please enter the author's name to search for: ").title()
            author_operations.view_author_details(author_name)
        elif menu_action == "3":
            author_operations.view_all_authors()
    elif menu_action == "4":
        print("\nThank you for using the library management system. Have a good day!")
        break
    else:
        print("\nPlease make a selection by entering an integer.")