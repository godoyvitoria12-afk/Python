# média das notas até digitar -1

soma = 0
cont = 0

n = int(input("Insira sua nota: "))

while n != -1:
    soma += n
    cont += 1
    n = int(input("Insira sua nota: "))


if cont > 0:
    media = soma / cont
    print("A média das notas é: ", media)

else:
    print("Nenhuma nota válida foi inserida.")
