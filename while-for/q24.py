# Escreva um programa que recebe um número inteiro positivo n e exibe a soma dos dígitos de n.
n=int(input("digite um número: "))
soma=0
while n>0:
    algarismo=n%10
    soma+=algarismo
    n= n//10
print("a soma dos algarismos é:",soma)
