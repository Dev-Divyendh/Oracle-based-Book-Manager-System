import customtkinter as ctk
from tkinter import messagebox, filedialog

from db_utils import connect_to_oracle
from sql_loader import execute_sql_file
from features.search_books import search_books_window
from features.show_available_books import show_available_window
from features.replace_damaged import replace_damaged_window
from features.update_status import update_status_window

class BookManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Manager - Oracle Login")
        self.master.geometry("1000x600")
        self.master.minsize(1000, 600)

        # Branding Header
        ctk.CTkLabel(master, text="\U0001F4DA Book Manager System", font=("Segoe UI", 20, "bold")).pack(pady=10)

        # Login Form Frame
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=20)

        ctk.CTkLabel(self.frame, text="Oracle Username:").grid(row=0, column=0, sticky='e', padx=10, pady=10)
        self.username_entry = ctk.CTkEntry(self.frame, width=200)
        self.username_entry.grid(row=0, column=1, pady=10)

        ctk.CTkLabel(self.frame, text="Oracle Password:").grid(row=1, column=0, sticky='e', padx=10, pady=10)
        self.password_entry = ctk.CTkEntry(self.frame, show="*", width=200)
        self.password_entry.grid(row=1, column=1, pady=10)

        self.login_button = ctk.CTkButton(master, text="Connect & Load SQL File", command=self.login)
        self.login_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(master, text="Status: Waiting for login...", anchor="w")
        self.status_label.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        dsn = "artemis.vsnet.gmu.edu:1521/vse18c.vsnet.gmu.edu"
        try:
            self.connection, self.cursor = connect_to_oracle(username, password, dsn)
            self.status_label.configure(text="Status: Connected to Oracle DB")
            messagebox.showinfo("Success", "Connected to Oracle DB!")
            self.load_sql_script()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))
            self.status_label.configure(text="Status: Connection failed")

    def load_sql_script(self):
        filepath = filedialog.askopenfilename(title="Select BookCopies.sql file", filetypes=[("SQL Files", "*.sql")])
        if not filepath:
            messagebox.showwarning("No File", "SQL file not selected.")
            return
        success = execute_sql_file(self.cursor, filepath)
        if success:
            self.connection.commit()
            messagebox.showinfo("Success", "SQL Script executed successfully!")
            self.status_label.configure(text="Status: SQL script executed")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "SQL script execution failed.")
            self.status_label.configure(text="Status: SQL execution failed")

    def exit_program(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            try:
                if hasattr(self, 'cursor') and self.cursor:
                    self.cursor.close()
                if hasattr(self, 'connection') and self.connection:
                    self.connection.close()
            except:
                pass
            self.master.quit()


    def show_main_menu(self):
        self.frame.destroy()
        self.login_button.destroy()

        # Layout: Sidebar + Content Area
        layout_frame = ctk.CTkFrame(self.master)
        layout_frame.pack(fill="both", expand=True)

        # Sidebar menu frame
        sidebar = ctk.CTkFrame(layout_frame, width=200)
        sidebar.pack(side="left", fill="y", padx=10, pady=10)

        self.content_frame = ctk.CTkFrame(layout_frame)
        self.content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(sidebar, text="Main Menu", font=("Segoe UI", 16, "bold")).pack(pady=10)

        ctk.CTkButton(sidebar, text="1. Search Books", command=lambda: search_books_window(self.content_frame, self.cursor)).pack(pady=5, padx=10)
        ctk.CTkButton(sidebar, text="2. Show Available Copies", command=lambda: show_available_window(self.content_frame, self.cursor)).pack(pady=5, padx=10)
        ctk.CTkButton(sidebar, text="3. Replace Damaged Copies", command=lambda: replace_damaged_window(self.content_frame, self.cursor, self.connection)).pack(pady=5, padx=10)
        ctk.CTkButton(sidebar, text="4. Update Copy Status", command=lambda: update_status_window(self.content_frame, self.cursor, self.connection)).pack(pady=5, padx=10)
        ctk.CTkButton(sidebar, text="5. Exit", command=self.exit_program).pack(pady=10, padx=10)

        self.status_label.configure(text="Status: Connected - Ready")

if __name__ == "__main__":
    import tkinter.ttk as ttk
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    # Dark coloured table
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview", background="#1e1e1e", foreground="white", fieldbackground="#1e1e1e")
    style.map("Treeview", background=[("selected", "#094771")])
    style.configure("Treeview.Heading", background="#2a2a2a", foreground="white", font=('Segoe UI', 10, 'bold'))
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # removes borders
    app = BookManagerApp(root)
    root.mainloop()
