print("Welcome to the Code Cafe! \n __________")
print("(for Yes and No questions use 0 and 1 as answers.)\n __________")
import time 
Drinks={
    "Latte": 4.50,
    "Americano": 3.50,
    "Cappuccino": 3.75,
    "Chai":3.50,
    "Matcha": 4.50}
Food={
    "Scone":3.29,
    "Pumpkin Muffin": 3.50,
    "Croissant": 2.20,
    "Danish": 3.30,
    "Bagel": 4.50}
Payment={
    "Dollar":1.00,
    "Quarter":0.25,
    "Dime":0.10,
    "Nickel":0.05,
    "Penny":0.01,}

Total= 0.00

#running menu 
print("Here's the menu: \n")
for key in Drinks.keys():
    print(f" \n {key}\n _____")
for key in Food.keys():
    print(f" \n {key}\n _____")

    
Choice=input(" \n What would you like?>> \n")


#First choice
if Choice in Drinks:
    cost=(Drinks[Choice])
    Total+=cost
    Milk_opt= int(input('''Would you like another type of milk?
We have Oat, Soy, Whole or Almond? They are .50 extra.'''))
    if Milk_opt==True:
        Total+=0.50
        print(f"{Choice}, Sure! That will be {Total} dollars")
    elif Milk_opt== False:
        Total+=0
elif Choice in Food:
    cost=(Food[choice])
    Total+=cost
    print(f"{Choice}, Sure! That will be {cost}.")
else:
     print("Thats not a Choice sorry!")

# if they have a second Choice


Choice2=int(input("would you like anything else?"))


if Choice2==False:
    Cust_Payment=input(f"Your total will be {Total}. Will that be cash or card?")
else:
    Choice3=input("What else could I get you?")
    if Choice3 in Drinks.keys():
            cost2=(Drinks[Choice3])
            Total+=cost2
            Milk_opt2= int(input('''Would you like another type of milk?
We have Oat, Soy, Whole or Almond? They are .50 extra.'''))
            if Milk_opt2==True:
                Total+=0.50
                print(f"{Choice3}, Sure! That will be {Total} dollars")
            elif Milk_opt2== False:
                Total+=0
    elif Choice3 in Food:
        cost=(Food[Choice3])
        Total+=cost
        print(f"{Choice3}, Sure! That will be {cost}.")
    else:
         print("Thats not a Choice sorry!")
                  
if Cust_Payment=="cash" or "Cash":
    print("Cash? Sure thing, how much of each of these will you give me?")
    Cash_List=[int(n) for n in input("Dollars:____ \nQuarters:____\nDimes:____\nNickels:____\nPenny:____").split()]
    print(Cash_List)
    
    Total-= Cash_List[0]*(Payment["Dollar"])
    Total-= Cash_List[1]*(Payment["Quarter"])
    Total-= Cash_List[2]*(Payment["Dime"])
    Total-= Cash_List[3]*(Payment["Nickel"])
    Total-= Cash_List[4]*(Payment["Penny"])
    if Total>0.00:
        Cash_List=[int(n) for n in input(f"That wasn't enough, Your total is still {Total}").split()]
        Total-= Cash_List[0]*(Payment["Dollar"])
        Total-= Cash_List[1]*(Payment["Quarter"])
        Total-= Cash_List[2]*(Payment["Dime"])
        Total-= Cash_List[3]*(Payment["Nickel"])
        Total-= Cash_List[4]*(Payment["Penny"])
    
elif Cust_Payment=="Card" or "card":
    Pin=input("Please insert your card pin:____\n(four digets)\n")
    while Pin != "1234":
        Pin=input("Try again! \n(four digets)\n")
    if Pin == "1234:
        print("Card Processing"
        time.sleep(1)
        print("Processing..."
        time.sleep(3)
        print("Payment Accepted!")
        Total-=Total
              
if Total>0.00:
    New_Payment=int("That wasnt enough, Will you give me the rest of the payment?\n (0 for no 1 for yes)")
    if New_Payment== Tr
elif Total >0.00:
    Total*= -1
    print("Perfect! heres your items and Heres your change: {Total}")
    if Choice in Drinks:
        print('''   ( ) (
                       ________
                       \ ~~~~ /_
                        \    / _)
                         ----''')
    else:
        print('''  ) ( )
                 ________
                /       /)
               |        |
               | bakery |
               /  ~~~~   \
               |_________|''')
elif Total==0.00:
    print("Perfect! heres your items:")
    if Choice in Drinks:
        print('''   ( ) (
                       ________
                       \ ~~~~ /_
                        \    / _)
                         ----''')
    else:
        print('''  ) ( )
                 ________
                /       /)
               |        |
               | bakery |
               /  ~~~~   \
               |_________|''')
    
    
        

    
    


     
