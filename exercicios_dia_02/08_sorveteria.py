

total = 0.00
print(8 * '-', "Sorveteria", 9 * '-')
print(10 * '-', "Preços:",10 * '-')

#Escolha do tipo de sorvete
print(6 * '-', "Tipo de Sorvete", 6 * '-')
print("(1) Casquinha: R$ 1,00")
print("(2) Cascão:    R$ 2,50")
print("(3) Cestinha:  R$ 4,00")

while True:
    tipo:int = int(input("Escolha o tipo de sorvete --> "))

    if tipo == 1 or tipo == 2 or tipo == 3:
        
        if tipo == 1:
            tipo = 'uma Casquinha'
            total += 1.00

        elif tipo == 2:
            tipo = 'um Cascão'
            total += 2.50

        elif tipo == 3:
            tipo = 'uma Cestinha'
            total += 4.00
        break
    else:
        print("Opção inválida. Favor escolher 1, 2 ou 3.")

#Escolha do sabor do sorvete
print(30 * '-')
print(12 * '-', "Sabor", 11 * '-')
print("(1) Morango")
print("(2) Creme")
print("(3) Chocolate")

while True:
    sabor:int = int(input("Escolha o sabor --> "))

    if sabor == 1 or sabor == 2 or sabor == 3:
        
        if sabor == 1:
            sabor = 'Morango'

        elif sabor == 2:
            sabor = 'Creme'

        elif sabor == 3:
            sabor = 'Chocolate'
        break
    else:
        print("Opção inválida. Favor escolher 1, 2 ou 3.")

#Escolha da cobertura do sorvete
print(30 * '-')
print(10 * '-', "Cobertura", 9 * '-')
print("(1) Caramelo:      R$ 1,50")
print("(2) Morango:       R$ 1,50")
print("(3) Chocolate:     R$ 1,50")
print("(4) Sem Cobertura: R$ 0,00")


while True:
    cobertura:int = int(input("Escolha a cobertura --> "))

    if cobertura == 1 or cobertura == 2 or cobertura == 3 or cobertura == 4:
        if cobertura == 1:
            cobertura = 'Caramelo'
            total += 1.50

        elif cobertura == 2:
            cobertura = 'Morango'
            total += 1.50

        elif cobertura == 3:
            cobertura = 'Chocolate'
            total += 1.50

        elif cobertura == 4:
            cobertura = 'Sem Cobertura'
        break
    else:
        print("Opção inválida. Favor escolher 1, 2, 3 ou 4.")

    
    
print(f"Você comprou {tipo}, sabor {sabor} ", end="")

if cobertura != 'Sem Cobertura':

    print(f"com cobertura de {cobertura}.")
else:
    print(f"{cobertura}")
print(f"Total a pagar: R$ {total}")