velocidade = int(input("Informe a velocidade média: "))
tempo = input("Informe o tempo da viagem: ")
distancia = velocidade * tempo 
consumo = distancia / 8  
print(f"Serão necessários {consumo:.1f}l de combustível")