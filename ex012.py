print("======" "DESAFIO 12" "======")
n = float(input("Qual o preço do produto?: R$"))
d = 5 / 100
p = n - n * d
print("O valor de R${:.2f} com o desconto de 5% passa a ser R${:.2f}".format(n, p))