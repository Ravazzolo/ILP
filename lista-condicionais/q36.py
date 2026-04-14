idade=int(input('digite a idade: '))
if idade<12:
    print("Criança")
elif idade<18:
    print("adolescente")
elif idade<60:
    print("Adulto")
else:
    print("idoso")