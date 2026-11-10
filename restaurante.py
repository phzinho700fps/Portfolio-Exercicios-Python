#Restaurante Python, faça seu pedido!

comidas = ["lasanha", "feijoada", "frango a parmegiana", "bife a milanesa"]
precos = [35, 40, 30, 30]

print("lasanha - 0 / feijoada - 1 / frango a parmegiana - 2 / bife a milanesa - 3")

pedido = int(input("Digite o número do seu pedido: "))

if pedido == 0:
    print("Obrigado por pedir lasanha, seu pedido está pronto em breve!")

elif pedido == 1:
    print("Obrigado por pedir feijoada, seu pedido está pronto em breve!")

elif pedido == 2:
    print("Obrigado por pedir frango a parmegiana, seu pedido está pronto em breve!")

if pedido == 3:
    print("Obrigado por pedir bife a milanesa, seu pedido está pronto em breve!")

pedido2 = input("gostaria de pedir algo a mais?: ")
resposta = ["s", "n"]

if resposta == "s":
    int(input("digite o número do pedido a mais: "))
else:
    ("pedido finalizado, obrigado!")

