import customtkinter as ctk
from tkinter import ttk
from toast import show_toast


def replace_damaged_window(master, cursor, connection):
    # Clear previous content
    for widget in master.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(frame, text="Enter ISBN or partial Title:").pack(pady=5)
    keyword_entry = ctk.CTkEntry(frame, width=500)
    keyword_entry.pack(pady=5)

    # Damaged table
    ctk.CTkLabel(frame, text="Damaged Copies:").pack()
    damaged_tree = ttk.Treeview(frame, columns=("ISBN", "Copy#", "Title", "Status"), show="headings", height=8)
    for col in damaged_tree["columns"]:
        damaged_tree.heading(col, text=col)
        damaged_tree.column(col, width=150)
    damaged_tree.pack(pady=5, fill="x")

    # Newly added table
    ctk.CTkLabel(frame, text="Newly Added Copies:").pack()
    new_tree = ttk.Treeview(frame, columns=("ISBN", "Copy#", "Title", "Status"), show="headings", height=8)
    for col in new_tree["columns"]:
        new_tree.heading(col, text=col)
        new_tree.column(col, width=150)
    new_tree.pack(pady=5, fill="x")

    def find_damaged():
        keyword = keyword_entry.get().strip()
        if not keyword:
            show_toast(master, "⚠️ Please enter a keyword.", color="orange")
            return

        try:
            if keyword.replace("-", "").isdigit():
                query = """
                    SELECT bc.ISBN, bc.Copy#, b.Title, bc.Status
                    FROM Book_Copies bc
                    JOIN Books b ON bc.ISBN = b.ISBN
                    WHERE bc.ISBN = :1 AND bc.Status = 'Damaged'
                """
                cursor.execute(query, (keyword,))
            else:
                query = """
                    SELECT bc.ISBN, bc.Copy#, b.Title, bc.Status
                    FROM Book_Copies bc
                    JOIN Books b ON bc.ISBN = b.ISBN
                    WHERE LOWER(b.Title) LIKE :1 AND bc.Status = 'Damaged'
                """
                cursor.execute(query, (f"%{keyword.lower()}%",))

            damaged_books = cursor.fetchall()

            damaged_tree.delete(*damaged_tree.get_children())
            new_tree.delete(*new_tree.get_children())

            if not damaged_books:
                show_toast(master, "No damaged copies found.", color="orange")
                return

            for row in damaged_books:
                damaged_tree.insert("", "end", values=row)

            count = len(damaged_books)
            confirm = ctk.CTkInputDialog(text=f"Replace all {count} damaged copy{'ies' if count > 1 else ''}?", title="Confirm Replacement")
            user_input = confirm.get_input()

            if user_input and user_input.lower() in ["yes", "y"]:
                replaced_rows = []

                for isbn, copy_num, title, _ in damaged_books:
                    cursor.execute("DELETE FROM Book_Copies WHERE ISBN = :1 AND Copy# = :2", (isbn, copy_num))
                    cursor.execute("SELECT MAX(Copy#) FROM Book_Copies WHERE ISBN = :1", (isbn,))
                    max_copy = cursor.fetchone()[0] or 0
                    new_copy = max_copy + 1
                    cursor.execute("INSERT INTO Book_Copies (ISBN, Copy#, Status) VALUES (:1, :2, 'Available')", (isbn, new_copy))
                    replaced_rows.append((isbn, new_copy, title, 'Available'))

                connection.commit()

                for row in replaced_rows:
                    new_tree.insert("", "end", values=row)

                if keyword.replace("-", "").isdigit():
                    cursor.execute("""
                        SELECT bc.ISBN, bc.Copy#, b.Title, bc.Status
                        FROM Book_Copies bc
                        JOIN Books b ON bc.ISBN = b.ISBN
                        WHERE bc.ISBN = :1 AND bc.Status = 'Damaged'
                    """, (keyword,))
                else:
                    cursor.execute("""
                        SELECT bc.ISBN, bc.Copy#, b.Title, bc.Status
                        FROM Book_Copies bc
                        JOIN Books b ON bc.ISBN = b.ISBN
                        WHERE LOWER(b.Title) LIKE :1 AND bc.Status = 'Damaged'
                    """, (f"%{keyword.lower()}%",))

                updated_damaged = cursor.fetchall()
                damaged_tree.delete(*damaged_tree.get_children())
                for row in updated_damaged:
                    damaged_tree.insert("", "end", values=row)

                show_toast(master, f"✅ Replaced {count} damaged copy{'ies' if count > 1 else ''}.")

        except Exception as e:
            show_toast(master, f"❌ {str(e)}", color="#b22222")

    ctk.CTkButton(frame, text="Find & Replace Damaged Copies", command=find_damaged).pack(pady=10)
