#Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral, será cobrado R$ 1,50
# Se o cliente escolher água mineral com gás, será cobrado R$ 2,50

#%%

texto = """ Escolha a sua água para comprar 
(1) - Água mineral - R$ 1,50 
(2) - Água mineral com gás - R$ 2,50 --> """

opcao = input(texto)
opcao = int(opcao)

if opcao == 1:
    print("Você escolheu Água mineral")
    print("Total a pagar: R$ 1,50")

elif opcao == 2:
    print("Você escolheu Água mineral com gás")
    print("Total a pagar: R$ 2,50")

else:
    print("Opção inválida")
# %%
