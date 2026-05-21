#Escreva um programa que recebe um número inteiro base e um número inteiro positivo expoente, e calcula base ** expoente sem usar o operador ** — use apenas multiplicações repetidas com while.
base=int(input("digite a base: "))
expoente=int(input("digite o expoente: "))
resultado=1
while True :
    resultado=resultado*base
    expoente-=1
    if expoente <=0:
        break
print(resultado)