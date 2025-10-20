import random
num=random.randint(1,100)

tries=0

while True:
    guess=int(input("Enter your num between 1 to 100 :"))

    if guess==num:
        tries+=1
        print(f"you are right in the {tries} th try")
        break
    elif guess>num:
        tries+=1
        print("Go little lower")
    elif guess<num:
        tries+=1
        print("Go little higher")
    else:
        tries+=1
        print("You are wrong")
