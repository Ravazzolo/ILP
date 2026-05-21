#Escreva um programa que recebe dois inteiros positivos a e b (com a < b) e imprime todos os inteiros no intervalo [a, b].
a=int(input("digite a: "))
b=int(input("digite b: "))
if a>b:
    print("erro")
else:
    while a<=b:
     print(a)
     a+=1
