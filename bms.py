class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TransferCash = False

    def register(self, name, ph, password):
        cash = self.cash
        conditions = True
        if len(str(ph))  > 10 or len(str(ph)) < 10:
            print("Invalid Phone number! Enter 10 digit Mobile Number")
            conditions = False

        if len(password) < 5 or len(password)  > 18:
            print("Enter Password greater than 5 and less than 18 Character")
            conditions = False     

        if conditions == True:
            print("Account created successfully ")
            self.client_details_list = [name, ph, password, cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")

        def login(self, name, ph, password):
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                if str(ph) in str(self.client_details_list):
                    if str(password) in str(self.client_details_list):
                        self.loggedin = True

                    if self.loggedin == True:
                        print(f"{name} logged in")
                        self.cash = int(self.client_details_list[3])
                        self.name = name
                    else:
                        print("Wrong details")

        def add_cash(self, amount):
            if amount > 0:
                self.cash += str(amount)
                with open(f"{name}","r") as f:
                    details = f.read()
                    self.client_details_list = details.split("\n")


                with open(f"{name}.txt","w") as f:
                    f.write(details.replace(str(self.client_details_list[3],str(self.cash))))

                print("Amount added successfully")

            else:
                print("Enter correct value of amount")

        def Transfer_cash(self, amount, name, ph):
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                if str(ph) in self.client_details_list:
                    self.TransferCash = True

            if self.TransferCash == True:
                total_cash = int(self.client_details_list[3]) + amount
                left_cash = self.cash - amount
                with open(f"{name}.txt","w") as f:
                    f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

                with open(f"{self.name}.txt","w") as f:
                    f.write(details.replace(str(self.client_details_list[3]),str(left_cash)))

                print("Amount Transfered Successfully to", name, "-",ph)

                    
if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to my Bank")
    print("1. Login")
    print("2. Create a new Account")
    user = int(input("Make Decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter Password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1. Add Amount ")
                print("2. Check Balance ")
                print("3. Transfer Amount ")
                print("4. Edit Profile ")
                print("5. Logout ")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter"))
                    Bank_object.add_cash(amount)
                    print("\n1.Back Menu ")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break

                if login_user == 2:
                    print("Balance =",Bank_object.cash)
                    print("\n1.Back Menu ")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    if choose == 2:
                        break

                if login_user == 3:
                    print("Balance ="Bank.cash)
                    amount = int(input("Enter Amount: "))
                    if amount > 0 and amount <= Bank.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Transfer_cash(amount, name, ph)
                        print("Balance =",Bank_object.cash)
                        print("\n1. Back Menu")
                        print("2.Logout ")  
    

    if user == 2:
        print("Creating a new Account ")
        name = input("Enter name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter Password: ")
        Bank_object.register(name, ph, password)            