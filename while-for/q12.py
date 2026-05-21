#Escreva um programa que tem como entrada um número inteito contador no intervalo [1; 10]. Quando for informado o contador == 0 o programa deve encerrar. Quando o valor de contador estiver fora do intervalo, o programa deve informar que o número é inválido.
while True:
    contador = int(input("Digite um número (0 para sair): "))

    if contador == 0:
        print("Programa encerrado.")
        break
    elif 1 <= contador <= 10:
        print(f"Número válido: {contador}")
    else:
        print("Número inválido!")