#Fizz Buzz: Print numbers from 1 to 100. For multiples of 3 print “Fizz”, for 5 print “Buzz”, and for both print “FizzBuzz”.
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0 :
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
    