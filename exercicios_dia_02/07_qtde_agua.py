#Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral, será cobrado R$ 1,50
# Se o cliente escolher água mineral com gás, será cobrado R$ 2,50
# Considere a quantidade de água

#%%

texto = """ Escolha a sua água para comprar 
(1) - Água mineral - R$ 1,50 
(2) - Água mineral com gás - R$ 2,50 --> """
opcao = input(texto)
opcao = int(opcao)
qtd = input("Quantas águas você quer?")
qtd = int(qtd)


if opcao == 1:
    print(f"Você escolheu {qtd} unidades de Água mineral")
    
    print("Total a pagar: R$ ", qtd * 1.5)
elif opcao == 2:
    print(f"Você escolheu {qtd} unidades de Água mineral com gás")
    print("Total a pagar: R$ ", qtd * 2.5)

else:
    print("Opção inválida")
# %%