import sqlite3
# -------------------- DATABASE --------------------
def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# -------------------- APP START --------------------
init_db()

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")
login_window.configure(bg="#e6f0ff")

tk.Label(login_window, text="Username", bg="#e6f0ff").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password", bg="#e6f0ff").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login, bg="#4da6ff", fg="white").pack(pady=10)
tk.Button(login_window, text="Sign Up", command=open_signup_window, bg="#4da6ff", fg="white").pack()

login_window.mainloop()

