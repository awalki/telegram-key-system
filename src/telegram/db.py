import sqlite3
import pathlib
from pathlib import Path

db_path = Path("keys.db")

def with_connection(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(db_path)
        try:
            result = func(connection, *args, **kwargs)
            connection.commit()
            return result
        finally:
            connection.close()
    return wrapper

@with_connection
def edit_column_values(connection, key_value, user_id):
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE keys
        SET activated_by = ?
        WHERE key = ? 
        """, (user_id, key_value)
    )

@with_connection
def select_key(connection, key_value):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT EXISTS(SELECT 1 FROM keys WHERE key = ?)
        """, (key_value,)
    )
    result = cursor.fetchone()
    return bool(result[0])

@with_connection
def user_exists(connection, user_id):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT EXISTS(SELECT 1 FROM keys WHERE activated_by = ?)
        """, (user_id,)
    )
    result = cursor.fetchone()
    return bool(result[0])

@with_connection
def key_activated(connection, key_value):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT EXISTS(
            SELECT 1 FROM keys 
            WHERE key = ? AND activated_by != 0
        )
        """, (key_value,)
    )
    result = cursor.fetchone()
    return bool(result[0])


# You can test your methods here
if __name__ == "__main__":
    print(key_activated("8O7C64AFVWXGUAIJM38WGVWD"))
