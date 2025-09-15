import random 

arr = ['st','pa','sc']

win=0
lose=0
while win<3 and lose<3:
    choice = random.randint(0,2) 
    player=input('Enter your choice (st,pa,sc) : ')

    
    bot = arr[choice]
    if player==bot:
        print('draw')
    
    elif (player=='st' and bot=='pa') or (player=='pa' and bot=='sc') or  (player=='sc' and bot=='st'):
        print('lose')
        lose+=1
    
    elif (player=='pa' and bot=='st') or (player=='sc' and bot=='pa') or  (player=='st' and bot=='sc'):
        print('win')
        win+=1

    print('%s win , %s lose'%(win,lose))
    





