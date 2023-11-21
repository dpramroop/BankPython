
import datetime

class Bank:

    def __init__(self, total=0.00) -> None:
        self.total=total

    def Deposit(self,amount):
        if amount>0:
            self.total+=amount
           
        
    def Withdraw(self,amount):
        if self.total>=amount:
            self.total-=amount

    def CurrentAmount(self):
        return self.total


bank= Bank(3000)
atm=True
transactionlist=[]
dchoice=False
while atm==True:
    opt= input("Choose: 1-Deposit, 2-Withdraw, 3-Current Balance, 4-Exit ::")
    if opt=="1":
        dchoice=True
        while dchoice:
            try:
                damt=input("Deposit Amount:")
                bank.Deposit(float(damt))
                print(bank.CurrentAmount())
                transactionlist.append({"Type":"Deposit","Amount":damt,"Balance":bank.CurrentAmount(),"Date":datetime.datetime.now()})
                
                dchoice=False
            except:
                print("Must be a valid number")
    elif opt=="2":
        dchoice=True
        while dchoice:
            try:
                amount= float(input("Withdraw Amount:"))
                bank.Withdraw(amount)
                print(bank.CurrentAmount())
                transactionlist.append({"Type":"Withdraw","Amount":amount,"Balance":bank.CurrentAmount(),"Date":datetime.datetime.now()})
                dchoice=False
            except Exception as e:
                print(e)    
    elif opt=="3":
        print(bank.CurrentAmount())
    elif opt=="4":
        print(bank.CurrentAmount())
        atm=False
    else:
        print("Please select from the following options")
print(transactionlist)
with open("transaction",'w') as file:
    for transaction in transactionlist:
        file.write("%s\n" % f"Type:{transaction['Type']}, Amount:${transaction['Amount']}, Balance:${transaction['Balance']},Date:{transaction['Date']}" )
print("GoodBye")
    
    