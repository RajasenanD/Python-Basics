questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]
i = 0
for question in questions:
  
    print(question[0])
    print(f'1. {question[1]}')
    print(f'2. {question[2]}')
    print(f'3. {question[3]}')
    print(f'4. {question[4]}')

    a = int(input('Enter the correct option: '))
    if a == question[5]:
        print('Correct answer')
      
    
    else:
        print(f'The correct answer is {question[5]}')
        print(f'Better luck next time')
        break

 
    print(f'You won {prizes[i]} rupees !!\n')
    i+=1
'''
millionaire is a game , asking question and take answer as input, if the answer is correct then it prints that answer is correct and also 
prints the prize money for that answer, the prize money is increases for each question which are answered correctly.

- Uses a nested list to frame questions and answer, inorder to select answer using index position, the answer is given in last index.
- Uses for loop for iteratet list , and assign 'a' variable as input to get answer if it equals to last index of each list then
the answer is correct otherwise it prints the correct answer and breaks the loop.
- And also for each answer the prize money increases, by assinging prizes in a list to fetch using index , by assigning i =0 then 
using increment operator to increase the index for each correct answer.
'''
