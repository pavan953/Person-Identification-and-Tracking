# import sqlite3
# from datetime import datetime

# def create_connection():
#     """
#     Establish a connection to the SQLite database.
#     """
#     return sqlite3.connect('person_database.db')

# def create_table():
#     """
#     Create the `persons` table if it does not exist.
#     """
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS persons (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             face_encoding BLOB,
#             last_recognized TEXT,
#             face_image BLOB
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def add_person(name, face_encoding, face_image):
#     """
#     Add a new person to the database.
#     """
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         INSERT INTO persons (name, face_encoding, last_recognized, face_image)
#         VALUES (?, ?, ?, ?)
#     ''', (name, face_encoding, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), face_image))
#     conn.commit()
#     conn.close()

# def update_last_recognized(name, face_image):
#     """
#     Update the `last_recognized` timestamp and `face_image` for a person.
#     """
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('''
#         UPDATE persons
#         SET last_recognized = ?, face_image = ?
#         WHERE name = ?
#     ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), face_image, name))
#     conn.commit()
#     conn.close()

# def get_all_persons():
#     """
#     Retrieve all persons from the database with their name and face encoding.
#     """
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute('SELECT name, face_encoding FROM persons')
#     persons = cursor.fetchall()
#     conn.close()
#     return persons

# def add_columns():
#     """
#     Add missing columns `last_recognized` and `face_image` if they don't exist.
#     """
#     conn = create_connection()
#     cursor = conn.cursor()
#     try:
#         # Add the `last_recognized` column
#         cursor.execute('ALTER TABLE persons ADD COLUMN last_recognized TEXT')
#     except sqlite3.OperationalError:
#         # Column already exists
#         pass

#     try:
#         # Add the `face_image` column
#         cursor.execute('ALTER TABLE persons ADD COLUMN face_image BLOB')
#     except sqlite3.OperationalError:
#         # Column already exists
#         pass

#     conn.commit()
#     conn.close()

# # Ensure the table is created with the correct schema
# create_table()

# # Ensure necessary columns are added
# add_columns()



import sqlite3
from datetime import datetime

def create_connection():
    return sqlite3.connect('person_database.db')

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            usn TEXT PRIMARY KEY,
            name TEXT,
            face_encoding BLOB,
            last_recognized TEXT,
            face_image BLOB
        )
    ''')
    conn.commit()
    conn.close()

def add_person(usn, name, face_encoding, face_image):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO persons (usn, name, face_encoding, last_recognized, face_image)
        VALUES (?, ?, ?, ?, ?)
    ''', (usn, name, face_encoding, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), face_image))
    conn.commit()
    conn.close()

def update_last_recognized(usn, face_image):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE persons
        SET last_recognized = ?, face_image = ?
        WHERE usn = ?
    ''', (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), face_image, usn))
    conn.commit()
    conn.close()

def get_all_persons():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT usn, name, face_encoding FROM persons')
    persons = cursor.fetchall()
    conn.close()
    return persons

def get_person_by_usn(usn):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM persons WHERE usn = ?', (usn,))
    person = cursor.fetchone()
    conn.close()
    return person

def create_tracking_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tracking (
            usn TEXT PRIMARY KEY,
            name TEXT,
            face_image BLOB,
            last_seen TEXT
        )
    ''')
    conn.commit()
    conn.close()

def update_tracking(usn, name, face_image):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO tracking (usn, name, face_image, last_seen)
        VALUES (?, ?, ?, ?)
    ''', (usn, name, face_image, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

create_table()
create_tracking_table()
# add_columns()