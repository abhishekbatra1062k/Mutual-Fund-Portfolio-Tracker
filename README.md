# **Mutual-Fund-Portfolio-Tracker**

## **Setup Instructions**

### **Prerequisites**
- Python 3.9 or later
- SQLite (for the database)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/abhishekbatra1062k/Mutual-Fund-Portfolio-Tracker.git
   cd Mutual-Fund-Web-App
2. Create virtual Environment and Install Dependencies
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
3. Open the databse file and Run the following queries for Table Creation Queries
    ```bash
    sqlite3 app.db

    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL
    );

    DROP TABLE IF EXISTS portfolios;
    CREATE TABLE portfolios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        fund_name TEXT NOT NULL,
        units REAL NOT NULL,
        purchase_price REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
4. Run the application
    ```bash
    uvicorn app.main:app --reload