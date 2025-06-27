#to check a number is prime or not
import math

while True:
    number = input('Enter a number or Enter q to quit:  ')
    
    if number == 'q':
        break
    number = int(number)
    for num in range(2, int(math.sqrt(number))+1):
       if number % num == 0:
           print(f'The number {number} is not prime number')
           break
    else:
        print(f'The number {number} is a prime')
    