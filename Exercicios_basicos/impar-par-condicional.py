#IMPAR OU PAR
contp = 0
conti = 0
n = 0

while n != -1:
    n = int(input("Insira un número: "))
    if n%2 == 0:
        contp += 1

    else:
        conti += 1

print("Qntd de pares: ", contp)
print("Qntd de ímpares: ", conti)