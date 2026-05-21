#. Escreva um programa que recebe um inteiro positivo n e verifica se ele é um palíndromo numérico
n=int(input("digite um número positivo: "))
if str(n) == str(n)[::-1]:
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")