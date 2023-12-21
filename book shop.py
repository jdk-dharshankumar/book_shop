import mysql.connector

# Replace these with your actual database credentials
db_config = {
    "host": "your_mysql_host",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "bookshop"
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Function to add a new book to the database
def add_book(title, author, price):
    query = "INSERT INTO books (title, author, price) VALUES (%s, %s, %s)"
    values = (title, author, price)
    cursor.execute(query, values)
    connection.commit()
    print("Book added successfully.")

# Function to display all books in the database
def display_books():
    query = "SELECT * FROM books"
    cursor.execute(query)
    books = cursor.fetchall()
    
    if not books:
        print("No books available.")
    else:
        print("Books in the database:")
        for book in books:
            print("ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}")

# Example usage
add_book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
add_book("To Kill a Mockingbird", "Harper Lee", 12.99)
display_books()

# Close the connection
cursor.close()
connection.close()
