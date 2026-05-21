#Escreva um programa que lê n notas de alunos (onde n é fornecido pelo usuário) e exibe a maior nota lida.
n=int(input("digite quantas notas deseja informar: "))
contador=0
notas = []
while contador<n:
    nota=float(input("digite a nota: "))
    notas.append(nota)
    contador+=1
print("maior nota é:", max(notas))
