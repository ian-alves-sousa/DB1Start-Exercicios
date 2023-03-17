media_doacoes = float(input("Informe a média de doações dos últimos 3 anos: "))  
doacoes_atual = float(input("Informe o total de doações deste ano: ")) #C

total = doacoes_atual * 2 #A
excedente = doacoes_atual - media_doacoes #B


if doacoes_atual > media_doacoes: #E
  total += excedente * 3  #F


print(f"O total em doações será R$ {total:.2f}")  #D
