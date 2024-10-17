from random import randint
num=randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
diff=[0]
while True:
    choice=int(input("Guess the number between 1 to 100:\t"))
    diff.append(abs(num-choice))
    if(choice==num):
        print(f"VOILA u guessed it corerct after {len(diff)} tries!!")
        break
    if(choice>100 or choice<0):
        print("Out of Bounds")
        continue
    if(diff[-2]):
        if(diff[-1] < diff[-2]):
            print("Warmer")
        else:
            print("Colder")
    else:
        if (diff[-1] < 10):
            print("Warm")
        else: 
            print("Cold")