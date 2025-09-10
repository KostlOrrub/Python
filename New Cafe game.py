print("Welcome to the Code Cafe! \n __________")
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

Total= 0.00

#running menu 
print("Here's the menu: \n")
for key in Drinks.keys():
    print(f" \n {key}\n _____")
for key in Food.keys():
    print(f" \n {key}\n _____")

    
Choice=input(" \n What would you like?>> \n")

if Choice in Drinks:
    cost=(Drinks[Choice])
    Total+=cost
    Milk_opt= bool(input('''Would you like another type of milk?
We have Oat, Soy, Whole or Almond? They are .50 extra.'''))
    if Milk_opt==True:
        Total+=0.50
    print(f"{Choice}, Sure! That will be {Total} dollars")
elif Choice in Food:
    cost=(Food[choice])
    Total+=cost
    print(f"{Choice}, Sure! That will be {cost}.")
else:
     print("Thats not a Choice sorry!")
        
Choice=bool(input("would you like anything else?"))


if Choice==False:
    print(f"Your total will be {Total}. Will that be cash or card?")
else:
    choice2=input("What else could I get you?)
    if Choice in Drink.keys():
                  cost2=(Drinks



     
