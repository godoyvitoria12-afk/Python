# imprimir a ordem inversa de uma sequência 

n = int(input("Insira um para para exibir a sequência: "))

for n in range(n, 0, -1):
    print(n, end="|")
