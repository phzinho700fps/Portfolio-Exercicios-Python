#input das notas
 
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
nota3 = int(input("Digite sua terceira nota: "))
nota4 = int(input("Digite sua quarta nota: "))

#aqui é a parte onde analisa qual das 4 notas colocadas acima é a maior, a menor, tira a soma total delas e por fim calcula a média.
maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)
soma_notas = sum([nota1, nota2, nota3, nota4])
media = (nota1 + nota2 + nota3 + nota4) / 4

#mostra no terminal os resultados da "análise"
print(maior_nota)
print(menor_nota)
print(soma_notas)
print(media)