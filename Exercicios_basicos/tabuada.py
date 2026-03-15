a = int(input("Insira um número: "))

for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")
    # OU
    # print(a, "x", i, "=", a * i)

print("-----------------")
# tabuada somente para números pares
for i in range(0, 11, 2):
    print(f"{a} x {i} = {a * i}")