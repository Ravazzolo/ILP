# Escreva um programa que recebe um número inteiro positivo n e verifica se ele é primo. Escreva um programa que recebe um número inteiro positivo n e verifica se ele é primo.
n=int(input('digite seu numero: '))
for i in range(2,n):
    if n%i==0:
        print(f"{n} não é primo")
    else:
        print(f"{n} é primo")