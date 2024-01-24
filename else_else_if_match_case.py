#Control flow: orden en el que se ejecutan las cosas
bill_total = 201
bill_discount = 10
bill_discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100 ")
    bill_total = bill_total-bill_discount
elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total-bill_discount2
else:
    print("Bill is less than 100")


print("Your total bill is " + str(bill_total))


kylo = int(input("Inserte un numero:"))

match kylo:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 500 | 501:
       print("Server Error")
    case _:
        print("Unknown")