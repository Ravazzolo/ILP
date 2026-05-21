# Escreva um programa que recebe dois inteiros positivos a e b e calcula o Máximo Divisor Comum (MDC) usando o algoritmo de Euclides com for.
a=int(input("digite a: "))
b=int(input("digite b: "))
divisores=[]
for i in range(1,max(a,b)+1):
    if a%i==0 and b%i==0:
        divisores.append(i)
MDC=max(divisores)
print(f"MDC de {a} e {b} = {MDC}")