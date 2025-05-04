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

# -------------------- INVENTORY DASHBOARD --------------------
def open_inventory_window():
    def add_item():
        try:
            name = name_entry.get()
            category = category_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            if not name:
                raise ValueError("Item name required")
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO inventory (name, category, quantity, price) VALUES (?, ?, ?, ?)",
                           (name, category, quantity, price))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Item added")
            clear_fields()
            load_items()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_item():
        try:
            selected = tree.selection()
            if not selected:
                raise ValueError("No item selected")
            item_id = tree.item(selected[0])['values'][0]
            name = name_entry.get()
            category = category_entry.get()
            quantity = int(quantity_entry.get())
            price = float(price_entry.get())
            conn = sqlite3.connect('inventory.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE inventory SET name=?, category=?, quantity=?, price=? WHERE id=?",
                           (name, category, quantity, price, item_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Updated", "Item updated")
            clear_fields()
            load_items()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_item():
        try:
            selected = tree.selection()
            if not selected:
                raise ValueError("No item selected")
            item_id = tree.item(selected[0])['values'][0]
            if messagebox.askyesno("Confirm", "Delete selected item?"):
                conn = sqlite3.connect('inventory.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM inventory WHERE id=?", (item_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Deleted", "Item deleted")
                clear_fields()
                load_items()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def order_item():
        try:
            selected = tree.selection()
            if not selected:
                raise ValueError("No item selected.")

            item = tree.item(selected[0])['values']
            item_id, name, category, current_qty, price = item

            order_win = tk.Toplevel(app)
            order_win.title("Place Order")
            order_win.geometry("300x200")
            order_win.configure(bg="#e6f0ff")

            tk.Label(order_win, text=f"Ordering: {name}", bg="#e6f0ff").pack(pady=5)
            tk.Label(order_win, text="Enter quantity:", bg="#e6f0ff").pack()
            qty_entry = tk.Entry(order_win)
            qty_entry.pack()

            def confirm_order():
                try:
                    order_qty = int(qty_entry.get())
                    if order_qty <= 0:
                        raise ValueError("Quantity must be positive.")
                    if order_qty > current_qty:
                        raise ValueError("Not enough stock available.")

                    new_qty = current_qty - order_qty
                    conn = sqlite3.connect('inventory.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE inventory SET quantity=? WHERE id=?", (new_qty, item_id))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Order Placed", f"You ordered {order_qty} of {name}")
                    order_win.destroy()
                    load_items()
                except Exception as e:
                    messagebox.showerror("Order Error", str(e))

            tk.Button(order_win, text="Place Order", command=confirm_order, bg="#4da6ff", fg="white").pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def restock_item():
        try:
            selected = tree.selection()
            if not selected:
                raise ValueError("No item selected.")

            item = tree.item(selected[0])['values']
            item_id, name, category, current_qty, price = item

            restock_win = tk.Toplevel(app)
            restock_win.title("Restock Item")
            restock_win.geometry("300x200")
            restock_win.configure(bg="#e6f0ff")

            tk.Label(restock_win, text=f"Restocking: {name}", bg="#e6f0ff").pack(pady=5)
            tk.Label(restock_win, text="Enter quantity to add:", bg="#e6f0ff").pack()
            qty_entry = tk.Entry(restock_win)
            qty_entry.pack()

            def confirm_restock():
                try:
                    add_qty = int(qty_entry.get())
                    if add_qty <= 0:
                        raise ValueError("Quantity must be positive.")

                    new_qty = current_qty + add_qty
                    conn = sqlite3.connect('inventory.db')
                    cursor = conn.cursor()
                    cursor.execute("UPDATE inventory SET quantity=? WHERE id=?", (new_qty, item_id))
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Restocked", f"{add_qty} units added to {name}")
                    restock_win.destroy()
                    load_items()
                except Exception as e:
                    messagebox.showerror("Restock Error",
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
