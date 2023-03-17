#principal

x = int(input('Digite x: '))
y = int(input('Digite y: '))
z = int(input('Digite z: '))

print('Respostas CORRETA')
if z > x and z < y:  
    print('A')  
 
if x == y:  
    print('B')  
 
if x != y:  
    print('C')  
 
if x != y and y < 0:  
    print('D')  
    if z < 0:  
        w = "-"  
    else:  
        w = "+" 
    print(w) 

print('Resposta TESTE D')
if x < z < y: 
     print('A')   
  
if x == y: 
     print('B')  
else: 
     print('C') 
     if y < 0: 
         print('D') 
         w = '-' if z < 0 else '+'
         print(w)

print('Resposta TESTE E')
	
if x < z < y: 
     print('A') 
  
print('B') if x == y else print('C') 
  
if y < 0: 
     print('D') 
     w = '-' if z < 0 else '+'
     print(w)