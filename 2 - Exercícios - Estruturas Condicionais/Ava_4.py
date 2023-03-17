x = int(input('Digite x: '))
y = int(input('Digite y: '))
z = int(input('Digite z: '))

if x > y ** 2 or z < 0:  
    print('A')  
elif z != y and x % 2 == 0:  
    print('B')  
elif z > x and y // x > 3:  
    print('C')  
else:  
    print('D')  