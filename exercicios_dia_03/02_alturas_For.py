#%%
#Faça um programa que receba x alturas sando um laço
# de repetição e realize a soma dessas alturas. Use FOR

soma = 0
qtde_entradas: int = int(input("Qual a quantidade de entradas? "))
for n in range (qtde_entradas): #de 0 a quant. entradas fornecida
    altura: float = float(input(f"Digite a altura {n+1} --> "))
    soma += altura

print(f"Soma das alturas: {soma}")