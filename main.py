import time

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