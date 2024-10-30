# Module5-Library-Management-System-With-Database-Integration

This project takes Python and uses it to manage a library database out of MySQL. Included in the connect_mysql.py are a user with password that I created to allow access to SELECT and INSERT, in accordance with the operations I already have included in this code. 

The program is navigated through a series of menus that are operated by entering an integer:

    Main Menu
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

Your selection will take you to one of the following menus.

    Book Operations:
    1. Add a new book
    2. Borrow a book
    3. Return a book
    4. Search for a book
    5. Display all books   

To add a new book, the program will ask for the title of the book, the author's name, the ISBN, and the publication date. The title and author's name's are marked as title case to keep everything normalized. For the author's name, the program will link the book to the author if the author is already in the database. If the author isn't, the system will ask for a biography or notes on the author and add the author to the database. The publication date uses regex to ensure proper formatting of the date so that MySQL will accept it.

Borrowing a book will request the book name and library ID of the user borrowing the book. Successful completion of this task will mark the book as unavailable in the Book table in MySQL and will generate data that will be added to the borrowed_books table. The data will include today's date as the check-out date and will add a return-date for 3 weeks in the future.

Returning a book only requests the book's title. This will search the books table to ensure it is currently checked out, will mark it as being available, and will delete the corresponding row from the borrowed_books table.

Searching for a book will take any information entered (all or part of the title) and pull up all of the information on the books it finds. This will include if the book is currently checked out or not.

Displaying all books will do the same, just in a condensed format, for all of the books in the books table.
 
    User Operations:
    1. Add a new user
    2. View user details
    3. Display all users

Adding a new user prompts to input the name of the individual to add as a user. The program then randomly generates a 7-digit library ID that is associated with the name.

Viewing user details asks for the library ID of the user you want to see. It pulls up the name associated with it as well as any books they currently have checked out.

Display all users pulls up all users and displays their names and library IDs.
    
    Author Operations:
    1. Add a new author
    2. View author detais
    3. Display all authors

Adding a new author asks for the author's name and biography/notes about the author.

Viewing author details will take all or part of an author's name and search through the author table in MySQL. It will return any matches with the author's name, biography, and books they have written that are in the books table.

Display all authors will do the same as viewing author details, but with every author in the author table.
