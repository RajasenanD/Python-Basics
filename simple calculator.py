#simple calculator
while True:
    operation = input("Enter 'add,sub,mul,div' to do required operation: ")

    if operation != 'add' and operation != 'mul' and operation != 'sub' and operation != 'div':
        print('Enter operation only mentioned above')
        continue
    else:
        break

while True:
    try:
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
    except ValueError as e:
        print('Give number as input:...',e)
        continue
    else:
        break

def calc(a,b):
    if operation == 'add':
        return a+b
    elif operation == 'sub':
        return a-b
    elif operation == 'mul':
        return a*b
    else:
        return a/b
    

result = calc(a,b)
print(result)


'''Simple calculator

Uses if condition inside while loop to check whether the input is within add,sub,mul,div otherwise it prints 'Enter mentioned operation' and continue to ask again until required operation in entered.

Uses try and except inside while loop to check Valueerror whether the input in integer otherwise prints 'Enter number as input' otherwise continue to ask for input till number is given.

Uses function calc() to do operations mentioned in the input() using if conditions and returns the value of operations.

Call the function calc() and assign the value in a variable result.

Then prints result'''
