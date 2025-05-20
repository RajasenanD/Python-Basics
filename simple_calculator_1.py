try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

    print('What kind of operation you want to perform:\nPress + for addion:\nPress - for subtraction:\nPress * for multiplication:\nPress / for division:')

    o = input('Enter the operation: ')
    match o:
        case "+":
            print(f'The result is {a+b}')
        case "-":
            print(f'The result is {a-b}')   
        case "*":
            print(f'The result is {a*b}')   
        case "/":
            print(f'The result is {a/b}')
except Exception as e:
    print('Enter a valid value for a and b...')