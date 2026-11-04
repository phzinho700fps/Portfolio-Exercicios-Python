#teste de aprovação de alunos com base na média de notas

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) /2

#mostra no terminal as informações colocadas nos inputs acima
print(nome)
print(nota1)
print(nota2)
print(media)


#condicional que determina se o aluno passa, fica de recuperação ou repova com base na média das notas
if media >= 7:
    print(f"{nome} está aprovado!")
elif media < 5.9:
    print(f"{nome} está reprovado!")
else:
    print(f"{nome} está de recuperação!")