import customtkinter as ctk
from toast import show_toast


def show_available_window(master, cursor):
    # Clear previous content
    for widget in master.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(master)
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(frame, text="Enter ISBN or partial Title:").pack(pady=10)
    keyword_entry = ctk.CTkEntry(frame, width=400)
    keyword_entry.pack(pady=5)

    result_label = ctk.CTkLabel(frame, text="")
    result_label.pack(pady=10)

    def check_availability():
        keyword = keyword_entry.get().strip()
        if not keyword:
            show_toast(master, "⚠️ Please enter a keyword.", color="orange")
            return

        try:
            if keyword.replace("-", "").isdigit():
                cursor.execute("""
                    SELECT b.Title, COUNT(bc.Copy#) 
                    FROM Books b 
                    LEFT JOIN Book_Copies bc ON b.ISBN = bc.ISBN AND bc.Status = 'Available'
                    WHERE b.ISBN = :1
                    GROUP BY b.Title
                """, (keyword,))
            else:
                cursor.execute("""
                    SELECT b.Title, COUNT(bc.Copy#)
                    FROM Books b
                    LEFT JOIN Book_Copies bc ON b.ISBN = bc.ISBN AND bc.Status = 'Available'
                    WHERE LOWER(b.Title) LIKE :1
                    GROUP BY b.Title
                """, (f"%{keyword.lower()}%",))

            results = cursor.fetchall()

            if not results:
                if keyword.replace("-", "").isdigit():
                    cursor.execute("SELECT Title FROM Books WHERE ISBN = :1", (keyword,))
                else:
                    cursor.execute("SELECT Title FROM Books WHERE LOWER(Title) LIKE :1", (f"%{keyword.lower()}%",))

                titles = cursor.fetchall()
                if titles:
                    msg = "\n".join([f"'{title[0]}': 0 available" for title in titles])
                else:
                    msg = "No matching books found."

                show_toast(master, msg, color="orange")
                result_label.configure(text=msg)
            else:
                msg = "\n".join([f"'{title}': {count} available" for title, count in results])
                show_toast(master, "✅ Availability checked.")
                result_label.configure(text=msg)

        except Exception as e:
            show_toast(master, f"❌ {str(e)}", color="#b22222")

    ctk.CTkButton(frame, text="Check", command=check_availability).pack(pady=10)