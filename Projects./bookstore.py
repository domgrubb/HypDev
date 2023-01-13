## Importing libraries, switching to current directory ##
import os
import sys
import sqlite3
os.chdir(sys.path[0])

## Creating initial database, creating and populating initial table ##
db = sqlite3.connect('ebookstore')
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY,
Title TEXT, 
Author TEXT, 
Qty INTEGER)''')
db.commit()

## Creating list of tuples to push into table ##
shelf = [(3001,'A Tale of Two Cities','Charles Dickens',30),
(3002,'Harry Potter and the Philosopher\'s Stone','JK Rowling',40),
(3003,'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
(3004,'The Lord of the Rings','J. R. R. Tolkien', 37), 
(3005,'Alice in Wonderland', 'Lewis Carroll', 12)]

cursor.executemany('''
INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''',
shelf)
db.commit()

## Writing functions for user to call later ##
def enter_book():
    '''Prompts user to enter details for book, calls cursor execute to add to table'''
    num = input('Please enter the ID of the book: ')
    title = input('Please enter the title of the book: ')
    author = input('Please enter the author of the book: ')
    qty = input('Please enter the quantity of books: ')

    cursor.execute('''INSERT INTO books(id, Title, Author, Qty)
    VALUES(?,?,?,?)''', (num,title,author,qty))
    db.commit()
    print('Book entered successfully')

def update_book():
    '''Prompts user for ID to identify book to update, then following details'''
    num = input('Please input the ID number of the book to update: ')
    title = input('Please enter the title of the book: ')
    author = input('Please enter the author of the book: ')
    qty = input('Please enter the quantity of books: ')

    cursor.execute('''UPDATE books SET Title = ?, 
    Author = ?, 
    Qty = ?
    WHERE id = ?''', (title,author,qty,num))
    db.commit()
    print('Book updated successfully')

def delete_book():
    '''Prompts user for ID to identify book to delete then deletes from database'''
    num = (input('Please enter the ID of the book to remove: '))

    cursor.execute('''DELETE FROM books WHERE id = ?''', (num,))
    db.commit()
    print('Book removed successfully')

def search_book():
    '''Prompt the user for information to search the database with, retrieves matches'''
    form = int(input('Do you wish to search by ID (1), Title (2) or Author (3)? '))

    if form == 1:
        num = input('Please enter the title you wish to search for: ')
        cursor.execute('''SELECT * FROM books WHERE id = ?''', (num,))
        book = cursor.fetchone()
        print(book)

    elif form == 2:
        title = input('Please enter the title you wish to search for: ')
        result = int(input('One result (1) or multiple (2)? '))
        cursor.execute('''SELECT * FROM books WHERE Title = ?''', (title,))
        if result == 1:
            book = cursor.fetchone()
        else:
            book = cursor.fetchall()
        print(book)

    elif form == 3: 
        author = input('Please enter the name of the author you wish to search for: ')
        cursor.execute('''SELECT * FROM books WHERE Author = ?''', (author,))
        book = cursor.fetchone()
        print(book)

    else:
        print('Invalid input given')

## Looping code for user to edit database ##
choice = 0
while choice != 'e':
    choice = input('''Welcome to the book database! Please select an option:
    "a" - add book,
    "u" - update book,
    "d" - delete book,
    "s" - search books,
    "e" - exit database
    ''')

    if choice == 'a':
        enter_book()

    elif choice == 'u':
        update_book()

    elif choice == 'd':
        delete_book()

    elif choice == 's':
        search_book()

    elif choice == 'e':
        continue

    else:
        print('Invalid character entered, please try again.')

print('Thank you for using the database, goodbye.')
