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
                    if cursor.fetchone() == None:
                        print(f"{library_id} is not yet in use.")
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
                cursor = conn.cursor()
                cursor.execute(f"SELECT name from Users WHERE library_id = '{library_id}'")                
                if cursor.fetchone() == None:
                    print("That library ID was not found in the system. Returning to the menu.")
                else:
                    cursor.execute(f"SELECT name from Users WHERE library_id = '{library_id}'")  
                    for user in cursor.fetchall():
                        (name, ) = user
                        print(f"{library_id} is assigned to {name}.")
                    
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
