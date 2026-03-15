# ler numeros do usuário até ele digitar 0
n = int(input("Escreva seus números: "))

while n != 0:
    print("Os numeros são: ", n)
    n = int(input("Digite 0 para sair!"))
