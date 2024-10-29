from connect_mysql import connect_database
import random

class UserOperations:
    def add_user(self, name):
        while True:  
            library_id_generator = [str(random.randint(0, 9)) for _ in range(7)]   # If additional numbers are needed, increase the range.
            library_id = "".join(library_id_generator)

            conn = connect_database()
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    cursor.execute(f"SELECT id from Users WHERE library_id = '{library_id}'")
                    if cursor.fetchone() == None:   # This verifies that the library_id is not already in use in the database.
                        query = "INSERT INTO Users (name, library_id) VALUE (%s, %s)"
                        add_user = (name, library_id)
                        cursor.execute(query, add_user)
                        conn.commit()
                        print(f"Welcome, {name}. Your account has been created. Your Library ID is: {library_id}\nReturning to the main menu.")
                        break

                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    cursor.close()
                    conn.close()


    def view_user(self, library_id): 
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)
                cursor.execute(f"SELECT name from Users WHERE library_id = '{library_id}'")                
                if cursor.fetchone() == None:
                    print("That library ID was not found in the system. Returning to the menu.")
                else:
                    cursor.execute(f"SELECT id, name from Users WHERE library_id = '{library_id}'")  # This returns the user_name and their ID for tracing to the borrowed_books table.
                    for user in cursor.fetchall():
                        (user_id, user_name) = user
                        print(f"{library_id} is assigned to {user_name}.")
                        cursor.execute(f"SELECT book_id from borrowed_books WHERE user_id = {user_id}")     # Confirms that the user has books currently checked out.     
                        if cursor.fetchone() == None:
                            print(f"{user_name} doesn't have any books checked out currently.")
                        else:
                            print(f"{user_name} has the following books checked out:")
                            cursor.execute(f"SELECT book_id from borrowed_books WHERE user_id = {user_id}")    # This returns the book_ids that arte currently checked out by the user.
                            for borrowed_book in cursor.fetchall(): 
                                (book_id, ) = borrowed_book
                                cursor.execute(f"SELECT title from books WHERE id = {book_id}")     # Returns the titles of the books that are currently checked out.
                                for book in cursor.fetchall():
                                    (title, ) = book
                                    print(title)
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def view_all_users(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Users")
                for user in cursor.fetchall():
                    (user_id, user_name, library_id) = user
                    print(f"User: {user_name}. Library ID: {library_id}")
                    
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()
