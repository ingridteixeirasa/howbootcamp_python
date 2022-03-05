###
# Excercícios propostos - Diversão de Carnaval
# How Bootcamp - Python
# Autora: Ingrid Teixeira da Silva Alves
# Exercício 4
###

print("Cálculo IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print (f"Seu IMC é: {imc:.2f}")