def calcular_imc(peso: float, altura: float) -> float:

    imc = peso / (altura ** 2)

    return imc


print(calcular_imc(1.8, 80))
print(calcular_imc(altura=1.8, peso=80))
#calcular_imc(80)
print(calcular_imc(80, altura=1.8))
#calcular_imc("80", 1.8)
