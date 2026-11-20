# import all the necessary libararies
import mysql.connector as sql
from prettytable import PrettyTable
import random as r
import os
from dotenv import load_dotenv

# all the functions
def ramdom_no(y):
    if y.lower() == "acc_no":
        total=""
        for i in range (5):
            no1=r.randint(0,9)
            total+=str(no1)
        return total
    
    elif y.lower() == "cust_id":
        total="CUST0"
        for i in range (4):
            no1=r.randint(0,9)
            total+=str(no1)
        return total


    elif y.lower() == "ifse_no":
        total="SPB000"
        for i in range (5):
            no1=r.randint(0,9)
            total+=str(no1)
        return total




#password
load_dotenv()
DBpass=os.environ.get("DB_password")
manager_pass=os.environ.get("manager_password")


# create a database to store data

try:
    a = sql.connect(host="localhost",user="root",passwd=DBpass)
    cur=a.cursor()
    a.autocommit = True
    cur.execute("CREATE DATABASE IF NOT EXISTS test3")
    cur.execute("USE test3")
    cur.execute("CREATE TABLE t1(Account_no INT PRIMARY KEY, Name varchar(100),Customer_ID varchar(15),Branch_Name varchar(100),Address varchar(200), IFSE_code varchar(100),Account_type varchar(50),Balance int,Phone_Number varchar(15))")
    cur.execute("CREATE TABLE t2(Account_no INT,Name VARCHAR(50),Last_Payment VARCHAR(20),2nd_Last_Payment VARCHAR(20),3rd_Last_Payment VARCHAR(20),FOREIGN KEY (Account_no) REFERENCES t1(Account_no))")
    a.commit()
    print("succ")

except:
    a = sql.connect(host="localhost",user="root",passwd=DBpass, database="test3" )
    cur=a.cursor()
    a.autocommit = True


# wealcome message
table=PrettyTable()
table.field_names=["Welcome to the Bank Management System. Namaste \U0001F64F \U0001F64F !!"]

print(table)



