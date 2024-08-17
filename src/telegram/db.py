import sqlite3

def with_connection(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect("C:/Users/Nazar/Desktop/workdir/keysystem/keys.db")
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
        SET activated = 1, activated_by = ?
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
        SELECT EXISTS(SELECT 1 FROM keys WHERE key = ? AND activated = ?)
        """, (key_value, True)  # Здесь True означает, что мы ищем активированные ключи
    )
    result = cursor.fetchone()
    return bool(result[0])

# You can test your methods here
if __name__ == "__main__":
    print(select_key("UCFP9Z0OZGWAD75XTSRXN211"))
