IMC=float(input(" Digite seu IMC: "))
if IMC < 18.5: 
    print("Abaixo do peso")
elif IMC< 25:
    print("Peso normal")
elif IMC< 30:
    print("Sobrepeso")
else:
    print("obesidade")