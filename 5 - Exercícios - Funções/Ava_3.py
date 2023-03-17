def termo_fibonacci1(termo):
    ultimo = 1
    penultimo = 1
    atual = 1

    for i in range(3, termo + 1):
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual

    return atual

def termo_fibonacci(termo):
    if termo <= 2:
        atual = 1
    else:atual = termo_fibonacci(termo - 1) + termo_fibonacci(termo - 2)
    return atual


num = int(input('Digite um número: '))
print(termo_fibonacci(num))
print(termo_fibonacci1(num))
