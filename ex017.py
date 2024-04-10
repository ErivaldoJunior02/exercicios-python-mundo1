print("======" "DESAFIO 17" "======")
from math import hypot
o = float(input("Digite o valor do cateto oposto: "))
a = float(input("Digite o valor do cateto adjacente: "))
h = hypot(o, a)
print("Com o cateto oposto de {} e o cateto adjacente de {} a hipotenusa será de {:.2f}!".format(o, a, h))
