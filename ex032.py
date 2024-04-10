print("======" "DESAFIO 32" "======"),
a = int(input("Digite um ano: "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O ano de {} é um ano bissexto!".format(a))
else:
    print("O ano de {} não é um ano bissexto!".format(a))