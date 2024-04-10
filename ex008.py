print("======" "DESAFIO 8" "======")
m = int(input("Digite um valor em metros: "))
km = m / 1000
hm = m / 100
dcm = m / 10
dc = m * 10
c = m * 100
mm = m * 1000
print("O valor de {}m pode ser lido como, {}km, {}hm, {} dcm, {}dc, {}cm ou {}mm".format(m, km, hm, dcm, dc, c, mm))
