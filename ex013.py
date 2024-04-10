print("======" "DESAFIO 13" "======")
s = float(input("Qual o valor do seu salário?: R$"))
a = 15 / 100
n = s + s * a
print("O seu salário no valor de R${:.2f} com o aumento de 15%, ficará no valor de R${:.2f}".format(s, n))
