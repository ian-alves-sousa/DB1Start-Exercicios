entrada1 = [(2, 4), (6, 3), (5, 10)]
entrada2 = [(4, 8), (16, 4)]
entrada3 = [(1, 2), (3, 6), (6, 12)]
lista = [entrada1, entrada2, entrada3]
for dupla in lista:
  saida = set() 
  for x, y in dupla: 
      if x < y: 
          saida.add(x) 
      else: 
          saida.add(x // y)
  print(len(saida))