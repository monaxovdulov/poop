import random
number_random=random.randint(1, 10)
attempt=0
while True:
    number_user=int(input())
    if number_random == number_user:
        print("хорош, мега хорош, мега супер пупер хорош")
        if attempt>3:
            print("лох")
    else:
        print("не хорош")
        attempt=attempt+1
        
