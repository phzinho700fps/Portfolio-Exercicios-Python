#input de números, usando float para aceitar números inteiros e decimais
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))



#aqui é onde o usuário escolhe qual operação ele gostaria de realizar, bastando escolher um dos números
print("1 - SOMA")
print("2 - SUBTRAÇÃO")
print("3 - MULTIPLICAÇÃO")
print("4 - DIVISÃO")

resultado = int(input("digite a operação desejada: "))


#aqui começa as condicionais, de acordo com a escolha do usuário de qual operação ele vai realizar. Além de que aqui que realiza as operações matemáticas com bases nos números dos inputs.
if resultado == 1:
    print(f"O resultado da soma entre {numero1} e {numero2} é: {numero1 + numero2}")
elif resultado == 2:
    print(f"O resultado da subtração entre {numero1} e {numero2} é: {numero1 - numero2}")
elif resultado == 3:
    print(f"O resultado da multiplicação entre {numero1} e {numero2} é: {numero1 * numero2}")
elif resultado == 4:
    if numero2 != 0:
        print(f"O resultado da divisão entre {numero1} e {numero2} é: {numero1 / numero2}") 
    else:
        print("para divisão, o segundo número não pode ser zero!")
else:
    print("escolha uma operação dentre as 4 opções...")