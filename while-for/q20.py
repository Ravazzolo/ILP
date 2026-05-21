#. Escreva um programa que calcula e exibe a soma: 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, onde n é fornecido pelo usuário.
n=int(input("digite n: "))
soma=0
denominador=1
contagem=0
while denominador<=n:
    soma+=1/denominador
    denominador+=1
print("a soma é:",soma)
    

    