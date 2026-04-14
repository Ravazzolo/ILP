n1=int(input("Digite seu número: "))
n2=int(input("Digite seu número: "))
operador=input("Digite um operador (+, -, *, /): ")
if operador== "+":
    print("resultado:", n1+n2)
elif operador=="-":
    print("resultado:", n1-n2)
elif operador=="*":
    print("resultado:", n1*n2)
elif operador=="/":
    if n2==0:
        print("erro: divisão por 0")
    else:
        print("resposta:",n1/n2)
