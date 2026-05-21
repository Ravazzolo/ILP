#Escreva um programa que recebe um número inteiro positivo n e exibe n na ordem inversa dos dígitos.
n=int(input("digite um número: "))
inverso=0
while n>0:
    algarismo=n%10
    inverso=inverso*10+algarismo
    n//=10
print("a soma dos algarismos é:",inverso)
