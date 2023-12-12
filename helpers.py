import sqlite3

# Файл для создания базы данных

def create_entries_table():
    with sqlite3.connect('vault.db') as connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        predict TEXT NOT NULL,
        image TEXT NOT NULL
        )
        """)
        cursor.close()
        connection.commit()


if __name__ == "__main__":
    create_entries_table()
