# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 1.99
#   1 sandwich @ $ 5.50
#   1 cake @ $ 3.25
#
#   Your total bill is $ 10.74

# Modify the line below
coffee = float(input('1 coffee @: $ '))

# Modify the line below
sandwich = float(input('1 sandwich @: $ '))

# Modify the line below
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

float(print('Your total bill is $ ', bill_total))