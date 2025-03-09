import random
X = 0
top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("Please type a number bigger than 0")
        quit()
else:
    print("Please type a digit")
    quit()

num = random.randint(0,top_of_range)
# print(num)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a digit")
        continue
    if user_guess == num:
        print("You got it!")
        break
    elif X < 4:
        print("Try Again")
        X += 1
    else:
        print("you lose")
        quit()

