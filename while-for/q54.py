#Escreva um programa que recebe um número inteiro base e um número inteiro positivo expoente, e calcula base ** expoente sem usar o operador ** — use apenas multiplicações repetidas com for.
base=int(input("digite base: "))
expoente=int(input("digite expoente: "))
resultado=1
for i in range(expoente):
   resultado*=base
print(f"{base} elevado a {expoente} = {resultado}")