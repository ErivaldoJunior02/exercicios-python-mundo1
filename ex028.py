import random
print("======" "DESAFIO 28" "======")
n = int(input("Tente adivinhar qual número pensei entre 0 e 5: "))
s = random.randint(0,5)
print("O número que pensei foi {}".format(s))
if n == s:
    print("Você acertou!!")
else:
    print("Você errou, tente denovo!")

