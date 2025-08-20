idades: list = []

while True:
    idade: str = input("Entre com a idade: ")

    if idade == "":
        break

#passar para int somente agora para usar o teste acima (vazio)
    idades.append(int(idade))

print(idades)
media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtd = len(idades)

print("MEDIA:", media)
print("MINIMO:", minimo)
print("MAXIMO:", maximo)
print("QTD:", qtd)

