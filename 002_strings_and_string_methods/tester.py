example_string = "Hello bro"
print((example_string[0:2]) + (example_string[7:9]))

example_string2 = 'jack Is My NAME'
print(example_string2.capitalize())

example_string3 = 'Get rid of stars please*'
print(example_string3.strip('*'))

example_string4 = 'hello my name is jack'
print(example_string4.capitalize().replace('jack', 'Jack'))

var1 = 'jack'
var2 = 'hello'
var3 = 'my name is'
emp_string = f'{var2.capitalize()} {var3} {var1.capitalize()}'

byte_string = b"\316\273"
print(byte_string.decode('utf-16'))

example_string5 = "It cost me 1000.00$"
cost = float(example_string5[-8:-1])
if cost > 500:
    print(True)
else:
    print(False)
