#%%
#Faça um programa que receba 4 alturas sando um laço
# de repetição e realize a soma dessas alturas. Use WHILE

soma=0
count = 1
while count <= 4:
    altura: float = float(input(f"Digite a altura {count} --> "))
    soma += altura
    count += 1

print(f"A soma das alturas é: {soma}")