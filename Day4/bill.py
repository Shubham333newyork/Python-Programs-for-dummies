import random
test_seed = int(input("Create a seed number : "))
random.seed(test_seed)

names = input("Give me everybody names, separated by comma and space \n")
new_names = names.split(", ")

length = len(new_names)
random_choice = random.randint(0, length -1)
lucky_Person = new_names[random_choice]
print(f" {lucky_Person} is going to pay for today.  ")