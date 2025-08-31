#Lista:

lista = [2, 132, "wil", ["ds", "de", "da"], 3]

print(lista[2])
#%%
#Dicionários
# pares de chave/valor

dados_wil = {
    "sobrenome":"Arruda", #Chave / Valor
    "nome":"Wil",
    "filhos":True,
    "formacao":["estatistica", "bigdata", "datascience"], # Neste caso o Valor é uma lista / #Lista de formações
    "cargos": [            # Valor é uma lista e cada elemento um dicionário
        {"nome": "ds jr.", "empresa":"tapps"},
        {"nome": "ds plr.", "empresa":"sas"},
        {"nome": "ds sr.", "empresa":"boticario"},
        {"nome": "ds espec.", "empresa":"via varejo"}, 
    ]
} 

for i in dados_wil:
    print(i, "->", dados_wil[i])

#%%
print(dados_wil)
print(dados_wil["nome"]) #Acessando os itens
print(dados_wil["formacao"][-1])

print(dados_wil["cargos"][-1]["empresa"]) #última empresa 

#Acionando chave
dados_wil["estado civil"] = "casado"

print(dados_wil)

#Descobrindo os nomes das chaves:
print("Chaves:", dados_wil.keys())

#Descobrindo os valores do dicionário:
print("Valores:", dados_wil.values())

#Trazendo os pares chave/valor em formato de tupla:
print("Itens:", dados_wil.items())

for i in dados_wil:
    print(i, "->", dados_wil[i]) #O i é uma variável

dados_wil.items()



for item in dados_wil.items():
    print(item)



for [chave, valor] in dados_wil.items():
    print(chave, "->", valor)

