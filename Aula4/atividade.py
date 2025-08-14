#float(input) para retornar um numero
#if, elif, else
#for
#break (pausa)
#while (loop infinito)


nota01_aluno = float(input("Informe a primeira nota: "))
nota02_aluno = float(input("Informe a segunda nota: "))

media_aluno = (nota01_aluno + nota02_aluno)/2

#if media_aluno >= 6: 
#    print("Aluno aprovado.")
#elif media_aluno < 6 and media_aluno >=5:
#print("Aluno em recuperação.")
#else: media_aluno >5
#print("Aluno reprovado.")


#for fregues in range (10) vai contar de "0" ate o decimo numero "9"
#for fregues in range (1,10) vai contar de "1" a "9"
#for fregues in range (1,10,2) vai contar o primeiro numero "1" e apos isso contar o segundo numero
#vai imprimir 1,3,5,7,9
##for fregues in range (10,1,-1) vai contar o primeiro numero "10" ate "1"

for fregues in range (10):
    fregues+=1
    print(fregues)
    if fregues == 10:
        print ("PARABÉNS!!! VC GANHOU!!!")

for fregues in range (10):
    print(fregues)
else:
    print("PARABÉNS!!! VC GANHOU!!!")


while tem_aula == True:
    for aula in range (5):
        print("Tem aula!")
    else:
        print("Olha a greve")
        break
print ("Hoje não tem aula")

