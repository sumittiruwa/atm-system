#ATM System 

balance = 1000
pin = 2345

print("**insert your card please**")
pin_num = int(input("enter your pin number please: \n"))
if pin_num == pin:
    while  True:
        print('''
               1- check balanece
               2- deposite
               3- withdraw
               4- exit
               ''')

        option = int(input("choose your option please \n"))
        if option == 1:
                print(f"you cuurent balance is {balance}")
        elif option == 2:
                deposte_amt =  int(input("enter your deposite amount \n"))
                balance = balance +  deposte_amt
                print(f"your update balance is {balance}")
        elif option == 3:
                withdraw_amt + int(type("enter your withdraw amount \n"))
                balance = balance - withdraw_amt
                print(f"your current amout  {balance} \n")
else:
    print("pin number is wrong!!, try Again")