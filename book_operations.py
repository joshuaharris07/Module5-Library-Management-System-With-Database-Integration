from connect_mysql import connect_database
from datetime import date, timedelta
import author_operations as author_ops
import re

author_operations = author_ops.AuthorOperations()   # Calling this class in order to allow a new author to be easily created while using the add_book function.

class BookOperations:    
    def add_book(self):
        while True:
            title = input("Enter the title of the book: ").title()
            if title.strip() == "":
                print("No book title was entered. Returning to the main menu.")
                break
            author_name = input("Enter the author's name: ").title()
            if author_name.strip() == "":
                print("No author was entered. Returning to the main menu.")
                break

            conn = connect_database()   # Confirming author is in the database.
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT id from Authors WHERE name = '{author_name}'")
                    if cursor.fetchone() == None:                       
                        print(f"{author_name} is not yet in the system.")
                        author_operations.add_author(author_name)
                        conn = connect_database()
                        if conn is not None:
                            try:
                                cursor = conn.cursor()
                                cursor.execute(f"SELECT id from Authors WHERE name = '{author_name}'")
                            except Exception as e:
                                print(f"Error: {e}")
                    else: 
                        cursor.execute(f"SELECT id from Authors WHERE name = '{author_name}'")
                    for author in cursor.fetchall():
                        (author_id, ) = author  # Pulls the id from Authors table in SQL
                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()
                    conn.close()

            while True:
                isbn = input("Enter the ISBN of the book: ") 
                if isbn.strip() == "":
                    print("No ISBN was entered.")
                else:
                    break

            while True:
                publication_date = input("Enter the date the book was published in this format: YYYY-MM-DD: ") 
                if not re.match(r"\d{4}-\d{2}-\d{2}$", publication_date):
                    print("Invalid format, please enter it as YYYY-MM-DD")
                else:
                    break
                
            conn = connect_database() 
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    query = f"""
                    INSERT INTO Books (title, author_id, isbn, publication_date)
                    VALUES ('{title}', '{author_id}', '{isbn}', '{publication_date}');
                    """
                    cursor.execute(query)
                    conn.commit()

                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()
                    conn.close()           
            print(f"{title} was successfully added to the system.")
            break


    def borrow_book(self, title, library_id):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT id, availability from Books WHERE title = '{title}'")
                for book in cursor.fetchall():
                    (book_id, availability) = book
                find_library_id = (library_id, )
                query = "SELECT id, name from Users WHERE library_id = %s"
                cursor.execute(query, find_library_id)
                for user in cursor.fetchall():
                    (user_id, user_name) = user

                if availability == 1:
                    cursor.execute(f"""
                    UPDATE books 
                    SET availability = '0'
                    WHERE id = {book_id}
                    """)
                    conn.commit()
            
                    query = ("""
                    INSERT INTO Borrowed_books (user_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)
                    """)
                    return_date = date.today() + timedelta(weeks=3)
                    borrow_book = (user_id, book_id, date.today(), return_date)
                    cursor.execute(query, borrow_book)
                    conn.commit()
                    print(f"{user_name} has checked out {title}. The due date is {return_date}")

                elif availability == 0:
                    cursor.execute(f"SELECT return_date FROM borrowed_books WHERE book_id = {book_id}")
                    for book in cursor.fetchall():
                        (return_date, ) = book
                    print(f"{title} is not currently available. It should be returned by {return_date}") #TODO list when it should be available

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def return_book(self, title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT id, availability from Books WHERE title = '{title}'")
                for book in cursor.fetchall():
                    (book_id, availability) = book

                if availability != 1:
                    cursor.execute(f"""
                    UPDATE Books 
                    SET availability = '1'
                    WHERE id = {book_id}
                    """)
                    conn.commit()
                    
                    cursor.execute(f"""
                    DELETE FROM Borrowed_books
                    WHERE book_id = {book_id}               
                    """)
                    conn.commit()

                    print(f"{title} has been returned.")
                
                else:
                    print(f"{title} was not previously checked out.")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def search_book(self, title):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)     # Uses a buffered cursor to avoid an error if more than one row is selected by cursor.fetchone()
                cursor.execute(f"SELECT * from Books WHERE title LIKE '%{title}%'")                
                if cursor.fetchone() == None:
                    print("No books were found in the system matching that search. Returning to the menu.")
                else:
                    cursor.execute(f"""
                    SELECT b.title AS Title, a.name AS Author, b.isbn AS ISBN, b.publication_date, b.availability
                    FROM Books b, Authors a
                    WHERE b.author_id = a.id AND b.title LIKE '%{title}%';
                    """)
                    for book in cursor.fetchall():
                        (title, author_name, ISBN, publication_date, availability) = book
                        if availability == 1:
                            print(f"\nTitle: {title}\nAuthor: {author_name}\nISBN: {ISBN}\nPublication Date: {publication_date}\n{title} is currently available for checkout.")
                        else:
                            print(f"\nTitle: {title}\nAuthor: {author_name}\nISBN: {ISBN}\nPublication Date: {publication_date}\n{title} is not currently available for checkout.")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def display_all_books(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("""
                SELECT b.title AS Title, a.name AS Author, b.isbn AS ISBN, b.publication_date, b.availability
                FROM Books b, Authors a
                WHERE b.author_id = a.id;
                """)
                for book in cursor.fetchall():
                    (title, author_name, ISBN, publication_date, availability) = book
                    if availability == 1:
                        print(f"\nTitle: {title}, Author: {author_name}, ISBN: {ISBN}, Publication Date: {publication_date}. Currently available.")
                    else:
                        print(f"\nTitle: {title}, Author: {author_name}, ISBN: {ISBN}, Publication Date: {publication_date}. Not available.")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()
