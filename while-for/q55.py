# Escreva um programa que recebe dois inteiros positivos a e b (com a < b) e imprime todos os inteiros no intervalo [a, b].
a=int(input("digite a: "))
b=int(input("digite b: "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    print("a precisa ser menor que b")