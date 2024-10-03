import sqlite3

def init_db():
    conn = sqlite3.connect('mental_health.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS journal
                      (id INTEGER PRIMARY KEY, user TEXT, entry TEXT, reflection TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

def add_journal_entry(user, entry, reflection, timestamp):
    conn = sqlite3.connect('mental_health.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO journal (user, entry, reflection, timestamp) VALUES (?, ?, ?, ?)", (user, entry, reflection, timestamp))
    conn.commit()
    conn.close()

def get_journal_entries(user):
    conn = sqlite3.connect('mental_health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM journal WHERE user=?", (user,))
    entries = cursor.fetchall()
    conn.close()
    return entries
