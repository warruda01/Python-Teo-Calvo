# %%
# Uma maneira de definir listas:
idades = [28, 42, 43, 35, 39, 28, 38]

#Está carregando elementos int
print(idades)
print(idades[0])

#listas não são arrays
# %%
# Cada item está em uma posição
wil = ["Wilber", "Arruda", 47, True, "casado", 5200]
print(wil)

# %%
type(wil)
type(wil[0])
# %%

#somando todas as idades
idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

print(f"soma idades: {sum(idades)}")

print(f"media idades: {sum(idades) / len(idades):.2f}")

print(f"menor idade: {min(idades)} ")

print(f"maior idade: {max(idades)} ")
# %%
wil = ["wil", 47, 
       True, "Casado", 
       ["estagiario", "ds jr.", "ds pl", "ds sr.", "head"],
       [1500, 4000, 4550, 6500, 10000],
       ["Ana", "Maria", "Ingrid"]]

print(wil[6][0]) #Vai imprimir a posição 4 da lista dentro da lista

exs = wil[6] #Pegará a lista dentro da lista e jga em exs
primeira_ex = exs[0] #pegará a posição 0 da nova lista
print(primeira_ex)
# %%
#Ajustando para sempre pegar a lista de nomes se estiver na última posição
tamanho = len(wil)
pos = tamanho-1
print(wil[-1][-1]) #Último elemento da lista  dentro da lista

#%%
#Fatiamento:

#Pegar os três primeiros elementos de uma lista
print(wil[:3])

#Pegar dois últimos traballhos da lista:
print(wil[4][-2:])

#wil[start : stop]  - se ocultar o start ele entenderá queo dois pontos já é o início

# %%

#Evolução do salário em ordem inversa
#Definindo salários:
salarios = wil[5]

#Apresentando na ordem inversa:
print(salarios[::-1]) #Padrão é de 1 em 1. MAs pode ser 2 em 2
# wil[start : stop: step]