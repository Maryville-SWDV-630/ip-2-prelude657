from CheckingAccount import Checking_Account #driver importing checking account
import random #random function to create account number
import sys #for exit

print ("Enter your name:") #name field
name = input()

print ("Enter you Adresss:") #address field
addy = input()

print("How much will you start you bank account with?:") #initial deposit
balance = int (input())

accountNumber = (random.randrange(100,999)) #random account number creator

accnum = Checking_Account(name,accountNumber,addy,balance)

print ("your account number is %d" %(accountNumber)) #account number

print()

while True: #account selection
    print ("Enter 1 for account info")
    print ("Enter 2 to debit money")
    print ("Enter 3 to credit money")
    print ("Enter 4 to end transaction")
    
    
    selection = int(input())
    
    if (selection ==1): # account info
        print(accnum.get_account_name())
        print(accnum.get_addy())
        print()
        print("your balance is : $" + str(accnum.get_balance()))
        print ("your account number is: %d" %(accountNumber))
        print()
        print ("Please make another selection or press 4 to exit")
        print()
        
    elif (selection == 2):
        print("How much are you withdrawing?:") #withdraws money from account via debit method on checkin_account.py
        debit_amount = int (input())
        debit_check= accnum.debit(debit_amount)
        if(debit_check == 0):
            print("insufficient funds. You only have %d dollars in your account" %(balance))
            
        else:
            print("money withdrawn")
   
    elif (selection == 3):
        print("How much are you depositing?:") #deposits money to account via credit method on checkin_account.py
        credit_amount = int (input())
        accnum.credit (credit_amount)
        print ("money deposited")
        print ("Your new balance is: $" + str(accnum.get_balance()))
        
    elif (selection == 4): #exit
         print("Thank you for using our ATM")
         sys.exit()
        
    else:
        print ("try again") #any other number besides 1-4
    print()
        
        
        
        
        