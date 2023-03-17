num = 5  #A
 
for i in range(num): 
    linha = '' 
    for j in range(i, -1, -1): 
        linha += '* ' 
 
    print(linha) 

num = 6   #B
for i in range(num): 
    linha = '' 
    for j in range(num): 
        if (i < num // 2 and j < num // 2) or (i >= num // 2 and j >= num // 2): 
            linha += '  ' 
        else: 
            linha += '* ' 
 
    print(linha)


for i in reversed(range(1, num // 2)): #C
    print('* ' * num) if i % 2 == 0 else print(' *' * num)