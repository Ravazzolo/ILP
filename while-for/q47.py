#Escreva um programa que recebe um número inteiro positivo n e imprime a soma dos números de 1 a n.
n=int(input("digite n: "))
soma=0
if n>0:
    for i in range(1,n+1):
        soma+=i
else:
    print("n deve ser positivo")
print(soma)