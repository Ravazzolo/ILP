#Escreva um programa que simula um jogo de adivinhação: o programa sorteia um número inteiro entre 1 e 100 e o usuário tenta adivinhar. A cada tentativa o programa informa se o chute foi "muito baixo", "muito alto" ou "acertou!". O laço termina quando o usuário acertar.
import random
random.randint(1, 100)
while True:
    chute=int(input("digite seu chute: "))
    if chute<random.randint(1, 100):
        print("muito baixo")
    elif chute>random.randint(1, 100):
        print("muito alto")
    else:
        print("acertou!")
        break
