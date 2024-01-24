def tax_calcu(bill, tax_rate):
    return round((bill*tax_rate) / 100, 2)

print("Total tax:",tax_calcu(175, 15))

print("Total tax:",tax_calcu(365, 12))




