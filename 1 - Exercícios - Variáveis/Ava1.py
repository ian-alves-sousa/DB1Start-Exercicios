tempC = float(input('Informe a temperatura em C: ')) 
tempF = tempC * 1.8 + 32

print(f'A temperatura em F é: {tempF}') #Correta

#print(f'A temperatura em F é: {tempF:.f}') #Incorreta

print('A temperatura em F é: ' + str(tempF)) #Correta

print(f'A temperatura em F é: {tempF:.1f}') #Correta

print('A temperatura em F é: {}'.format(tempF)) #Correta