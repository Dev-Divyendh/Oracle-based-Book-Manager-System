import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from toast import show_toast

def search_books_window(master, cursor):
    # Clear any existing content in the right panel
    for widget in master.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(frame, text="Enter search keyword:").pack(pady=5)
    keyword_entry = ctk.CTkEntry(frame, width=400)
    keyword_entry.pack(pady=5)

    ctk.CTkLabel(frame, text="Search by:").pack()
    search_by = ttk.Combobox(frame, values=["ISBN", "Title", "Category"], state="readonly")
    search_by.current(0)
    search_by.pack(pady=5)

    result_tree = ttk.Treeview(frame, columns=("ISBN", "Title", "Edition", "Category", "Price"), show='headings')
    for col in result_tree["columns"]:
        result_tree.heading(col, text=col)
        result_tree.column(col, width=100)
    result_tree.pack(pady=10, fill="both", expand=True)

    def search():
        keyword = keyword_entry.get()
        column = search_by.get()
        if not keyword:
            show_toast(master, "⚠️ Please enter a search keyword.", color="orange")
            return

        try:
            if column in ["Title", "Category"]:
                query = f"SELECT * FROM Books WHERE LOWER({column}) LIKE :1"
                cursor.execute(query, (f"%{keyword.lower()}%",))
            else:
                query = f"SELECT * FROM Books WHERE {column} = :1"
                cursor.execute(query, (keyword,))

            rows = cursor.fetchall()
            for row in result_tree.get_children():
                result_tree.delete(row)

            if rows:
                for row in rows:
                    result_tree.insert('', "end", values=row)
                show_toast(master, f"✅ Found {len(rows)} result(s)")
            else:
                show_toast(master, "No matching books found.", color="orange")
        except Exception as e:
            show_toast(master, f"❌ {str(e)}", color="#b22222")

    ctk.CTkButton(frame, text="Search", command=search).pack(pady=5)
