import random
def geuss():
    m = random.randint(1,100)
    while True:
        n = int(input())
        if m == n :
            print('nice geuss!')
            break
        if n != m:
            if n > m:
                print('upper than my nummber')
            elif n < m : 
                print('smaller than my number')
geuss()