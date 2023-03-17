
frases = ['DB1 Start','Seja bem-vindo!','Ao infinito e além!','Aprender e conectar-se','Aprendendo a programar']
 
for frase in frases:
  achou = False 
  i = 0 
  while (not achou) and (i < len(frase)): 
      if i % 2 == 0: 
          i += 1 
          continue 
  
      if frase[i] == ' ': 
          achou = True 
  
      i += 1
  else:
    print(f'A frase "{frase}" foi executada {i} vezes')