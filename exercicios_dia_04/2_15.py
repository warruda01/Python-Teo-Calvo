#Escreva um programa que receba uma lista de números do usuário e conte
# quantas vezes um número específico aparece na lista. Solicita ao usuário
# um número e exiba a contagem.
lista: list = []

n: int = int(input("Qual a quantidade de números? "))
proc: int = int(input("Qual o número a ser procurado? "))
for i in range (0, n):
    numero: int = int(input(f"Digite o número {i+1}--> "))
    lista.append(numero)

soma = lista.count(proc)

print(f"O número {proc} se repete por {soma} vezes na lista")

#Usando for:
soma = 0
for elemento in lista: #Elemento assume cada item da lista
    if elemento == proc:
        soma += 1

print(f"O número {proc} se repete por {soma} vezes na lista")

