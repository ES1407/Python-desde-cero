def suma(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(suma(4,5,6))


def suma(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


print(suma(coffe=2.99, cake=5.00, juice=1.75))

nums = 34
for i in nums:
 print(i)