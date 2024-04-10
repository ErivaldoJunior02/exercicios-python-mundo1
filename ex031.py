print("======" "DESAFIO 31" "======")
v = int(input("Quantos KM tem sua viagem?: "))
if v <= 200:
    print("Sua viagem custará R${:.2f}!".format(v * 0.5))
else:
    print("Sua viagem custará R${:.2f}!".format(v * 0.45))