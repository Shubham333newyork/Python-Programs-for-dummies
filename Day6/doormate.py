def Doormate(rows,columns):
    width = columns
    for i in range(0,int(rows/2)):
        pattern = '.|.' * ((i*2)+1)
        print(pattern.center(width,'-'))
    print('WELCOME'.center(width,'-'))
    i = int(rows /2)
    while i >0:
        pattern = '.|.' * ((i*2) - 1)
        print(pattern.center(width,'-'))
        i = i- 1
    
rows, columns = map(int, input().split())
Doormate(rows,columns)
    