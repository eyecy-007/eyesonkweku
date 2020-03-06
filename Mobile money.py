import random

Accounts=[]
def createAccount():
    details={"AccountId":"","pin":"","balance":0}
    details['AccountId']=random.randint(99,999)
    details['pin']=input("enter your desired pin: ")
    Accounts.append(details)
    return getAccount(details['AccountId'],details['pin'])

def transferMoney():
        opt = input('MoMo,\nSelect 1 for MoMo User\nSelect 2 for Non MoMo User\nselect 3 for E-zwich\nSelect 4 for Other Networks\nSelect 5 for Bank Account\nSelect 6 to Go Back\n')
        
def payBill():
    opt = input('MoMo,\nSelect 1 for Utilities\nSelect 2 for School Fees\nselect 3 for General Payment\nSelect 4 for EVD\nSelect 5 for MTN Bills\nSelect 6 to Go Back\n')
    
def Buyairtime():
    opt = input('MoMo,\nSelect 1 for Self\nSelecct 2 for Others\nSelect 3 to end session\n')
    
def checkwallet():
    opt = input('MoMo,\nSelect 1 to Check Balance\nSelect 2 to Allow Cashout\nSelect 3 to Change & Reset PIN\nSelect 4 to Go Back\n')

    def Buybundle():
    opt = input('MoMo,\nSelect 1 for Data Bundle\nSelect 2 to Go Back\n')


def socialMediaBundle(index):
    opt = input('socialMediaBundle,\nSelect 1, from GHC15\nSelect 2 for GHC25\nSelect 3 for GHC35\nSelect 4 to Go Back\n')
    if opt =='4':
        keepAlive = False
    else:
        print('enter a valid number')
    

def midnightBundle(index):
    opt = input('socialMediaBundle,\nSelect 1, from GHC15\nSelect 2 for GHC25\nSelect 3 for GHC35\nSelect 4 to Go Back\n')
    if opt =='4':
        keepAlive = False
    else:
        print('enter a valid number')
    

def videoBundle(index):
    opt = input('socialMediaBundle,\nSelect 1, from GHC15\nSelect 2 for GHC25\nSelect 3 for GHC35\nSelect 4 to Go Back\n')
    if opt =='4':
        keepAlive = False
    else:
        print('enter a valid number')

    

def getAccount(AccountId,pin):
    for item in Accounts:
        if item.get("AccountId") == AccountId and item.get('pin') == pin:
            return Accounts.index(item)

def deposit(index):
    Accounts[index]['balance']+=float(input('Deposit\nenter deposit amount: '))

def withdrawal(index):
    amt = float(input('enter withdraw amount: '))
    if amt <= Accounts[index]['balance']:
        Accounts[index]['balance']-=amt
    else:
        print('you cannot withdraw more than your current balance, Ghc{}'.format(Accounts[index]['balance']))



def sessionControl(Buybundle):
     print(Buybundle)
     keepAlive=True
     while(keepAlive):
         opt = input('Data Bundle,\nSelect 1 for Social Media Bundle\nSelect 2 for Midnight Bundle\nSelect 3 for Video Bundle\nSelect 4 to Go Back\n')
         if opt =='1':
             socialMediaBundle(index)
         elif opt =='2':
             midnightBundle(index)
         elif opt =='3':
             videoBundle(index)
         elif opt =='4':
              keepAlive = False
         else:
             print('enter a valid number')



def sessionControl(transferMoney):
     print(transferMoney)
     keepAlive=True
     while(keepAlive):
         a= input('Enter number:')
         b=input('Confirm number')
         c=input('Enter amount')
         d=input('Enter reference')


def sessionControl(checkwallet):
     print(checkwallet)
     correct_pin = "1807"
     keepAlive=True
     while(keepAlive):
         pin=input("MoMo\nEnter Pin:")
         tries = 1
         while correct_pin == "1807":
             if pin == correct_pin and tries <= 1:
                 print("Current Balance:GHS200.00,Availabe Balance:GHS200.00")
                 break
                
             if tries < 3 and pin!= correct_pin:
                 tries+=1
             #if pin == correct_pin and tries <= 2:
                 #print("Current Balance:GHS200.00,Availabe Balance:GHS200.00")
                 
                 pin=int(input("Wrong pin, Re-Enter pin again:"))
                 if tries == 3 and pin!= correct_pin:
                     print("Incorrect pin, you have no remaining attempts to input your pin!")
                 while correct_pin == "1006":
                     if pin == correct_pin and tries < 4:
                         print("Current Balance:GHS200.00,Availabe Balance:GHS200.00")
                         break
                     




                     
                 #else:
                     #if pin == correct_pin
                     #if tries < 4:
                         #print("Current Balance:GHS200.00,Availabe Balance:GHS200.00")
                         #break



#def sessionControl(index):
    #print(index)
    #keepAlive=True
    #while(keepAlive):
        #opt = input('Welcome,\nselect 1 to make a deposit\nselect 2 to make a withdrawal\nselect 3 to view account details\nselect 4 to Go Back\n')
        #if opt =='1':
            #deposit(index)
        #elif opt =='2':
            #withdrawal(index)
        #elif opt =='3':
            #print(Accounts[index]) 
        #elif opt =='4':
            #keepAlive = False
        #else:
            #print('enter a valid number')

def main():
    keepAlive=True
    while(keepAlive):
        opt = input('MoMo,\nSelect 1 to Transfer Money\nSelect 2 to Buy Airtime  \nselect 3 to Pay Bill\nSelect 4 to Buy bundle\nSelect 5 to check wallet\nSelect 6 to Go Back\n')
        if opt =='1':
            sessionControl(transferMoney())
        elif opt =='2':
            sessionControl(Buyairtime())
        elif opt =='3':
            sessionControl(PayBill())
        elif opt =='4':
            sessionControl(Buybundle())
        elif opt =='5':
            sessionControl(checkwallet())
        elif opt =='6':
            keepAlive = False
        else:
            print('enter a valid number')
    
if __name__ == "__main__":
    main()
