#Budget App Task
#Budget titled Zuri Budget App
database = { }

class Budget():
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(amount, bal):
        bal += amount
        return bal

    def withdraw(user, amount, bal):
        bal -= amount
        return bal

    def balance(db):
        for categ, bal in db.items():
            print(categ, bal)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        valuue2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(valuue2) + amount
        return db

def init():
    print(" Welcome to the Zuri Budget App \n")
    print("**** **** **** **** **** **** ****")
    menu()

def menu():
    try:

        selectedOption = int(input("\n **Please select a transaction to perfom**\nchoose (1) For  a new budget\nChoose (2) For budget funding \nChoose (3) For withdrawal\nChoose (4) To check your balance\nChoose (5) For electronic transfer fund between budgets\nChoose (6) To Exit the system\n"))
    except:
        print("Invalid input")
        menu()

    if (selectedOption == 1):
        new_budget()
    elif (selectedOption == 2):
        credit()
    elif (selectedOption == 3):
        debit()
    elif (selectedOption == 4):
        balance()
    elif (selectedOption == 5):
        transfer()
    elif (selectedOption == 6):
        out()
    else:
        print('Invalid input\n')
        menu()

def new_budget():
    print("\nCreating a New Budget\n")

    budget_title = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n$"))
      

    except:
        print('\nInvalid input')
        new_budget()
    budget = Budget(budget_title, amount)
    database[budget_title] = amount
    print('')
    print(f'Budget {budget_title} was setup with ${amount}')
    menu()

def debit():
    print("****Withdraw from an existing budget****\n")
    print('**** Available Budgets ****')

    for key, value in database.items():
        print(f"-  {key}")

    choose = int(input('\nPress (1) To confirm transaction\nPress (2) To terminate transaction\n'))
    if (choose == 1):
        user = input("\n Please select a budget to be debited \n")
        if user in database:
            print("Warning: Available balance cannot be less than $10.")
            amt = int(input("Enter amount \n$"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdraw(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been debited from Budget-{user}\nAvailable balance is ${new_balance}")
                menu()

            else:
                choose = int(input(f'\nBudget {user} is insufficient of the ${amt} required\nThe actual balance {database[user]}\n\nPress (1) To deposit to the budget\nPress (2) To choose the right budget\n'))
                if (choose == 1):
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(amt, balance)
                    database[user] = new_balance
                    print('')
                    print(f"Budgets {user} has been credited with ${amt}\n")
                    debit()

                elif (choose == 2):
                    debit()
                else:
                    print('Invalid option\n')
                    debit()
        else:
          choose = int(input(f'\n****  Budget {user} does not exist! ****\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
          if (choose == 1):
              new_budget()
          elif (choose == 2):
              debit()
          elif (choose == 3):
              print('')
              menu()
          else:
              print('Invalid option\n')
              debit()
    elif (choose == 2):
        print('\nTransaction terminated successfuly ')
        menu()
    else:
        print('\nInvalid option')
        debit()



def credit():
    print("**** Deposit into a budget ****\n")
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(f"-  {key}")

    choose = int(input('\nPress (1) To confirm transaction\nPress (2) To terminate transaction\n'))
    if (choose == 1):
        user = input("Select a budget \n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = new_balance
            print(f'\nBudget {user} is credited with ${amt}\nTotal Budget amount is now ${new_balance}')
            menu()

        else:
            print('')
            choose = int(input(f'Budget {user} does not exist!\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To return to the menu\n'))
            if (choose == 1):
                new_budget()
            elif (choose == 2):
                credit()
            elif (choose == 3):
                menu()
            else:
                print('Invalid option\n')
                credit()

    elif (choose == 2):
        print('\nDeposit transaction aborted successfuly')
        menu()
    else:
        print('\nInvalid option')
        deposit()


def balance():
    print(" Getting Your Budget Balance\n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print('Invalid selection. Please create a budget')
        print("**** **** **** **** ****")
        menu()
    else:
        print(f'${check_bal}')
        menu()

def transfer():
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(key)
        print('')
    print("**** Electronic Transfer Fund ****")
    print('Warning:  Budget balance cannot be left empty \n')
    from_budget = input("Enter the buget you are transfering from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer \n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You transfered ${from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose a valid budget\n')
                transfer()
        else:
            print(f'Insufficient amount-${from_amount} in {from_budget} budget')
            transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')
        print("You have been transfered to the main menu")

        menu()

def out():
    try:
        choose = int(input('Are you sure you want to exit the system?\nPress (1) to confirm\nPress (2) to continue budget operation\n'))
    except:
        print('Invalid input\n')
        out()

    if (choose == 1):
        print("\nSystem shutdown succesfuly. Good-bye!.")
        quit()
    elif (choose == 2):
        menu()
    else:
        print('Invalid input\n')
        out()



init()