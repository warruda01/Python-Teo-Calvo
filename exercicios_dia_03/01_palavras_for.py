#Faça um programa que conte quantas vezes a letra "a"
# aparece em uma palavra

palavra: str = input("Digite uma palavra: ")
soma = 0
for a in palavra:
    if a in 'aA':
        soma += 1

print(f"A letra 'a' aparece {soma} vezes na palavra {palavra}.")