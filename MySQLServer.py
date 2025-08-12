import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server (Change credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Add your MySQL root password if any
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
