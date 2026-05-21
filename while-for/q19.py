# Escreva um programa que imprime os primeiros n termos da progressão aritmética com primeiro termo a e razão r, onde n, a e r são fornecidos pelo usuário.
n=int(input("digite n: "))
r=int(input("digite razão: "))
a=int(input("digite a: "))
contagem=0
while True:
    print(a)
    a+=r
    contagem+=1
    if contagem==n:
        break

