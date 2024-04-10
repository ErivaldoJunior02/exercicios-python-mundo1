print("======" "DESAFIO 11" "======")
a = float(input("Qual a altura da sua parede?: "))
l = float(input("Qual a largura da sua parede?: "))
ar = a * l
t = ar / 2
print("Sua parede de {}m de altura, {}m de largura, com uma área de {}m2, irá precisa de {}L de tinta para pintar ela!".format(a, l, ar, t))
