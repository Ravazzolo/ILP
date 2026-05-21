 #Escreva um programa que lê números inteiros do usuário enquanto o usuário não digitar 0, e ao final exibe a quantidade de números lidos (sem contar o zero).
contador=0
while True:
    num=int(input("digite o numero: "))
    if num==0:
        break
    contador+=1

print("programa encerrado!")
print("quantidade de números lidos: ",contador)