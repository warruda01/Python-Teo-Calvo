# Faça um programa que receba uma quantidade indefinida de valores
#correspondentes a "Saldo em Conta", mas quando o usuário apertar 
# "enter" sem digitar valor algum o program para de receber valores
# e exibe a soma de todos os valores digitados anteriormente

saldo_total = 0

while True:
    saldo = input("Saldo em Conta --> ")
    if saldo == "":
        break
    
    saldo_total += float(saldo)

print(f"Somatório: {saldo_total}")
