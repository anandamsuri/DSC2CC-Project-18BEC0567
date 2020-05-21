import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = ''
    deposit=0
    debt=0
    amount2=0
    type = ''
    
    def createAccount(self):
        self.accNo= int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Ente the type of account [FD/RD] : ")
        self.loginid=input("Enter the Account Login Id :")
        self.password= input("Enter password :")
        i1=int(input("Deposit Money :"))
        if(i1>0) :
            self.deposit = i1
        else :
            print("please Enter a Valid Amount") 
        self.debt=0
        print("\n\n\nAccount Created")
    
    def showAccount(self):
        print("Account Number : ",self.accNo)
        print("Account Holder Name : ", self.name)
        print("Type of Account",self.type)
        print("Balance : ",self.deposit)
        print("Login : ",self.loginid)
    
    def modifyAccount(self):
        print("Account Number : ",self.accNo)
        self.name = input("Modify Account Holder Name :")
        self.type = input("Modify type of Account :")
        i2=int(input("Modify Balance :"))
        if(i2>0) :
            self.deposit = i2
        else :
            print("please Enter a Valid Amount")
        self.debt=0
        self.loginid=input("Enter the Account Login Id")
        self.password= input("Enter password ")
        
    def deposit(self,amount):
        if(amount>0) :
            self.deposit += amount
        else :
            print("please Enter a Valid Amount")
    def withdrawAmount(self,amount):
        if(amount>0) :
          self.deposit -= amount
        else :
            print("please Enter a Valid Amount")
    def takeloan(self,loan):
        if(amount2>0) :
            self.debt += amount2    
        else :
            print("please Enter a Valid Amount")
    def payloan(self,loan):
        if(amount2>0) :
            self.debt -= amount2
        else :
            print("please Enter a Valid Amount")
    def report(self):
        print(self.accNo," ",self.name ," ",self.type," ", self.deposit," ",self.id)
    
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
    def getLoginid(self):
        return self.loginid
    def getpassword(self):
        return self.password
    

def intro():
    print("\t\t\t\t**********************")
    print("\t\t\t\tRestful API to handle Bank Transactions")
    print("\t\t\t\t**********************")

    print("\t\t\t\tDone by:")
    print("\t\t\t\tAnand")
    print("\t\t\t\t18BEC0567")

    input()



def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo," ", item.name, " ",item.type, " ",item.deposit,)
        infile.close()
    else :
        print("No records to display")
        

def displaySp(num,word): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                if item.password == word :
                   print("Your account Balance is = ",item.deposit)
                   found = True
                else :
                   print("Enter Password is Incorrect ")   
                   found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")
  
def displaydt(num,word): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
              if item.password == word :
                print("Your account Debt is = ",item.debt)
                found = True
              else :
                  print("Enter Password is Incorrect ")   
                  found = True 
                    
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this number")        

def depositAndWithdraw(num1,num2,word): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    if item.password == word :
                      i3 = int(input("Enter the amount to deposit : "))
                      if(i3>0) :
                        amount = i3
                        item.deposit += amount
                        print("Your account is updted")
                      else :
                        print("please Enter a Valid Amount")
                        break
                    else:
                         print("Enter Password is Incorrect ") 
                elif num2 == 2 :
                    if item.password == word :
                      i4 = int(input("Enter the amount to withdraw : "))
                      if(i4>0) :
                        amount = i4
                      else :
                        print("please Enter a Valid Amount")
                        break        
                      if amount <= item.deposit :
                        item.deposit -=amount
                      else :
                        print("You cannot withdraw larger amount"  )
                    else :
                        print("Enter Password is Incorrect ")          
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
def payandtakedebt(num1,num2,word): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    if item.password == word :
                      i5 = int(input("Enter the amount to Take Loan : "))
                      if(i5>0) :
                        amount2 =  i5
                        item.debt += amount2
                        print("Your account is updted")
                      else :
                          print("please Enter a Valid Amount")
                          break
                    else :
                        print("Enter Password is Incorrect ") 
                else :
                    if item.password == word :              
                      i6=int(input("Enter the amount to Pay Loan : "))
                      if(i6>0) :
                        amount2 = i6
                        item.debt -=amount2
                      else :
                          print("please Enter a Valid Amount")
                          break 
                    else :
                        print("Enter Password is Incorrect ")          
    else :
        print("No records to Search")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
def deleteAccount(num,word):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
              if item.password == word :              
                newlist.append(item)
              else :
                  print("Enter Password is Incorrect ")  
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifyAccount(num,word):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accNo == num :
                if item.password == word :
                  item.name = input("Enter the account holder name : ")
                  item.type = input("Enter the account Type : ")
                  item.loginid = input("Enter the Login Id  : ")
                  item.password=input("Enter the password : ")
                else :
                  print("Enter Password is Incorrect ")  
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def writeAccountsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
def transfer(num,word,acc2):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
           if item.accNo == num :
              if(h1>0) :
                transamount=h1
                if item.password == word :
                  item.deposit = 100
                  if item.accNo == acc2 :
                    item.deposit = 100
                  else :
                      print("Transaction Unsuccessful Money will deposited back ")
                else :
                    print("Enter Password is Incorrect ")      
              else :
                  print("Enter A valid Amount ")      
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

            
          
            
ch=''
num=0
word2=0
intro()

while ch != 11:
    
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. Transfer Amount")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. Take Loan")
    print("\t9. PayLoan")
    print("\t10. Debt")
    print("\t11. Employee Login")
    print("\t0. EXIT")
    print("\tSelect Your Option (0-1) ")
    ch = input()
    
    if ch == '1':
        writeAccount()
    elif ch =='2':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        depositAndWithdraw(num, 1,word)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        depositAndWithdraw(num, 2,word)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password  :")
        displaySp(num,word)
    elif ch == '5':
        print("Enter your account no. :")
        num=input()
        print("Enter the Amount to be Transferred :")
        h1=int(input())
        word = input("\tEnter The account Password : ")
        print("Enter receiver account no. :")
        acc2=input()
        transfer(num,word,acc2)
    elif ch == '6':
        num =int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password :")
        deleteAccount(num,word)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        modifyAccount(num,word)
    elif ch =='8':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        payandtakedebt(num, 1,word)
    elif ch == '9':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        payandtakedebt(num, 2,word)
    elif ch =='10':
        num = int(input("\tEnter The account No. : "))
        word = input("\tEnter The account Password : ")
        displaydt(num,word)   
    elif ch == '0':
        print("\tThanks for using this API")
        break
    elif ch == '11':
        adm=input("Employee Login ID: ")
        if adm == "admin" :
          pas=input("Employee Login Password: ")
          if pas == "adminpassword" :
            displayAll();    
          else :
              print("Entered password is wrong ")
        else :
              print("Entered Employee Login ID is wrong ")        
    else :
        print("Invalid choice")
    
    ch = input("Press Enter to continue : ")
    


    
    
    
    
    
    
    
    
    
