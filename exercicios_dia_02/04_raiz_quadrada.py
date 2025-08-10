#Faça um programa que receba um número inteiro e calcule 
# sua raiz quadrada e exiba o resultado

numero = int(input("Digite um número inteiro para calcular sua raíz quadrada -->"))
raiz = numero ** (1/2) #numero ** 0.5
raiz = round(raiz, 4)
print(f"A raíz quadrada de {numero} é {raiz}")
