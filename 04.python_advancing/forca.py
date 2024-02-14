import random
def jogar():

    print("**********************************************")
    print("***       BEM VINDO AO JOGO DE FORCA       ***")
    print("**********************************************")

    # list de palavras possiveis de serem sorteadas para o jogo
    palavras_secretas = []
    with open('waves.txt','r') as linhas:
        for linha in linhas:
            palavras_secretas.append(linha.strip())
    print(palavras_secretas)
    palavra_secreta = palavras_secretas[(random.randrange(0,len(palavras_secretas)))-1]
    print("a palavra secreta é: "+palavra_secreta)
    
    # condicoes basicas de flow
    enforcou = False
    acertou = False

    erros = 0
    max_erros = 5
    # inicia uma palavra, nao é necessario mas da clareza no codigo
    palavra_adivinhada = ""

    # contagem para saber se a palavra tem espacos dentro
    prox = 0
    partes_palavra_secreta = palavra_secreta.split(' ')
    
    # cria o conteudo da palavra que o usuario vai modificar com suas tentativas
    for parte in partes_palavra_secreta:
        for letra in parte:
            palavra_adivinhada += "_"
        prox += 1
        if prox < len(partes_palavra_secreta):
            palavra_adivinhada += " "

    #checa se o jogo acabou
    while (not enforcou and not acertou):

        #pede mais uma tentativa
        print('Você ainda tem {} tentativas'.format(max_erros - erros))
        chute = input('Digite sua letra: '+palavra_adivinhada.capitalize()+ ' <--: '  )
        if len(chute) != 1 :
            print('Digite apenas uma caractere')
            continue
        
        chute = chute.strip()
        index = 0
        
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                listed_palavra_adivinhada = list(palavra_adivinhada)
                listed_palavra_adivinhada[index] = letra
                palavra_adivinhada = "".join(listed_palavra_adivinhada)
            index += 1

        if "_" not in palavra_adivinhada:
            acertou = True
            print("Fim do jogo você ganhou uma passagem para {}!".format(palavra_adivinhada))

        if chute.lower() not in palavra_secreta.lower():
            erros += 1
            print('A letra {} não foi encontrada'.format(chute))
        if erros >= max_erros:
            enforcou = True
            print("Fim do jogo você perdeu!")


if (__name__ == "__main__"):
    jogar()