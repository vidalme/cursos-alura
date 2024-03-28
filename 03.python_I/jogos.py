import forca
import adivinhacao
def escolhe_jogo():
    print("**********************************************")
    print("***           ESCOLHA SEU JOGO             ***")
    print("**********************************************")


    print("(1) Forca  (2) Adivinhação")
    jogo = int(input("selecione 1 ou 2: "))

    if( jogo == 1):
        forca.jogar()
    if( jogo == 2):
        adivinhacao.jogar()

    print("**********************************************")

if(__name__ == "__main__"):
    escolhe_jogo()