while True:
    table=PrettyTable()
    menu_options = [
    "1. Account Operation",
    "2. Transaction Operation",
    "3. Mini Statement",
    "4. Manager Folder",
    "5. Exit"]
    table.add_column("Banking Menu", menu_options)
    print(table)

    choice=input("\nEnter the option you want to choose:")


    if choice.lower() in ["1","account operation","aop"]:
        while True:
            
            table=PrettyTable()
            menu_options1 = [
            "1. Account Opening",
            "2. Account Updation",
            "3. Account Deletion",
            "4. Back to Main Menu"]
            table.add_column("Account Operation", menu_options1)
            print(table)
            

            choice1=input("Enter the option you want to choose:")


            if choice1=="1" or choice.lower()=="account opening" or choice.lower()=="ac" :
                # all the data
                Name=input("\nEnter your name:")
                Customer_ID=ramdom_no("cust_id")
                Branch_Name=input("\nEnter branch name:")
                Address=input("\nEnter your address:")
                IFSE_code=ramdom_no("ifse_no")
                Account_type=input("\nEnter Account Type:")
                Account_no=ramdom_no("acc_no")
                Phone_Number=input("\nEnter your Phone Number:")
                
                # insert the data into the database
                query="insert into t1 (Account_no,Name,Customer_ID, Branch_Name,Address,IFSE_code,Account_type,Balance,Phone_Number) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                value=(Account_no,Name,Customer_ID, Branch_Name,Address,IFSE_code,Account_type,0,Phone_Number)
                cur.execute(query, value)

                table=PrettyTable()
                table.align = "c"
                
                table.add_column("Your Account Details",[f"Account Number:{Account_no}", f"Name: {Name}", f"Customer ID: {Customer_ID}", f"Branch Name:{Branch_Name}", f"Address:{Address}", f"IFSE Code: {IFSE_code}", f"Account Type: {Account_type}" ,f"Phone Number: {Phone_Number}", f"Balance: 0 "])
                print(table)



                # table for mini statement
                query="insert into t2 (Account_no,Name,Last_Payment,2nd_Last_Payment,3rd_Last_Payment) values (%s,%s,%s,%s,%s)"
                value=(Account_no,Name,0,0 ,0)
                cur.execute(query, value)

                print("\n***Remember the Account Number for future reference***")
                print("\nAccount Created Successfully \U0001F44D \U0001F44D \U0001F44D")

                input("\nPress Enter to return to the menu...")
            
            
            elif choice1.lower() in ["2","account updation", "au"]:

                table=PrettyTable()
                menu_options1 = [
                "1. Update Name",
                "2. Update Phone Number",
                "3. Update Address",
                "4. Update Branch Name"]
                table.add_column("Account Updation", menu_options1)
                print(table)

                choice2=input("\nEnter the option you want to choose:")

                # update name 
                if choice2.lower()in ["1","update name","un"]:
                    try:
                        accn_no1=int(input("Enter Your Account Number:"))
                        cur.execute("SELECT Name FROM t1 WHERE Account_no = %s", (accn_no1,))
                        for i in cur:
                            name=i[0]
                            
                        table=PrettyTable()
                        table.add_column("Your Current Name", [name])
                        
                        print("\n", table)

                        new_name=input("Enter your new Name: ")

                        cur.execute("UPDATE t1 SET Name = %s WHERE Account_no = %s", (new_name, accn_no1))
                        cur.execute("UPDATE t2 SET Name = %s WHERE Account_no = %s", (new_name, accn_no1))


                        print("\nName Updated Successfully \U0001F600  \U0001F44D  \U0001F44D")

                        input("\nPress Enter to return to the menu...")


                    except:
                        print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")

                # update phone number

                elif choice2.lower() in["2","update phone number","upn","up"]:
                    try:
                        accn_no1=int(input("Enter Your Account Number:"))
                        cur.execute("SELECT Phone_Number FROM t1 WHERE Account_no = %s", (accn_no1,))
                        for i in cur:
                            phno=i[0]
                            
                        table=PrettyTable()
                        table.add_column("Your Current Phone Number", [phno])
                        
                        print("\n", table)

                        new_ph=input("Enter Your New Phone Number: ")

                        cur.execute("UPDATE t1 SET Phone_Number = %s WHERE Account_no = %s", (new_ph, accn_no1))

                        print("\nPhone Number Updated Successfully \U0001F600  \U0001F44D  \U0001F44D")


                        input("\nPress Enter to return to the menu...")
                    

                    except:
                        print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")

                    

                # update address 
                elif choice2.lower() in ["3","update address","ua",]:
                    try:
                        accn_no1=int(input("Enter Your Account Number:"))
                        cur.execute("SELECT Phone_Number FROM t1 WHERE Account_no = %s", (accn_no1,))
                        for i in cur:
                            address=i[0]
                            
                        table=PrettyTable()
                        table.add_column("Your Current Address", [address])
                        
                        print("\n", table)

                        new_address=input("Enter Your New Address: ")

                        cur.execute("UPDATE t1 SET Address = %s WHERE Account_no = %s", (new_address, accn_no1))

                        print("\nAddress Updated Successfully \U0001F600  \U0001F44D  \U0001F44D")

                        input("\nPress Enter to return to the menu...")


                    except:
                        print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")


                # update branch name
                elif choice2.lower()in ["4","update branch name","ubn","ub"]:
                    try:
                        accn_no1=int(input("Enter Your Account Number:"))
                        cur.execute("SELECT Branch_Name FROM t1 WHERE Account_no = %s", (accn_no1,))
                        for i in cur:
                            branch_na=i[0]
                            
                        table=PrettyTable()
                        table.add_column("Your Current Branch Name", [branch_na])
                        
                        print("\n", table)

                        new_ban=input("Enter Your New Branch Name: ")

                        cur.execute("UPDATE t1 SET Branch_Name = %s WHERE Account_no = %s", (new_ban, accn_no1))

                        print("\nBranch Name Updated Successfully \U0001F600  \U0001F44D  \U0001F44D")

                        input("\nPress Enter to return to the menu...")


                    except:
                        print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")


            elif choice1.lower() in ["3","account deletion","ad"]:
                try:
                    accn_no1=int(input("Enter Your Account Number:"))
                    cur.execute("SELECT Name FROM t1 WHERE Account_no = %s", (accn_no1,))
                    for i in cur:
                        name=i[0]
                        
                    table=PrettyTable()
                    table.add_column("Your Current Name", [name])
                    
                    print("\n", table)

                    confirm=input("Are you sure you want to delete your account? (yes/no): ")
                    if confirm.lower() == "yes":
                        cur.execute("DELETE FROM t1 WHERE Account_no = %s", (accn_no1,))
                        print("\nAccount Deleted Successfully \U0001F600  \U0001F44D  \U0001F44D")
                        input("\nPress Enter to return to the menu...")
                    else:
                        print("\nAccount deletion cancelled.")
                        input("\nPress Enter to return to the menu...")

                except:
                    print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")


            elif choice1.lower() in ["4","back to main menu","b"]:
                break

            



    elif choice.lower() in ["2","transaction operation", "ao"]:
        while True:

            table=PrettyTable()
            menu_options1 = [
            "1. Deposit in Account",
            "2. Withdraw from Account",
            "3. Check Balance",
            "4. Back to Main Menu"]
            table.add_column("Transaction Operation", menu_options1)
            print("\n", table)
            

            choice2=input("Enter the option you want to choose:")

            if choice2.lower() in ["1","deposit","d"]:
                #FFF
                try:
                    accn_no=int(input("Enter Your Account Number:"))

                    # for mini statement
                    cur.execute("SELECT * FROM t2 WHERE Account_no = %s", (accn_no,))

                    for i in cur.fetchall():
                        third_last_Payment = i[3]
                        second_last_payment = i[2]


                    # for main blance
                    cur.execute("select Balance from t1 where Account_no = %s",(accn_no,))
                    for i in cur:
                        bal=i[0]
                    

                    # diposit amount
                    deposit=int(input("\nEnter the amount you want to deposit:"))
                    cur.execute("update t1 set Balance=Balance+ %s where Account_no = %s", (deposit,accn_no))

                    cur.execute("select Balance from t1 where Account_no = %s",(accn_no,))
                    for i in cur:
                        baln=i[0]
                    table=PrettyTable()
                    table.add_column("Your Account Balance", [f"Rs.{baln}"])
                    print("\n",table)

                    # update mini statement
                    diposit= f"+{deposit}"
                    cur.execute("UPDATE t2 SET Last_Payment = %s, 2nd_Last_Payment = %s, 3rd_Last_Payment = %s WHERE Account_no = %s", (diposit,  second_last_payment,third_last_Payment, accn_no))
                    
                    print("\nAmount Deposited Successfully \U0001F600  \U0001F44D  \U0001F44D")
                    input("\nPress Enter to return to the menu...")

                except:
                    print("Account Number does not exist \U0001F615  \U0001F615  \U0001F615")

            elif choice2.lower() in ["2","withdraw","wd"]:
                try:
                    accn_no=int(input("Enter Your Account Number:"))

                    # for mini statement
                    cur.execute("SELECT * FROM t2 WHERE Account_no = %s", (accn_no,))

                    for i in cur.fetchall():
                        third_last_Payment = i[3]
                        second_last_payment = i[2]

                    # for main balance
                    cur.execute("select Balance from t1 where Account_no = %s",(accn_no,))
                    for i in cur:
                        bal=i[0]
                    table=PrettyTable()
                    table.add_column("Your Account Balance", [f"Rs.{bal}"])
                    print(table)

                    withdr=int(input("Enter the amount you want to Withdraw:"))
                    if bal is None or bal < withdr:
                        print("Your account has insufficient balance !!! \U0001F615  \U0001F615")
                    else:
                        
                        cur.execute("update t1 set Balance=Balance- %s where Account_no = %s", (withdr,accn_no))
                        a.commit()
                        cur.execute("select Balance from t1 where Account_no = %s", (accn_no,) )
                        for i in cur:
                            baln=i[0]
                        table=PrettyTable()
                        table.add_column("Your Account Balance", [f"Rs.{baln}"])
                        print("\n",table)

                        # update in mini statement
                        withdraw= f"-{withdr}"

                        cur.execute("UPDATE t2 SET Last_Payment = %s, 2nd_Last_Payment = %s, 3rd_Last_Payment = %s WHERE Account_no = %s", (withdraw,  second_last_payment,third_last_Payment, accn_no))


                        print("\nAmount Withdraw Successfully \U0001F600  \U0001F44D  \U0001F44D")
                        input("\nPress Enter to return to the menu...")


                except:
                    print("\nAccount Number does not exist \U0001F615  \U0001F615  \U0001F615")


            elif choice2.lower() in ["3","check balance","cb"]:

                try:
                    accn_no=int(input("Enter Your Account Number:"))
                    cur.execute("select Balance from t1 where Account_no = %s",(accn_no,))
                    for i in cur:
                        bal=i[0]
                        
                    table=PrettyTable()
                    table.add_column("Your Account Balance", [f"Rs.{bal}"])
                    print(table)

                    input("\nPress Enter to return to the menu...")

                except:
                    print("\nAccount Number does not exist \U0001F615  \U0001F615  \U0001F615")


            elif choice2.lower() in ["4","back to main menu","b"]:
                break


    elif choice.lower() in ["3","mini statement","ms"]:

        try:
            accn_no=int(input("Enter Your Account Number:"))

            # for mini statement
            cur.execute("SELECT * FROM t2 WHERE Account_no = %s", (accn_no,))

            for i in cur.fetchall():
                your_name = i[1]

            choice3=input(f"\n Is Your Name: {your_name} \U0001F44D \U0001F44D \U0001F44D  (yes/no): ")

            if choice3.lower() in ["yes","y"]:
                cur.execute("SELECT * FROM t2 WHERE Account_no = %s", (accn_no,))
                for i in cur.fetchall():
                    third_last_Payment = i[4]
                    second_last_payment = i[3]
                    last_payment = i[2]

                table=PrettyTable()
                table.add_column("Mini Statement", [f"Last Payment: {last_payment}", f"Second Last Payment: {second_last_payment}", f"Third Last Payment: {third_last_Payment}"])
                print(table)
                print("\n ***Here + mean Deposit and - mean Withdraw***")

                input("\nPress Enter to return to the menu...")


            elif choice3.lower() in ["no","n"]:
                print("\nPlease enter the correct account number \U0001F615  \U0001F615  \U0001F615")
                input("\nPress Enter to return to the menu...")
                



            

        except:
            print("\nAccount Number does not exist \U0001F615  \U0001F615  \U0001F615")
            

    elif choice.lower() in ["4", "manager folder", "mf"]:

        # ================= MANAGER LOGIN =================

        manager_password = input("\nEnter Manager Password: ")

        if manager_password != manager_pass:
            print("\nIncorrect Manager Password !!! ❌")
            input("\nPress Enter to return to the main menu...")
            continue

        print("\nManager Login Successful ✅")

        # ================= MANAGER MENU =================

        while True:

            table = PrettyTable()

            manager_options = [
                "1. View All Accounts",
                "2. Search Customer",
                "3. View Total Bank Balance",
                "4. Account Statistics",
                "5. View All Transactions",
                "6. Delete Customer Account",
                "7. Change Account Type",
                "8. Bank Information",
                "9. Manager Logout"
            ]

            table.add_column("Manager Folder", manager_options)

            print("\n", table)

            manager_choice = input("\nEnter your choice: ")

            # ==================================================
            # 1. VIEW ALL ACCOUNTS
            # ==================================================

            if manager_choice.lower() in ["1", "view all accounts", "vaa"]:

                cur.execute("""
                    SELECT Account_no, Name, Customer_ID,
                           Branch_Name, Account_type, Balance,
                           Phone_Number
                    FROM t1
                """)

                data = cur.fetchall()

                if data:

                    table = PrettyTable()

                    table.field_names = [
                        "Account No",
                        "Name",
                        "Customer ID",
                        "Branch",
                        "Account Type",
                        "Balance",
                        "Phone"
                    ]

                    for row in data:
                        table.add_row(row)

                    print("\n", table)

                else:
                    print("\nNo accounts found.")

                input("\nPress Enter to return to Manager Menu...")

            # ==================================================
            # 2. SEARCH CUSTOMER
            # ==================================================

            elif manager_choice.lower() in ["2", "search customer", "sc"]:

                try:

                    acc_no = int(input("\nEnter Account Number: "))

                    cur.execute("""
                        SELECT *
                        FROM t1
                        WHERE Account_no = %s
                    """, (acc_no,))

                    customer = cur.fetchone()

                    if customer:

                        table = PrettyTable()

                        table.field_names = [
                            "Account No",
                            "Name",
                            "Customer ID",
                            "Branch",
                            "Address",
                            "IFSC Code",
                            "Account Type",
                            "Balance",
                            "Phone"
                        ]

                        table.add_row(customer)

                        print("\n", table)

                    else:
                        print("\nAccount Number does not exist ❌")

                except:
                    print("\nInvalid Account Number ❌")

                input("\nPress Enter to return to Manager Menu...")

            # ==================================================
            # 3. TOTAL BANK BALANCE
            # ==================================================

            elif manager_choice.lower() in [
                "3",
                "total bank balance",
                "tbb"
            ]:

                cur.execute("""
                    SELECT SUM(Balance)
                    FROM t1
                """)

                result = cur.fetchone()

                total_balance = result[0]

                if total_balance is None:
                    total_balance = 0

                table = PrettyTable()

                table.field_names = ["Total Bank Balance"]

                table.add_row([f"Rs. {total_balance}"])

                print("\n", table)

                input("\nPress Enter to return to Manager Menu...")

            # ==================================================
            # 4. ACCOUNT STATISTICS
            # ==================================================

            elif manager_choice.lower() in [
                "4",
                "account statistics",
                "as"
            ]:

                # Total accounts
                cur.execute("SELECT COUNT(*) FROM t1")

                total_accounts = cur.fetchone()[0]

                # Savings accounts
                cur.execute("""
                    SELECT COUNT(*)
                    FROM t1
                    WHERE LOWER(Account_type) = 'savings'
                """)

                savings_accounts = cur.fetchone()[0]

                # Current accounts
                cur.execute("""
                    SELECT COUNT(*)
                    FROM t1
                    WHERE LOWER(Account_type) = 'current'
                """)

                current_accounts = cur.fetchone()[0]

                # Total balance
                cur.execute("""
                    SELECT SUM(Balance)
                    FROM t1
                """)

                total_balance = cur.fetchone()[0]

                if total_balance is None:
                    total_balance = 0

                table = PrettyTable()

                table.field_names = [
                    "Statistics",
                    "Value"
                ]

                table.add_row([
                    "Total Accounts",
                    total_accounts
                ])

                table.add_row([
                    "Savings Accounts",
                    savings_accounts
                ])

                table.add_row([
                    "Current Accounts",
                    current_accounts
                ])

                table.add_row([
                    "Total Bank Balance",
                    f"Rs. {total_balance}"
                ])

                print("\n", table)

                input("\nPress Enter to return to Manager Menu...")

            # ==================================================
            # 5. VIEW ALL TRANSACTIONS
            # ==================================================

            elif manager_choice.lower() in [
                "5",
                "view all transactions",
                "vat"
            ]:

                cur.execute("""
                    SELECT Account_no,
                           Name,
                           Last_Payment,
                           2nd_Last_Payment,
                           3rd_Last_Payment
                    FROM t2
                """)

                data = cur.fetchall()

                if data:

                    table = PrettyTable()

                    table.field_names = [
                        "Account No",
                        "Name",
                        "Last Payment",
                        "2nd Last",
                        "3rd Last"
                    ]

                    for row in data:
                        table.add_row(row)

                    print("\n", table)

                else:
                    print("\nNo transactions found.")

                input("\nPress Enter to return to Manager Menu...")

            # ==================================================
            # 6. DELETE CUSTOMER ACCOUNT
            # ==================================================

            elif manager_choice.lower() in [
                "6",
                "delete customer account",
                "dca"
            ]:

                try:

                    acc_no = int(
                        input("\nEnter Account Number to delete: ")
                    )

                    cur.execute("""
                        SELECT Name, Balance
                        FROM t1
                        WHERE Account_no = %s
                    """, (acc_no,))

                    customer = cur.fetchone()

                    if customer:

                        name = customer[0]
                        balance = customer[1]

                        table = PrettyTable()

                        table.field_names = [
                            "Account Number",
                            "Name",
                            "Balance"
                        ]

                        table.add_row([
                            acc_no,
                            name,
                            f"Rs. {balance}"
                        ])

                        print("\n", table)

                        confirm = input(
                            "\nAre you sure you want to delete "
                            "this account? (yes/no): "
                        )

                        if confirm.lower() in ["yes", "y"]:

                            # Delete mini statement first
                            cur.execute("""
                                DELETE FROM t2
                                WHERE Account_no = %s
                            """, (acc_no,))

                            # Delete account
                            cur.execute("""
                                DELETE FROM t1
                                WHERE Account_no = %s
                            """, (acc_no,))

                            a.commit()

                            print(
                                "\nAccount Deleted Successfully ✅"
                            )

                        else:

                            print(
                                "\nAccount deletion cancelled."
                            )

                    else:

                        print(
                            "\nAccount Number does not exist ❌"
                        )

                except:

                    print(
                        "\nInvalid Account Number ❌"
                    )

                input(
                    "\nPress Enter to return to Manager Menu..."
                )

            # ==================================================
            # 7. CHANGE ACCOUNT TYPE
            # ==================================================

            elif manager_choice.lower() in [
                "7",
                "change account type",
                "cat"
            ]:

                try:

                    acc_no = int(
                        input("\nEnter Account Number: ")
                    )

                    cur.execute("""
                        SELECT Name, Account_type
                        FROM t1
                        WHERE Account_no = %s
                    """, (acc_no,))

                    customer = cur.fetchone()

                    if customer:

                        name = customer[0]
                        old_type = customer[1]

                        print(
                            f"\nCustomer Name : {name}"
                        )

                        print(
                            f"Current Account Type : {old_type}"
                        )

                        new_type = input(
                            "\nEnter New Account Type "
                            "(Savings/Current): "
                        )

                        if new_type.lower() in [
                            "savings",
                            "current"
                        ]:

                            new_type = new_type.capitalize()

                            cur.execute("""
                                UPDATE t1
                                SET Account_type = %s
                                WHERE Account_no = %s
                            """, (new_type, acc_no))

                            a.commit()

                            print(
                                "\nAccount Type Updated Successfully ✅"
                            )

                        else:

                            print(
                                "\nInvalid Account Type ❌"
                            )

                    else:

                        print(
                            "\nAccount Number does not exist ❌"
                        )

                except:

                    print(
                        "\nInvalid Account Number ❌"
                    )

                input(
                    "\nPress Enter to return to Manager Menu..."
                )

            # ==================================================
            # 8. BANK INFORMATION
            # ==================================================

            elif manager_choice.lower() in [
                "8",
                "bank information",
                "bi"
            ]:

                cur.execute(
                    "SELECT COUNT(*) FROM t1"
                )

                total_accounts = cur.fetchone()[0]

                cur.execute("""
                    SELECT COUNT(DISTINCT Branch_Name)
                    FROM t1
                """)

                total_branches = cur.fetchone()[0]

                cur.execute("""
                    SELECT SUM(Balance)
                    FROM t1
                """)

                total_balance = cur.fetchone()[0]

                if total_balance is None:
                    total_balance = 0

                table = PrettyTable()

                table.field_names = [
                    "Bank Information",
                    "Value"
                ]

                table.add_row([
                    "Bank Name",
                    "Bank Management System"
                ])

                table.add_row([
                    "Total Accounts",
                    total_accounts
                ])

                table.add_row([
                    "Total Branches",
                    total_branches
                ])

                table.add_row([
                    "Total Bank Balance",
                    f"Rs. {total_balance}"
                ])

                print("\n", table)

                input(
                    "\nPress Enter to return to Manager Menu..."
                )

            # ==================================================
            # 9. MANAGER LOGOUT
            # ==================================================

            elif manager_choice.lower() in [
                "9",
                "manager logout",
                "logout",
                "l"
            ]:

                print(
                    "\nManager Logged Out Successfully 👋"
                )

                break

            # ==================================================
            # INVALID OPTION
            # ==================================================

            else:

                print(
                    "\nInvalid Manager Option ❌"
                )


    elif choice.lower() in ["5","exit","e"]:
        print("\nThank you for using the Bank Management System. Have a great day! hmmmmm \U0001F600 \U0001F600 \U0001F600")
        break