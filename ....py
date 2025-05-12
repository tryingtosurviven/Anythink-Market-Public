#Rock,Paper,Scissors
'''
Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
'''
import random

choice = {1:'✊', 2:'✋', 3:'✌️', 4:' 🦎',5:' 🖖'}

while True:
    p1 = int(input('enter 1 to 5: '))
    if p1 not in choice:
        print('invalid, try again')
        continue
    else:
        print(f"you choose {choice[p1]}")
    
    com = random.randint(1,5)
    print(f"com choose {choice[com]}")

    if p1 == com:
        print('draw')
    elif (p1 == 3 and com == 2) or (p1 == 2 and com == 1) or (p1 == 1 and com ==4) or (p1 == 4 and com == 5) or (p1 == 5 and com == 3) or (p1==3 and com == 4) or (p1==4 and com == 2) or (p1==2 and com == 5) or (p1==5 and com==1) or (p1==1 and com== 3):
        print("player 1 win")
    else:
        print("computer win")

    playagain = input('play again? Y/N: ').lower()
    if playagain == 'n':
        break
    
    