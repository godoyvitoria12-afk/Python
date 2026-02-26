#ler números até o usuário digitar 0 e somar os valores
soma = 0
cont = 0

print("Digite 0 para sair")
n = int(input("Escreva seus números: "))

while n != 0:
    soma += n
    n = int(input("Escreva seus números: "))

print("A soma dos números digitados é:", soma)