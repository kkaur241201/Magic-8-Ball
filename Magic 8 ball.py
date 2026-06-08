import random
question = input("Ask magic 8 ball a question")
answer = random.randint(1,8)
if answer == 1:
    print("it is certain")
elif answer == 2:
    print("outlook good")
elif answer == 3:
    print("you may rely on it")
elif answer == 4:
    print("Ask again later")
elif answer == 5:
    print("concentrate and ask again")
elif answer == 6:
    print("reply hazy, try again")
elif answer == 7:
    print("my reply is no")
elif answer == 8:
    print("my sources say no")
else:
    print("That's not a question")
print("The end")