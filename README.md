# 🏦 Bank Management System

A command-line Bank Management System built with **Python** and **MySQL**. It lets customers open and manage accounts, deposit and withdraw money, and view mini statements, while a password-protected manager panel provides bank-wide reports and administration tools. Menus are rendered as clean tables using **PrettyTable**.

---

## ✨ Features

### 👤 Account Operations
- **Account Opening** – auto-generates a unique Account Number, Customer ID (`CUST0XXXX`) and IFSC-style code (`SPB000XXXXX`)
- **Account Updation** – update name, phone number, address or branch name
- **Account Deletion** – delete an account after confirmation

### 💸 Transaction Operations
- **Deposit** money into an account
- **Withdraw** money (with insufficient-balance check)
- **Check Balance**

### 🧾 Mini Statement
- Shows the last three transactions (`+` = deposit, `-` = withdrawal)
- Asks the customer to confirm their name before displaying the statement

### 🔐 Manager Folder (password protected)
1. View all accounts
2. Search customer by account number
3. View total bank balance
4. Account statistics (total / savings / current accounts)
5. View all transactions
6. Delete a customer account
7. Change account type (Savings / Current)
8. Bank information (accounts, branches, total balance)
9. Manager logout

### 🎯 Convenience
- Menu options can be chosen by **number**, **full name** or **shortcut** (e.g. `1`, `account operation`, `aop`)
- Friendly emoji-based feedback messages

---

## 🛠️ Tech Stack

| Component        | Technology                 |
|------------------|----------------------------|
| Language         | Python 3.x                 |
| Database         | MySQL                      |
| DB Connector     | `mysql-connector-python`   |
| Table Rendering  | `prettytable`              |

---

## 📋 Prerequisites

- Python 3.8 or higher
- MySQL Server installed and running on `localhost`
- A MySQL user with permission to create databases (default: `root`)

---

## 🚀 Installation & Setup

1. **Clone or download** the project

   ```bash
   git clone <your-repository-url>
   cd bank-management-system
   ```

2. **Install the dependencies**

   ```bash
   pip install mysql-connector-python prettytable
   ```

3. **Configure the database connection**

   Open the Python file and update the connection details with your own MySQL credentials:

   ```python
   a = sql.connect(host="localhost", user="root", passwd="YOUR_MYSQL_PASSWORD")
   ```

   > 💡 Tip: avoid committing real passwords to Git. Consider storing them in an environment variable or a `.env` file.

4. **Run the program**

   ```bash
   python bank.py
   ```

   On first run the program automatically creates the database (`test3`) and both tables. On later runs it connects to the existing database.

---

## 🗄️ Database Schema

**Database:** `test3`

### Table `t1` – Account details

| Column         | Type          | Notes                |
|----------------|---------------|----------------------|
| `Account_no`   | INT           | Primary key          |
| `Name`         | VARCHAR(100)  |                      |
| `Customer_ID`  | VARCHAR(15)   | e.g. `CUST01234`     |
| `Branch_Name`  | VARCHAR(100)  |                      |
| `Address`      | VARCHAR(200)  |                      |
| `IFSE_code`    | VARCHAR(100)  | e.g. `SPB00012345`   |
| `Account_type` | VARCHAR(50)   | Savings / Current    |
| `Balance`      | INT           | Starts at 0          |
| `Phone_Number` | VARCHAR(15)   |                      |

### Table `t2` – Mini statement

| Column              | Type         | Notes                         |
|---------------------|--------------|-------------------------------|
| `Account_no`        | INT          | Foreign key → `t1.Account_no` |
| `Name`              | VARCHAR(50)  |                               |
| `Last_Payment`      | VARCHAR(20)  | e.g. `+500` or `-200`         |
| `2nd_Last_Payment`  | VARCHAR(20)  |                               |
| `3rd_Last_Payment`  | VARCHAR(20)  |                               |

---

## 🧭 Usage Guide

### Main Menu

```
+-----------------------+
|      Banking Menu     |
+-----------------------+
| 1. Account Operation  |
| 2. Transaction Operation |
| 3. Mini Statement     |
| 4. Manager Folder     |
| 5. Exit               |
+-----------------------+
```

### Shortcuts

| Menu                   | Shortcut |
|------------------------|----------|
| Account Operation      | `aop`    |
| Account Opening        | `ac`     |
| Account Updation       | `au`     |
| Account Deletion       | `ad`     |
| Transaction Operation  | `ao`     |
| Deposit                | `d`      |
| Withdraw               | `wd`     |
| Check Balance          | `cb`     |
| Mini Statement         | `ms`     |
| Manager Folder         | `mf`     |
| Exit                   | `e`      |

### Manager Access

The Manager Folder is protected by a password defined in the source code. Change it before using the project for anything beyond learning.

---

## 📁 Project Structure

```
bank-management-system/
├── bank.py        # Main application
└── README.md      # Project documentation
```

---

## 🔒 Security Notes

This project is built for learning purposes. Before any real-world use:

- Move database credentials and the manager password out of the source code
- Hash stored credentials instead of using plain-text comparison
- Validate all user input (phone numbers, amounts, account types)
- Use database transactions so deposits, withdrawals and statement updates succeed or fail together

---

## 🚧 Future Improvements

- Customer PIN / password authentication
- Guaranteed-unique account number generation
- Full transaction history table instead of only the last three entries
- Fund transfer between accounts
- GUI or web interface (Tkinter / Flask / Django)
- Export statements to PDF or CSV

---

## 👨‍💻 Author

**Suvayan**

---

## 📄 License

This project is open source and available for educational use.
