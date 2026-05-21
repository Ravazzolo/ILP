# Escreva um programa que recebe um número inteiro positivo n e imprime o produto (fatorial) de 1 × 2 × ... × n.
n=int(input("digite n: "))
multiplicação=1
if n>0:
    for i in range(1,n+1):
        multiplicação*=i
else:
    print("n deve ser positivo")
print(multiplicação)