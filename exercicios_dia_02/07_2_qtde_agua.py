#Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral, será cobrado R$ 1,50
# Se o cliente escolher água mineral com gás, será cobrado R$ 2,50
# Considere a quantidade de água

#%%

texto = """ Escolha a sua água para comprar 
(1) - Água mineral - R$ 1,50 
(2) - Água mineral com gás - R$ 2,50
--> """
opcao = input(texto)
#qtd = input("Quantas águas você quer?")

valor_item = 0

if opcao == "1":
    valor_item = 1.5
    
elif opcao == "2":
    valor_item = 2.5

if valor_item == 0:
    print("Opção inválida. Entre com a opção correta.")
else:

    qtd = input("Quantas garrafas? ")
    qtd = int(qtd)
    valor_total = valor_item * qtd
    print("Sua conta deu: R$ ", valor_total)