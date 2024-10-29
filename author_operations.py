from connect_mysql import connect_database

class AuthorOperations:
    def add_author(self, author_name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * from Authors WHERE name = '{author_name}'")
                if cursor.fetchone() == None:   # Verifies that the author isn't already in the database.
                    biography = input("Please enter the biography or details you want to note about this author: ")
                    
                    query = "INSERT INTO Authors (name, biography) VALUE (%s, %s)"
                    add_user = (author_name, biography)
                    cursor.execute(query, add_user)
                    conn.commit()

                    print(f"{author_name} has been added to the library system.")
                else:
                    print(f"{author_name} is already in the system.\nReturning to the main menu.")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def view_author_details(self, author_name):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor(buffered=True)     # Uses a buffered cursor to avoid an error if more than one row is selected by cursor.fetchone()
                cursor.execute(f"SELECT * from Authors WHERE name LIKE '%{author_name}%'")                
                if cursor.fetchone() == None:
                    print("No authors found in the system matching that search. Returning to the menu.")
                else:
                    cursor.execute(f"""SELECT id, name, biography
                    FROM Authors
                    WHERE name LIKE '%{author_name}%'
                    """)  
                    for author in cursor.fetchall():
                        (author_id, author_name, biography) = author
                        print(f"\nAuthor: {author_name}\nBiography: {biography}, {author_id}")
                        cursor.execute(f"SELECT title from Books WHERE author_id = {author_id}")                
                        if cursor.fetchone() == None:
                            print("No books in our library have been written by that author.")
                        else:
                            print(f"{author_name} has written the following books that are in our library:")
                            cursor.execute(f"SELECT title from Books WHERE author_id = {author_id}")    
                            for book in cursor.fetchall(): 
                                (title, ) = book
                                print(title)           
                                          
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()


    def view_all_authors(self):
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Authors")
                for author in cursor.fetchall():
                    (author_id, author_name, biography) = author
                    print(f"\nAuthor: {author_name}\nBiography: {biography}")
                    
            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()
                conn.close()