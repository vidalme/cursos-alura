print("**********************************")
print("*BEM VINDO AO JOGO DE ADIVINHACAO*")
print("**********************************")

numero_secreto = 42
tentativas = 3
rodada = 1

for rodada in range(0,tentativas):

    print("-------------------------------------------------------------------------------------")
    print ("voce esta na rodada {} de um total de {} tentativas".format( rodada+1 , tentativas ) )
    print("-------------------------------------------------------------------------------------")
    chute = input("Digite um número entre 1 e 100: ")
    chute = int(chute)
    print("Voce digitou ", chute)
    
    if ( chute < 1 or chute > 100):
        print("!!!!!!!!seu numero não é valido!!!!!!")
        print("apenas numeros entre 1 e 100 são validos")
        continue
    

    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto 

    if (acertou):
        print("===>>>>  voce acertou!   <<=====")
        break
    else:
        if (maior):
            print("o seu chute é maior que o numero secreto")
        elif(menor):
            print("o seu chute é menor que o numero secreto")


print ("game over")