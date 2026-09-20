accounts = []

def display_menu():
    print("============== Bank Management System ==============")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Search Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Delete Account")
    print("7. Exit")

def create_account():
    account = {}

    account["id"] = int(input("Enter Account ID: "))
    account["name"] = input("Enter Account Holder Name: ")
    account["balance"] = float(input("Enter Initial Balance: "))

    accounts.append(account)

    print("Account created successfully!")

def view_accounts():
    if not accounts:
        print("No accounts found")
        return

    print("\n============== Accounts ==============")
    for account in accounts:
        print("----------------------------")
        print("ID", account["id"])
        print("Name", account["name"])
        print("Balance", account["balance"])

def search_account():
    if not accounts:
        print("No accounts found")
        return

    accounts.sort(key=lambda account: account["id"]) 

    account_id = int(input("Enter Account ID: "))

    left = 0
    right = len(accounts) - 1

    while left <= right:
        middle = (left + right) // 2

        if accounts[middle]["id"] == account_id:
            account = accounts[middle]

            print("\n============== Account ==============")
            print("----------------------------")
            print("ID", account["id"])
            print("Name", account["name"])
            print("Balance", account["balance"])
            print("----------------------------")

            return

        elif accounts[middle]["id"] < account_id:
            left = middle + 1
        else:       
            right = middle - 1        

def deposit():
    account_id = int(input("Enter Account ID: "))

    for account in accounts:
        if account["id"] == account_id:
            amount = float(input("Enter Deposit Amount:"))
            
            if amount < 0:
                print("----------------------------")
                print("Deposit amount cannot be negative")
                return
            
            account["balance"] += amount

            print("Deposit successful")

def withdraw():
    account_id = int(input("Enter Account ID: "))

    for account in accounts:
        if account["id"] == account_id:
            amount = float(input("Enter withdrawal Amount:"))

            if account["balance"] < amount :
                print("----------------------------")
                print("Insufficient balance")
                return

            account["balance"] -= amount

            print("withdrawal successful")

def delete_account():
    if not accounts:
        print("No accounts found")
        return
    
    account_id = int(input("Enter Account ID: "))

    for account in accounts:
        if account["id"] == account_id:
            accounts.remove(account)

            print("Account delete successful")

            return



def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                create_account()
            case '2':
                view_accounts()
            case '3':
                search_account()    
            case '4':
                deposit()
            case '5':
                withdraw()
            case '6':
                delete_account()    
            case '7':
                print("Exit")
                break    
            case _:
                print("Invalid Choice Selction")

main()                                      

