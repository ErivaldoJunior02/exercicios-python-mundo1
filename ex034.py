print("======" "DESAFIO 34" "======")
s = float(input("Qual o valor do seu salário?: R$"))
if s > 1250:
    print("Você terá uma aumento de 10%, portanto R${}!".format(s + s * 10/100))
else:
    print("Você terá um aumento de 15%, portanto R${}!".format(s + s * 15/100))