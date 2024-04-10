print("======" "DESAFIO 33" "======")
p = float(input("Digite um número: "))
s = float(input("Digite outro número: "))
t = float(input("Digite mais um número: "))
if p < s and p < t:
    m = p
if s < p and s < t:
    m = s
if t < p and t < s:
    m = t
if p > s and p > t:
    ma = p
if s > p and s > t:
    ma = s
if t > p and t > s:
    ma = t
print("O menor número informado foi {}!".format(m))
print("O maior número informado foi {}!".format(ma))