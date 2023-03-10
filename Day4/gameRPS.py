import random


select_User = int(input("What do you wanna choose ?"))


select_Com = random.randint(0,2)
print(select_Com)


if select_User ==0 and select_Com==2:
    print("You won.")
elif select_User==1 and select_Com==0:
    print("You won.")
elif select_User==2 and select_Com==1:
    print("You won.")
else:
    print("You lost.")