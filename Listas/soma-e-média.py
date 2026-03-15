# Lista para imprimir, somar, mostrar o maior e menor ...
numeros = []  # lista vazia
soma = media = contp = 0

for i in range(5):
    n = int(input("Digite um número: "))
    numeros.append(n)
    soma += n
    if n%2 == 0:
        contp += 1

maior = max(numeros) #função para encontrar o maior
menor = min(numeros) #função para encontrar o menor
media = soma/5

print("Os números digitados foram:", numeros)
print("A soma é: ", soma)
print("A média é: ", media)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"Qntd de pares: {contp}")
