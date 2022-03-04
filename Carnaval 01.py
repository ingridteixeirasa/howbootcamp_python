###
# Excercícios propostos - Diversão de Carnaval
# How Bootcamp - Python
# Autora: Ingrid Teixeira da Silva Alves
# Exercício 1





from math import log10
import math

print("Operações matemáticas com Python")

a = int(input("Digite um número inteiro A: "))
b = int(input("Digite um número inteiro B: "))

soma = a + b
diferenca = b - a
mult = a * b
quociente = a // b
resto = a % b
logaritimo_a = math.log10 (a)
exponencial =  a ** b

print(f"A soma entre eles é: {soma} ")
print(f"A diferença entre B e A é: {diferenca} ")
print(f"A multiplicação entre eles é: {mult} ") 
print(f"O quociente de A por B é: {quociente} ")
print(f"O resto da divisão de A por B é: {resto} ")
print(f"O logaritimo de base 10 de A: {logaritimo_a} ")
print(f"A elevado a B é: {exponencial} ")