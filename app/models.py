import os,sqlite3
from app import create_connection

def init_db(conn):
    conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL, created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)')
    conn.close()

def get_all_notes():
    conn = create_connection(os.getenv('DB_NAME','app.db'))
    cursor = conn.cursor()
    notes = cursor.execute('SELECT * FROM notes').fetchall()
    conn.commit()
    conn.close()
    return notes;

def add_notes(content):
    conn = create_connection(os.getenv('DB_NAME','app.db'))
    conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()

def delete_notes(id):
    conn = create_connection(os.getenv('DB_NAME','app.db'))
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def search_notes(query):
    conn = create_connection(os.getenv('DB_NAME','app.db'))
    notes = conn.execute('SELECT * FROM notes WHERE content LIKE %?%',(query,)).fetchmany(5)
    conn.close()
    return notes;