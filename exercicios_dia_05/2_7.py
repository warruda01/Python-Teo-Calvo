fruta = input("Digite uma fruta para pesquisar: ").lower()

frutas = {
    "Maçã": "1.50",
    "Banana": "1.75",
    "Uva": "1.90",
    "Pera": "1.25",
    "Laranja": "0.65",
    "Limão": "1.25",
    "Goiaba": "2.15",
    "Abacaxi": "3.20",
    "Jaca": "5.80",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido!")
