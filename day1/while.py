lucky_num = 30
try_num = 0

while try_num < 3:
    try_num += 1
    guess_num = int(input("Please inter the guess num: "))

    if guess_num == lucky_num:
        print("lucky num",lucky_num)
        print(" Haha, You got it !")
        break
    elif guess_num < lucky_num:
        print(" Try bigger ....")
    elif guess_num > lucky_num:
        print(" Try smaller ....")

else:
    print("To many retries ...... ")