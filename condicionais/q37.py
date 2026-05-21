mês=int(input("Digite o mês: "))
verão=[12,1,2]
outono=[3,4,5]
inverno=[6,7,8]
primavera=[9,10,11]
if mês in verão:
    print("Verão")
elif mês in outono:
    print("Outono")
elif mês in inverno:
    print("Inverno")
elif mês in primavera:
    print("Primavera")
else:
    print("mês inválido")