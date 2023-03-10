row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map  = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}  ")
position = input("What postion do you want to select?")

horizontal = int(position[0])
vertical = int(position[1])
map[horizontal -1] [vertical -1 ]= int(input("Enter your desired number: "))


print(f" {row1}\n {row2}\n{row3}  ")
