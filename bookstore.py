import sqlite3
from tabulate import tabulate

#                                                   =====CREATING DATABASE=====
db = sqlite3.connect('ebookstore')
cursor = db.cursor()  

#                                                   ======CREATING FUNCTIONS=====
# Function to initialise the database/ create a table
def init_db():
    cursor.execute('''
    CREATE TABLE if NOT EXISTS books (id INTEGER PRIMARY KEY, Title TEXT NOT NULL, Author TEXT NOT NULL, Qty INTEGER)    
    ''')
    db.commit()
   
    books_qty = [
            (3001, 'A Tale of Two Cities', 'Charles Dickens', 30), 
            (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40),
            (3003, "The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25),
            (3004, "The Lkord of the Rings", "J.R.R Tolkien", 37),
            (3005, "Alice in Wonderland", "Lewis Carroll", 12),
            ]
    try:
        cursor.executemany('''INSERT INTO books(id, Title, Author, Qty)
        VALUES(?,?,?,?)''', books_qty)
    except:
        print("data already exists")
    db.commit()
    print(f"\nHere is the existing table:\n {(tabulate(books_qty))}")

# Function which allows to add a book
def add_book():
    try:
        new_id = int(input("Please enter book id: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    # checking whether this id is already taken and ofering further options
    id_list = cursor.execute('''SELECT * FROM books WHERE id = ?''', (new_id,)).fetchone()
    if id_list is not None:
        user_choice = input("This id already exists. Enter '1' to try again or '2' to exit: ")
        if user_choice != "2":
            try:
                new_id = int(input("Please enter book id: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            exit()
    new_title = input("Please enter book title: ")
    new_author = input("Please enter the author: ")
    # checking whether this book is already in the table and ofering further options
    title_list = cursor.execute('''SELECT * FROM books WHERE Title = ?''', (new_title,)).fetchone()
    author_list = cursor.execute('''SELECT * FROM books WHERE Author = ?''', (new_author,)).fetchone()
    if title_list and author_list is not None:
        user_choice = input("This book already exists. Enter '1' to add another book or '2' to exit: ")
        if user_choice != "2":
            new_title = input("Please enter book title: ")
            new_title = input("Please enter author: ")
        else:
            exit()
    try:
        new_Qty = int(input("Please enter the number of books: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
    VALUES(?,?,?,?)''', (new_id, new_title, new_author, new_Qty))
    db.commit()

# Function to update a book:
def update_book():
    try: 
        book_id = int(input("Please enter the id of the book you would like to update: "))
    except ValueError:
            print("Invalid input. Please enter a number.")
    # A menu to offer choice of what needs to be updated
    while True:
        update_choice = input("""What would you like to update? Enter:
                        'id' (to update the id)
                        'Title' (to update the title)
                        'Author' (to update the Author)
                        'Qty' (to update the quantity)
                        'quit' (to exit)
                        : """).lower()
        if update_choice == "quit":
            exit()
        elif update_choice == "id":
            try:
                updated_id = int(input("Please enter new id: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            cursor.execute('''UPDATE books SET id = ? WHERE id = ? ''', (updated_id, book_id))
            db.commit()
        elif update_choice == "title":
            updated_title = input("Please enter updated title: ")
            cursor.execute('''UPDATE books SET Title = ? WHERE id = ? ''', (updated_title, book_id))
            db.commit()
        elif update_choice == "author":
            updated_author = input("Please enter the updated Author: ")
            cursor.execute('''UPDATE books SET Author = ? WHERE id = ? ''', (updated_author, book_id))
            db.commit()
        elif update_choice == "qty":
            try:
                updated_qty = int(input("Please enter updated quantity: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''', (updated_qty, book_id))
            db.commit()
        else:
            print("Invalid input")

# Function to delete a book:
def delete_book():
    try: 
        book_id = int(input("Please enter the id of the book you would like to delete: "))
    except ValueError:
            print("Invalid input. Please enter a number.")
    # checking if the book is in the table
    book_list = cursor.execute('''SELECT * FROM books WHERE id = ?''', (book_id,)).fetchone()
    if book_list == None:
        print("The book is not in the table")
    else:
        cursor.execute('''DELETE FROM books WHERE id = ? ''', (book_id,))
        db.commit()
        
def search_books():
    # A menu to offer search by id, Title or Author
    while True:
        user_search = input("""Enter:
                        'id' (to search by id)
                        'Title' (to search by title)
                        'Author' (to search by Author)
                        'quit' (to exit)
                        : """).lower()
        if user_search == "quit":
            exit()
        elif user_search == "id":
            try: 
                book_id = int(input("Please enter the id of the book you would like to find: ")) 
            except ValueError:
                print("Invalid input. Please enter a number.")
            found_book = cursor.execute('''SELECT * from books WHERE id = ?''', (book_id, )).fetchone() 
            if found_book == None:
                print("The book is not found")
            else:
                print(f"""
                Here is the book you are looking for.
                Book id: {found_book[0]}
                Title: {found_book[1]}
                Author: {found_book[2]}
                Quantity: {found_book[3]}
                """)
        elif user_search == "author":
            book_author = input("Please enter the Author of the book you would like to find: ").capitalize()
            author_list = cursor.execute('''SELECT * FROM books WHERE Author = ?''', (book_author,)).fetchone()
            if author_list == None:
                 print("The book is not found")
            else:
                print(f"""
                Here is the book you are looking for.
                Book id: {author_list[0]}
                Title: {author_list[1]}
                Author: {author_list[2]}
                Quantity: {author_list[3]}
                """)
        elif user_search == "title":
            book_title = input("Please enter the Title of the book you would like to find: ").capitalize()
            title_list = cursor.execute('''SELECT * FROM books WHERE Title = ?''', (book_title,)).fetchone()
            if title_list == None:
                 print("The book is not found")
            else:
                print(f"""
                Here is the book you are looking for.
                Book id: {title_list[0]}
                Title: {title_list[1]}
                Author: {title_list[2]}
                Quantity: {title_list[3]}
                """)
        else:
            print("Incorrect input")

#                                                   =====MAIN BODY=====

init_db()
# creating user menu & calling functions
while True:
    user_choice = input("""What would you like to do? Enter:
                        'add' (to add a book)
                        'update' (to update a book)
                        'delete' (to delete a book)
                        'search' (to find a book)
                        'quit' (to exit)
                        : """).lower()
    if user_choice == "quit":
        print("Goodbye!")
        exit()
    elif user_choice == "add":
        add_book()
    elif user_choice == "update":
        update_book()
    elif user_choice == "delete":
        delete_book()
    elif user_choice == "search":
        search_books()
    else:
        print("Invalid input")
db.close()
