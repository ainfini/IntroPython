
'''
Zaineb Halibi
Homework 2
Neal Terrell
Here's One For You, Nineteen For Me  '''


taxable = int(input("What is your 2019 taxable income ?"))
 
if (0 <= taxable <= 9700):
    bracket = taxable - 0
    taxed = bracket * .10
    taxrate = round(((taxed / bracket) * 100),1)

    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

elif ( 97001 <= taxable <= 39475):
    bracket = taxable - 9700
    taxed = 970 + bracket * .12
    taxrate = round(((taxed / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

    
elif ( 39476 <= taxable <= 84200):
    bracket = taxable - 39475
    taxed = 4543 + bracket * .22
    taxrate = round(((taxed / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

elif ( 84201 <= taxable <= 160725):
    bracket = taxable - 84200
    taxed = 14382 + bracket * .24
    taxrate = round(((taxed / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

elif ( 160726 <= taxable <= 204100):
    bracket = taxable - 160725
    taxed = 32748 + bracket * .32
    taxrate = round(((taxed / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

elif ( 204101 <= taxable <= 510300):
    bracket = taxable - 204100
    taxed = 46628 + bracket * .35
    taxrate = (taxed / taxable) * 100
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

elif (510301 < taxable > 10000000):
    bracket = taxable - 10000000 
    taxed = 3664987 + bracket * .70
    taxrate = round(((taxed / taxable) * 100),1)
    
    bracket1 = taxable - 510300
    taxed1 = 153798 + bracket1 * .37
    taxrate1 = round(((taxed1 / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed1))
    print("Your effective tax rate is {}%".format(taxrate1))
    print()
    print("With a new 70% bracket, your tax liability would be ${:,.2f}".format(taxed))
    print("Your effective tax rate with the new bracket would be {}%".format(taxrate))

elif (510301 > taxable) :
    bracket = taxable - 510300
    taxed = 153798 + bracket * .37
    taxrate = round(((taxed / taxable) * 100),1)
    
    print("Your tax liability is ${:,.2f}".format(taxed))
    print("Your effective tax rate is {}%".format(taxrate))

   
