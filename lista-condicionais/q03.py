n1=int(input("Digite seu número: "))
n2=int(input("Digite outro número: "))
paridade="soma é par" if (n1+n2)%2==0 else "soma é impar"
print(paridade)