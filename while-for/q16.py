#Escreva um programa que lê números reais do usuário enquanto o usuário não digitar um número negativo, e ao final exibe a soma de todos os valores lidos (sem incluir o negativo).
contador=0
soma=0
while True:
    num=int(input("digite o numero: "))
    if num<0:
        break
    contador+=1
    soma+=num
print("programa encerrado!")
print("soma dos números lidos: ",soma)