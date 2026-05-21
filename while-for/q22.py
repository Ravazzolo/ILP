n=int(input("digite quantas notas deseja informar: "))
contador=0
notas = []
while contador<n:
    nota=float(input("digite a nota: "))
    notas.append(nota)
    contador+=1
print("maior nota é:", min(notas))
