file=r"C:\Users\user\Documents\Git Bash\python-homeworks\lesson-8\homework\accounts.txt"
class Account:
    def __init__(self,account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance

    def __str__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"

class Bank:
    def __init__(self):
        self.accounts={}

    def create_account(self,name,initial_deposit):
        try:
            account_number=list(self.accounts.keys())[-1]+1
            i=1
            while self.exists(account_number):
                account_number=list(self.accounts.keys())[-1]+1+i
                i=i+1
        except:
            account_number=1
        self.accounts[account_number]=Account(account_number,name,initial_deposit)
        return self.accounts[account_number]
    def view_account(self,account_number):
        try:
            print(self.accounts[account_number])
        except:
            print("No such account number exist!")

    def deposit(self,account_number,amount):
        if self.exists(account_number):
            self.accounts[account_number].balance=self.accounts[account_number].balance+amount
        else:
            print("No such account exist")

    def withdraw(self,account_number,amount):
        if self.exists(account_number):
            if self.accounts[account_number].balance>=amount:
                self.accounts[account_number].balance=self.accounts[account_number].balance-amount
            else:
                print("You don't have that much money")
        else:
            print("No such account exist")

    def save_to_file(self):
        with open(file,"w") as f:
            for row in self.accounts.values():
                f.write(str(row)+"\n")

    def load_from_file(self):
        with open(file,"r") as f:
            lines=f.readlines()
            for line in lines:
                l=line.strip().split(", ")
                self.accounts[int(l[0])]=Account(int(l[0]),l[1],int(l[2]))

    def exists(self,account_number):
        if account_number in self.accounts.keys():
            return True
        else:
            return False
        
My_Bank=Bank()
My_Bank.load_from_file()
while True:
    choice=input("""
          1.Create an account
          2.View account details
          3.Deposit Money
          4.Withdraw money
          5.Save to file
          6.Exit
          Your choice (1-5): """)
    if choice=="1":
        name=input("Enter name: ")
        initial_deposit=int(input("Enter initial deposit: "))
        my_account=My_Bank.create_account(name,initial_deposit)
        print("Account created! Your details:")
        print(my_account)
    elif choice=="2":
        account_number=int(input("Enter account number: "))
        My_Bank.view_account(account_number)
    elif choice=="3":
        account_number=int(input("Enter account number: "))
        amount=int(input("Enter amount: "))
        My_Bank.deposit(account_number, amount)
    elif choice=='4':
        account_number=int(input("Enter account number: "))
        amount=int(input("Enter amount: "))
        My_Bank.withdraw(account_number, amount)
    elif choice=="5":
        My_Bank.save_to_file()
    elif choice=="6":
        print("Goodbye")
        break
    else:
        print("Unsupported choice!")