#definir nota
nota_trabalho= float (input("Digite a sua nota no trabalho"))
nota_prova = float (input("Digite a sua nota de prova"))
#calcular a media
media = (nota_trabalho + nota_prova)
print(f"Sua média é {media: .2f}")
if media >=7:
    print("Aprovado")
else:
    print ("Reprovado")