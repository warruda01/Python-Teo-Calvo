#Solicita um número {numero} e retorna os números pelos quais ele é
# divisível no intervalo entre 1 e o número máximo dado pelo usuário{max}

numero: int = int(input("Número a ser calculado (divisivel): "))
max: int = int(input("Número máximo a ser calculado: "))

for n in range (1, max + 1):
    if n % numero == 0:
        print(f"O número {n} é divisível por {numero}")

