# Solicitar frases, para parar de solicitar apensas tecle enter. O programa deve apresentar as
# frases e quantas vezes foi repetida
dic_frases = {}
while True:
    frase = input("Digite uma frase --> ")
    if frase == "":
        break

    if frase not in dic_frases:
        dic_frases[frase] = 1
    else:
        dic_frases[frase] += 1


for i, j in dic_frases.items():

    print(i, '-->', j )

print(20 * '-')
# OU: 

for i in dic_frases:

    print(i, '-->', dic_frases[i] )

#Ordenando os itens

print(20 * '-')

# %%
dados = {
    "oi": 1,
    "ola": 10, 
    "oi tudo bem?": 3,
    "test": 2,
    "teste": 5,
}

items = list(dados.items())
print(items)

#Ordem pela chave
#items.sort()
#print(items)

#Ordem pelo segundo elemento

items.sort(key=lambda x: x[-1])
print(items)

#Ordem pelo segundo elemento decrescente
items.sort(key=lambda x: x[-1], reverse=True)
print(items)

for i, j in items:
    print(i, "-->", j)
# %%
