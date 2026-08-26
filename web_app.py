import sqlite3


def get_user(conn: sqlite3.Connection, user_id):
    """Retrieve a user record safely using a parameterized query.

    Args:
        conn: An active SQLite connection.
        user_id: The identifier of the user to fetch. Can be any type that SQLite
                 accepts for the ``id`` column (typically int or str).

    Returns:
        The first matching row as a tuple, or ``None`` if no user matches.
    """
    cursor = conn.cursor()
    # Use a parameterized query to avoid SQL injection.
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
