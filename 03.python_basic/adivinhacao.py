import random

def jogar():
    print("******************************************")
    print("***  BEM VINDO AO JOGO DE ADIVINHACAO  ***")
    print("******************************************")

    numero_secreto = round(random.randrange(1,101))
    rodada = 1
    pontos = 1000

    print("Escolha o nivel de dificuldade")
    print("Fácil (1)  /  Médio (2)  /  Dificil (3)")
    nivel = int(input("Degine o nivel: "))
    print("")

    #checar como garantir que o nivel seja apenas uma das 3 opcoes
    if (nivel==1):
        tentativas = 12
    elif (nivel==2):
        tentativas = 6
    elif (nivel==3):
        tentativas = 3

    #print( "cheating code --> ",numero_secreto )

    for rodada in range(0,tentativas):

        print("-------------------------------------------------------------------------------------")
        print ("           tentativa {} de {}".format( rodada+1 , tentativas ) )
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
            print("Total de pontos: {}".format(pontos))
            break
        else:
            if (maior):
                print("o seu chute é maior que o numero secreto")
            elif(menor):
                print("o seu chute é menor que o numero secreto")
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - abs(pontos_perdidos)

        if(rodada+1 == tentativas):
            print("Você perdeu, o numero correto é {}".format(numero_secreto))
    print ("game over")

if (__name__ == "__main__"):
    jogar()