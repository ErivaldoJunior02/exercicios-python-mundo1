print("======" "DESAFIO 29" "======")
v = int(input("Qual a velocidade do carro?: "))
if v > 80:
    print("Você foi receberá uma multa!")
    print("A multa será de R${:.2f}!".format((v - 80) * 7))
else:
    print("Está tudo certo, pode continuar sua viagem!")