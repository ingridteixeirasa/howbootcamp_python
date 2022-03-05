###
# Excercícios propostos - Diversão de Carnaval
# How Bootcamp - Python
# Autora: Ingrid Teixeira da Silva Alves
# Exercício 2-6
###


lista = ["Olá", " ", "Ingrid", " ", "Phyton", " "]

conta_vazio = lista.count(" ")

for i in range(0, conta_vazio):
    lista.remove(" ")

print(lista)