#Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final, 
# de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado
n1 = int(input("Digite a nota n1: "))
n2 = int(input("Digite a nota n2: "))
media = (n1 + n2) / 2
if media >=0 and media < 5:
    print(f"Media: {media}, você está REPROVADO!")
elif media >=5 and media <=6.9:
    print(f"Media: {media} Você está de RECUPERAÇÃO!")
elif media >=7 and media <=10:
    print(f"Média: {media} Você está APROVADO! Parabéns")
else:
    print("Nota inserida para a média invalida.")
