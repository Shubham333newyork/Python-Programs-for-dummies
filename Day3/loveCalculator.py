print("Welcome to world of love ")
name1 = input("What's your full name? ")
name2 = input("What's your girlfriend name?")
name = name1 + name2

t = name.lower().count("t")
r = name.lower().count("r")
u = name.lower().count("u")
e = name.lower().count("e")

true = t + r + u + e

l = name.lower().count("l")
o = name.lower().count("o")
v = name.lower().count("v")
e = name.lower().count("e")

love = l + o + v + e

score = int(str(true)+str(love))

if score>90 or score<10:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif 40<=score<=50:
    print(f"Your score is {score},you are alright together. ")
elif score>75 and score<80:
    print(f"Your score is {score}, you can make this sexy girl as your girlfriend. ")
elif score>80 :
    print(f"Your score is {score}, You can do sex with your girlfriend.")
else:
    print(f"Your score is {score} ")