print("======" "DESAFIO 18" "======")
from math import sin, cos, tan, radians
a = float(input("Digite o ângulo: "))
r = radians(a)
print("O seno de {:.2f} é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}".format(a, sin(r), cos(r), tan(r)))
