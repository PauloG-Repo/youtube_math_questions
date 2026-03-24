import random 
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 3

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS) #random.choice() == choose from any sequence that has index randomly

    expression = f'{str(left)} {operator} {str(right)}' 

    answer = eval(expression) #eval = evaluate. It accepts only stings
    return expression, answer

wrong = 0
input('Press any key to start')
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        guess = input(f'Problem #{i+1}: {expression} = ')
        if guess == str(answer): # make sure that you are comparing the same type. str(10) != int(10)
            break
        else:
            print('Wrong answer, try again.')
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("------------------------")
print('Nice work!!!')
print(f'Your total time is {total_time} seconds!')

#a, b = generate_problem() >>>> since our function end in 'return expression, answer',
#print(a, b)    >>>>>> it sends back two values. By putting two variables on the left side of the =, Python automatically assigns 
#               >>>>>> the first returned value (expression) to the variable (a) and the second returned value (answer) to the variable (b).

#commit on git update