# 📚 Oracle Book Manager System (Python GUI)

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
![image](https://github.com/user-attachments/assets/f705267f-806d-4f02-996e-f5fea3c5b9ad)
![image](https://github.com/user-attachments/assets/e6a7795c-a895-430d-a151-3765dfe9f295)
![image](https://github.com/user-attachments/assets/cf18b526-6aa4-45b2-b78d-f8cbe618b249)
![image](https://github.com/user-attachments/assets/9fd3a665-100e-40a4-b6ef-9655367282fa)
![image](https://github.com/user-attachments/assets/00bea691-bede-48c4-a131-4821b3113fbd)
![image](https://github.com/user-attachments/assets/1b4eb511-b2b1-48c1-89d5-2f65489c1e2d)
![image](https://github.com/user-attachments/assets/d7d91a85-4f49-459b-bf37-02061c7e119e)
![image](https://github.com/user-attachments/assets/5f75c384-092a-4dfb-8e43-d1819f513173)

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
