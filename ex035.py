print("======" "DESAFIO 35" "======")
p = float(input("Digite o tamanho de uma reta: "))
s = float(input("Digite o tamanho de outra reta: "))
t = float(input("Digite o tamanho de mais uma reta: "))
if p < s + t and s < p + t and t < p + s:
    print("Essas retas podem formar um TRIÂNGULO!")
else:
    print("Essas retas NÃO podem formar um TRIÂNGULO!")