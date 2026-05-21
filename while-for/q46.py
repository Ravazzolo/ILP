# Escreva um programa que recebe um número inteiro positivo n como entrada e imprime todos os inteiros de 1 a n.
n=int(input("digite n: "))
if n>0:
    for i in range(1,n+1):
        print(i)
else:
    print("n deve ser positivo")