import random

highest = 20
answer = random.randint(1, highest)
guess = 0

print("guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("well done you guessed it")
        break
    else:
         if guess < answer:
            print("guess higher")
         else:
            print("guess lower")
print(f"the answer was {answer}")