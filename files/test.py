# a file to test the actual calculator algorithm

def calc(txt:str):
    pass

print("please enter what you want to be calculated:")
text = input("-> ")

OPERATORS = {"+":"addition",
              "-":"subtraction",
              "/":"devision",
              "*":"multiplication"}

operations = []

numbers = []

current_number = ""

for char in text:
    if char in OPERATORS:
        operations.append(char)
        numbers.append(current_number)
        current_number = ""
    else:
        current_number += char

numbers.append(current_number)

print(numbers, operations)