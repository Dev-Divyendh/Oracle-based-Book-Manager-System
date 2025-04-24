import customtkinter as ctk
from toast import show_toast


def update_status_window(master, cursor, connection):
    # Clear previous content
    for widget in master.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(frame, text="Enter ISBN:").pack(pady=5)
    isbn_entry = ctk.CTkEntry(frame, width=400)
    isbn_entry.pack()

    ctk.CTkLabel(frame, text="Enter Copy#:").pack(pady=5)
    copy_entry = ctk.CTkEntry(frame, width=400)
    copy_entry.pack()

    ctk.CTkLabel(frame, text="New Status (Available / Checked out / Damaged):").pack(pady=5)
    status_entry = ctk.CTkEntry(frame, width=400)
    status_entry.pack()

    result_label = ctk.CTkLabel(frame, text="")
    result_label.pack(pady=10)

    def update_status():
        isbn = isbn_entry.get().strip()
        copy_num = copy_entry.get().strip()
        new_status = status_entry.get().strip().capitalize()

        if not isbn or not copy_num or not new_status:
            show_toast(master, "⚠️ Please fill in all fields.", color="orange")
            return

        try:
            copy_num = int(copy_num)
            valid_statuses = ["Available", "Checked out", "Damaged"]
            if new_status not in valid_statuses:
                show_toast(master, f"❌ '{new_status}' is not a valid status.", color="#b22222")
                return

            cursor.execute("SELECT Status FROM Book_Copies WHERE ISBN = :1 AND Copy# = :2", (isbn, copy_num))
            row = cursor.fetchone()

            if not row:
                show_toast(master, "❌ Book copy not found.", color="#b22222")
                return

            current_status = row[0]
            if current_status == "Damaged" and new_status == "Available":
                show_toast(master, "❌ Cannot update a Damaged copy to Available.", color="#b22222")
                return

            cursor.execute("UPDATE Book_Copies SET Status = :1 WHERE ISBN = :2 AND Copy# = :3", (new_status, isbn, copy_num))
            connection.commit()

            result_label.configure(text=f"✅ Copy {copy_num} of ISBN {isbn} updated to '{new_status}'")
            show_toast(master, f"✅ Status updated to '{new_status}'")

        except ValueError:
            show_toast(master, "❌ Copy# must be an integer.", color="#b22222")
        except Exception as e:
            show_toast(master, f"❌ {str(e)}", color="#b22222")

    ctk.CTkButton(frame, text="Update Status", command=update_status).pack(pady=15)