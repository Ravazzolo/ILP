# Escreva um programa que imprime os primeiros 15 termos da sequência: 1, 3, 5, 7, 9, ...
contagem=0
i=1
while True:
    print(i)
    i+=2
    contagem+=1
    if contagem>=15:
        break
