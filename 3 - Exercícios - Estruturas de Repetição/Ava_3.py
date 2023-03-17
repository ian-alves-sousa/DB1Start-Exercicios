x = 0 
for i in range(1, 10): 
    x += 1 
    print(f'Execução de número {i}')
    if i % 3 == 0: 
        i += 1 
        x -= 1 
print(f'O valor de x é {x}')