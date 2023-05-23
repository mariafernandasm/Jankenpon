opcoes = ["pedra", "papel", "tesoura"]
escolha1 = input("Escolha entre pedra, papel e tesoura: ")
escolha2 = input("Escolha pedra, papel e tesoura: ")

def verificarEscolha(escolha1, escolha2):
    if escolha1 == "pedra" and escolha2 == "papel":
        print ("Papel ganhou!")
    if escolha1 == "pedra" and escolha2 == "tesoura":
        print ("Pedra ganhou!")
    if escolha1 == "papel" and escolha2 == "tesoura":
        print ("Tesoura ganhou!")
    if escolha1 == "papel" and escolha2 == "pedra":
        print ("Papel ganhou!")
    if escolha1 == "tesoura" and escolha2 == "pedra":
        print ("Pedra ganhou!")
    if escolha1 == "tesoura" and escolha2 == "papel":
        print ("Tesoura ganhou!")

resultado = verificarEscolha(escolha1, escolha2)
print(resultado)
