#Aluno: Ian Alves Sousa
#DB1 Start - Estruturas Condicionais
#Exercício 15 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Digite uma data válida, no formato dd/mm/aaaa: ')
  
if data[2] == '/' and data[5] == '/':
  data_lista = data.split('/')
  dia = len(data_lista[0])
  mes = len(data_lista[1])
  ano = len(data_lista[2])

  try:
    tipoDia = int(data_lista[0])
    tipoMes = int(data_lista[1])
    tipoAno = int(data_lista[2])
    lista31 = [1,3,5,7,8,10,12]
    lista30 = [4,6,9,11]

    if dia == 2 and mes == 2 and ano == 4 and data[2] == '/' and data[5]:
      
      if (tipoDia < 32 and tipoMes < 13) and ((tipoMes in lista31) or (tipoMes == 2 and (tipoDia <= 28 or (tipoDia <= 29 and (tipoAno % 4) == 0))) or (tipoMes in lista30 and tipoDia <= 30)):
        print(f'A data {data} que você digitou tem um formato válido.')
      else:
        print(f'A data que você digitou tem um formato válido, mas ela não existe.')
      
    else:
      print(f'A data que você digitou não tem um formato válido.')

  except ValueError:
    print('Você digitou uma data inválida. Tente novamente.')  
    
else:
  print(f'A data que você digitou não tem um formato válido.')
