
from datetime import datetime
PIN= 1234
balance=10000
transactions=[]
now = datetime.now()
date = now.strftime("%Y-%m-%d")     # Format: 2025-08-13
time = now.strftime("%H:%M:%S")
print("Welcome to SB1")

print('Insert your ATM Card')
print()

inserted= int(input('1 Yes, 2 No:'))

if inserted == 1:

    userpin =int(input('Enter your PIN:'))
    
    if userpin == PIN:
    
        print('''
        
        Available Languages:
        
        1. English
        
        2. hindi
        ''')
        
        language= int(input("Select any one of the languages above: "))
        
        print( '''
        
        1. Deposit
        
        2. withdrawal
        
        3. Balance Check / Mini Statement
        
        4. PIN Change
        ''')
        
        option =int(input('Select any one the options above:'))
        if option ==1:
            amount=int(input("Feed thr cash : "))
            if amount % 100==0:
                print('Cash has been accepted')
                balance+=amount
                transactions.append(amount)
                print("Your current balance is : ",balance)
            else:
                print('Invalid cash')
        elif option ==2:
            amount=int(input("Enter the amount : "))
            if amount<balance and amount%100==0:
                print('collect the cash')
                balance-=amount
                print ("your balance is : ",balance)
            else:
                print("No balance")
        elif option ==3:
            print(
                f'''
                            State bank of India
                Date: {date}                    Time :{time}
                ''')
            for transaction in transactions:
                print(transaction)
            print('Balance: ',balance)
        elif option == 4:
            old_pin=int(input('Enter ur old pin : '))
            if old_pin ==PIN:
                new_pin=int(input("Enter the new pin : "))
                PIN=new_pin
                print("Your new pin is : ",PIN)
        else:
            print("You have selected the wrong option")
    else:
        print("please enter a valid pin")
if inserted ==2:
    print("Please insert your card")