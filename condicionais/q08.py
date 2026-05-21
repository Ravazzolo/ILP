idade=int(input("Diga sua idade: "))
Peixinho=[5,6,7]
Infantil_A=[8,9,10]
Infantil_B=[11,12,13]
Juvenil=[14,15,16,17]
if idade in Peixinho:
    print("peixinho")
elif idade in Infantil_A:
    print(" infantil A")
elif idade in Infantil_B:
    print("Infantil B")
elif idade in Juvenil:
    print("juvenil")
else:
    print("Adulto")
