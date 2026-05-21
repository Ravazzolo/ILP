#Escreva um programa que lê 5 números inteiros digitados pelo usuário e imprime a soma deles.
soma = 0
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    soma += num
print("A soma dos números é:", soma)