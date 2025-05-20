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
