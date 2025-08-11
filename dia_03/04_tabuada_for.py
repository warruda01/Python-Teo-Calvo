#Tabuada usando o For

numero: int = int(input("Qual o número da tabuada? "))
max_numero: int = int(input("Qual o número máximo? "))
for i in range(1 , max_numero+1):
    print(f"{numero} x {i} = {numero * i}")

