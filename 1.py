#Harry (Kai-Teng)
#CMPSC 131
#Project 1
#September 1st

#Defining coins
quarter = 0.25
dime = 0.1
nickel = 0.05
cent = 0.01

#Price
price = float(input("What's the price:$"))
money_paid = float(input("How much are you going to pay:$"))
change = float(format(money_paid - price, '.2f'))

#Operation
#dollar bill
number_of_1dollar_bill = int(change/1)
remainder_from_1dollarbill = float(format(change%1, '.2f'))

#quarters
number_of_quarter = int(remainder_from_1dollarbill/0.25)
remainder_from_quarter = float(format(remainder_from_1dollarbill%0.25, '.2f'))

#dimes
number_of_dime = int(remainder_from_quarter/0.1)
remainder_from_dime = float(format(remainder_from_quarter%0.1, '.2f'))

#nickel
number_of_nickel = int(remainder_from_dime/0.05)
remainder_from_nickel = float(format(remainder_from_dime%0.05, '.2f'))

#cent
number_of_cent = int(remainder_from_nickel/0.01)


#Output
if money_paid == price:
    print("You're good to go.")
elif money_paid < price:
    print("The money is not enough. You still need to pay", format(price-money_paid, '.2f'), "dollar more.")
else:
    print("Returned $", change)
    print(number_of_1dollar_bill, ("dollars ($1)"))
    print(number_of_quarter, "quarters ($0.25)")
    print(number_of_dime, "dimes ($0.1)")
    print(number_of_nickel, "nickel ($0.05)")
    print(number_of_cent, "cents ($0.01)")








