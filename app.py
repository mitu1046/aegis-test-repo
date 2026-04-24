import sqlite3

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def search_users(search_term):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name LIKE ?', (f'%{search_term}%',))
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    print(get_user("admin"))
    print(search_users("john"))