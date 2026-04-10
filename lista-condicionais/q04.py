n1=int(input("Digite seu número: "))
intervalo=f"{n1} pertence ao intervalo [0,6]" if 0<=n1<=6 else f"{n1} não pertence ao intervalo [0,6]"
print(intervalo)