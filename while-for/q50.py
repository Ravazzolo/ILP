#Escreva um programa que lê 10 números reais digitados pelo usuário e imprime a média aritmética.
média=0
soma=0
for i in range(10):
    num = float(input("Digite um número inteiro: "))
    soma+=num
    média=soma/10
print("A média aritmética dos 10 números é:", média)