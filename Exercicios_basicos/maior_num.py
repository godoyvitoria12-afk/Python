# ler o maior num, e mostrar qual é o maior e o menor

print("Digite 0 para sair")

n = int(input("Digite um número: "))
maior = n

while n != 0:
    if n > maior:
        maior = n
    n = int(input("Digite um número: "))

print("O maior número digitado foi:", maior)