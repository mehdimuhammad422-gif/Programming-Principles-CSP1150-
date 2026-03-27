import time

import random

def random_list(quantity, minimum, maximum):
    lst = []
    for i in range(quantity):
        lst.append(random.randint(minimum, maximum))
    return lst

def ask_question(question, answer):
    while True:
        userAns = input(question + " ")
        
        if userAns.isdigit():
            userAns = int(userAns)
            break
        else:
            print("Enter a number please!")

    if userAns == answer:
        print("Correct!")
        return True
    else:
        print("Incorrect! Correct answer was", answer)
        return False



print ('Enter Your Name: ')
s_name=input()
print ('Enter your roll number: ')
rollNo=input()
print(f'Welcome to {s_name} ({rollNo}) Number List Test')
print('Select the difficulty level [E]asy, [M]edium, [H]ard. ')
level=''
qNum = 0
numCount = 0    
minNum = 0
maxNum = 0
while level not in ['E', 'e', 'M', 'm', 'H', 'h']:
    level=input( )
    if level=='E' or level=='e':
        qNum = 4
        numCount = 3
        minNum = 5
        maxNum = 10
    elif level=='M' or level=='m':
        qNum = 5
        numCount = 4
        minNum = 5
        maxNum = 15
    elif level=='H' or level=='h':
        qNum = 6
        numCount = 5
        minNum = 10
        maxNum = 20
    else:
        print('Invalid input. Please select E, M, or H.')


print("Difficulty selected!")
print("Your test will have", qNum, "questions")
print("Each question will have", numCount, "numbers between", minNum, "and", maxNum)
print("Last question will be a challenge question!")
input("Press Enter to begin...")

startTime = time.time()
score = 0


for i in range(1, qNum + 1):
    print("\nQuestion", i, "of", qNum)
    print("Current Score:", score)

    if i == qNum:
        print("[!!!] Challenge Question [!!!]")
        list_quest = random_list(numCount * 2, minNum, maxNum)
    else:
        list_quest = random_list(numCount, minNum, maxNum)

    print("List:", list_quest)
randType = random.randint(1, 4)


if randType == 1:
    answer = sum(list_quest)
    result = ask_question("What is the sum of the numbers in this list?", answer)

    if result:
        score += 1

elif randType == 2:
    answer = max(list_quest) - min(list_quest)
    result = ask_question("What is the difference between the minimum and maximum numbers in this list?", answer)

    if result:
        score += 1


elif randType == 3:
    avg = sum(list_quest) // len(list_quest)
    count = 0

    for n in list_quest:
        if n > avg:
            count += 1

    answer = count
    result = ask_question(f"How many numbers in this list are higher than {avg}?", answer)

    if result:
        score += 1


else:
    x = random.randint(1, len(list_quest))
    y = random.randint(1, len(list_quest))

    while x == y:
        y = random.randint(1, len(list_quest))

    print("Positions are", x, "and", y)

    answer = list_quest[x - 1] * list_quest[y - 1]
    result = ask_question("What is the product of the numbers in these positions?", answer)

    if result:
        score += 1