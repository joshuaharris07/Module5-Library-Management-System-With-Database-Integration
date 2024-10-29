import mysql.connector
from mysql.connector import Error

def connect_database():
    #   Open connection to the MySQL database
    db_name = "library_management_system"
    user = "CodingTemple"
    password = "C0dingT3mple!"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
    
        return conn

    except Error as e: 
        print(f"Error: {e}")
        return None