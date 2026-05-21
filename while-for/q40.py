#Escreva um programa que recebe um inteiro positivo n e determina se n é um número perfeito
#  (um número é perfeito se a soma de seus divisores próprios é igual a ele mesmo, ex: 6 = 1+2+3).
n=int(input("digite um número: "))
soma=0
x=1
while x<n:
    if n%x==0:
        soma+=x
    x+=1
if soma==n:
    print(f"{n} é um número perfeito")
else:
    print(f"{n} não é um número perfeito")
