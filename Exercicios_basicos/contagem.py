# Contagem condicional

x = int(input("Coloque um número: "))

for i in range(x, 0, -1):
    print(i, end="|")

print("\n\nMúltiplos:")

# somente múltiplos de 3
for i in range(1, x + 1):
    if i % 3 == 0:
        print(i, end="|")