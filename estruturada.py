def auto ():
    a = str(input("Diga se o auto em questão possui portas, Sim ou Não?\n")).upper()
    if a == "SIM":
        print("É um carro e possui quatro portas!")
    elif a == "NÃO":
        print("É uma moto e possui duas rodas!")
    else:
        print("Não é uma resposta válida")
auto()
