print("======" "DESAFIO 15" "======")
kr = float(input("Quantos KM você rodou com o carro?: "))
da = int(input("Quantos dias você ficou com o carro? "))
a = da * 60
km = kr * 0.15
t = a + km
print("Você terá que pagar R${} pela quantidade de dias que ficou com o carro! \n E R${} pela quantidade de KM rodados. \n Portanto um total de R${}".format(a, km, t))
