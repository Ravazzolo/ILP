velocidade=int(input("Digite a velocidade: "))
if velocidade<=80:
    print("sem multa")
elif velocidade<=100:
    print("Multa leve: R$ 130")
elif velocidade<=120:
    print("Multa média: R$ 195")
else:
    print("Multa grave: R$ 293 + suspensão")