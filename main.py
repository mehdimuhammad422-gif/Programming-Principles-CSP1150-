print ('Enter Your Name: ')
s_name=input()
print ('Enter your roll number: ')
rollNo=input()
print(f'Welcome to {s_name} ({rollNo}) Number List Test')
print('Select the difficulty level [E]asy, [M]edium, [H]ard. ')
level=input()
if level=='E' or level=='e':
    print('Easy')
elif level=='M' or level=='m':
    print('Medium') 
elif level=='H' or level=='h':
    print('Hard')
else:
    print('Invalid input. Please select E, M, or H.')