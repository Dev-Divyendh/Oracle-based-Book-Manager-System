import tkinter as tk
from tkinter import filedialog, messagebox
import oracledb
import os
from tkinter import ttk

class BookManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Manager - Oracle Login")
        self.master.geometry("400x250")

        # Login Frame
        self.frame = tk.Frame(master)
        self.frame.pack(pady=20)

        tk.Label(self.frame, text="Oracle Username:").grid(row=0, column=0, sticky='e')
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Oracle Password:").grid(row=1, column=0, sticky='e')
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(master, text="Connect & Load SQL File", command=self.connect_db)
        self.login_button.pack(pady=20)

    def connect_db(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        dsn = "artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu"

        try:
            self.connection = oracledb.connect(user=username, password=password, dsn=dsn)
            self.cursor = self.connection.cursor()

            messagebox.showinfo("Success", "Connected to Oracle DB!")
            self.load_sql_script()
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed:\n{e}")

    def load_sql_script(self):
        filepath = filedialog.askopenfilename(title="Select BookCopies.sql file", filetypes=[("SQL Files", "*.sql")])
        if not filepath:
            messagebox.showwarning("No File", "SQL file not selected.")
            return

        try:
            with open(filepath, 'r') as file:
                sql_script = file.read()

            sql_commands = sql_script.split(';')
            for command in sql_commands:
                cmd = command.strip()
                if not cmd:
                    continue
                try:
                    self.cursor.execute(cmd)
                except oracledb.DatabaseError as e:
                    error_obj, = e.args
                    print(f"Skipping error: {error_obj.message}")
                    continue


            self.connection.commit()
            messagebox.showinfo("Success", "SQL Script executed successfully!")
            self.show_main_menu()
        except Exception as e:
            messagebox.showerror("Execution Error", f"Failed to execute script:\n{e}")
    def search_books_window(self):
        win = tk.Toplevel(self.master)
        win.title("Search Books")
        win.geometry("600x400")

        tk.Label(win, text="Enter search keyword:").pack(pady=5)
        keyword_entry = tk.Entry(win, width=40)
        keyword_entry.pack(pady=5)

        tk.Label(win, text="Search by:").pack()
        search_by = ttk.Combobox(win, values=["ISBN", "Title", "Category"], state="readonly")
        search_by.current(0)
        search_by.pack(pady=5)

        # Result Treeview
        result_tree = ttk.Treeview(win, columns=("ISBN", "Title", "Edition", "Category", "Price"), show='headings')
        for col in result_tree["columns"]:
            result_tree.heading(col, text=col)
            result_tree.column(col, width=100)
        result_tree.pack(pady=10, fill="both", expand=True)

        def search():
            keyword = keyword_entry.get()
            column = search_by.get()
            if not keyword:
                messagebox.showwarning("Input Required", "Please enter a search keyword.")
                return

            try:
                # Using substring matching for Title and Category
                if column in ["Title", "Category"]:
                    query = f"SELECT * FROM Books WHERE LOWER({column}) LIKE :1"
                    self.cursor.execute(query, (f"%{keyword.lower()}%",))

                else:
                    query = f"SELECT * FROM Books WHERE {column} = :1"
                    self.cursor.execute(query, (keyword,))

                rows = self.cursor.fetchall()
                # Clearing previous results
                for row in result_tree.get_children():
                    result_tree.delete(row)

                if rows:
                    for row in rows:
                        result_tree.insert('', tk.END, values=row)
                else:
                    messagebox.showinfo("No Results", "No matching books found.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Search", command=search).pack(pady=5)


    def show_main_menu(self):
        # Hide login UI
        self.frame.destroy()
        self.login_button.destroy()

        # Replace with a menu
        tk.Label(self.master, text="Main Menu", font=("Arial", 16)).pack(pady=10)
        menu_options = [
            tk.Button(self.master, text="1. Search Books", command=self.search_books_window).pack(pady=5),
            "2. Show Number of Available Copies",
            "3. Replace Damaged Copies",
            "4. Update Book Copy Status",
            "5. Exit"
        ]
        for option in menu_options:
            tk.Label(self.master, text=option).pack()

# Launch App
if __name__ == "__main__":
    root = tk.Tk()
    app = BookManagerApp(root)
    root.mainloop()
