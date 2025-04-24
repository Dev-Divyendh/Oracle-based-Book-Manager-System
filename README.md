# 📚 Oracle Book Manager (Python GUI) — CS550 Project 2

This project is developed for **CS550 – Database Systems** (Spring 2025) at George Mason University. It is a **Python GUI application** built using `customtkinter` and `oracledb` that connects to the Oracle DB on GMU’s Artemis server. The application allows users to manage book data and perform operations like searching, updating, and replacing damaged book copies.

---

## ⚙️ Technologies Used

- Python 3.11
- `customtkinter` (themed Tkinter)
- `oracledb` (Oracle Python DB connector)
- Oracle Database (via GMU Artemis Server)
- SQL (DDL + DML scripts)

---

## 📋 Features

- 🔍 Search books by ISBN, Title, or Category (with substring matching)
- 📦 Show the number of available book copies
- 🛠️ Replace damaged book copies
- 🔄 Update status of book copies with validations
- 💬 Real-time toast messages for operations
- 📂 SQL script loader with GUI FileChooser
- 🔐 Secure login prompt for Oracle credentials

---

## 🗃️ Database Schema

### Books
| Column  | Type     |
|---------|----------|
| ISBN    | VARCHAR  |
| Title   | VARCHAR  |
| Edition | INT      |
| Category| VARCHAR  |
| Price   | NUMBER   |

### Book_Copies
| Column | Type     |
|--------|----------|
| ISBN   | VARCHAR  |
| Copy#  | INT      |
| Status | VARCHAR  |

- 🔗 `Book_Copies.ISBN` → Foreign Key referencing `Books.ISBN`

---

## 🖥️ How to Run

1. 📦 Install dependencies:
```bash
pip install customtkinter oracledb
```

2. 🚀 Launch the app:
```bash
python main.py
```

3. 👤 Enter Oracle login details when prompted

4. 📁 Select `BookCopies.sql` file using the file dialog to initialize tables

5. 🎛️ Use the GUI to interact with the database (search, update, replace, etc.)

---

## 🖼️ Screenshots

![image](https://github.com/user-attachments/assets/cc566eae-ed64-4567-be00-5c849c342f51)



---

## 📄 File Overview

```
oracle-book-manager-cs550/
├── main.py               # Entry point for the GUI app
├── db_utils.py           # Handles Oracle DB connection logic
├── sql_loader.py         # Loads BookCopies.sql to DB
├── toast.py              # Custom toast popup for messages
├── BookCopies.sql        # SQL schema and data script
├── features/             # Modular files for each CRUD operation
│   ├── search_books.py
│   ├── available_copies.py
│   ├── replace_damaged.py
│   └── update_status.py
└── README.md
```


---

## 📚 References

- [Oracle Python Quickstart](https://oracle.github.io/python-oracledb/)
- [customtkinter Documentation](https://customtkinter.tomschimansky.com/)
- [Execute SQL Script with Python](https://www.tutorialspoint.com/how-to-run-sql-script-using-jdbc)

---

## 👨‍💻 Authors

- Dev Divyendh Dhinakaran  
---

## 🏫 Course

**CS550 – Database Systems**  
George Mason University — Spring 2025
