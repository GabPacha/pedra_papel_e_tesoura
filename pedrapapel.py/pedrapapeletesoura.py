placarjog1=0
placarjog2=0

for x in range(3):
    jogador1=input("Jogador 1, digite o número correspondente às opções: 1-Pedra, 2-Papel, 3- Tesoura")
    if jogador1!= "1" and jogador1!="2" and jogador1!="3":
        jogador1=input("Opção inválida.Jogador1, digite o número correspondente às opções: 1-Pedra, 2-Papel, 3- Tesoura")
    jogador2=input("Jogador 2, digite o número correspondente às opções: 1-Pedra, 2-Papel, 3- Tesoura")
    if jogador2!= "1" and jogador2!="2" and jogador2!="3":
        print("Número inválido")
    if jogador1==jogador2:
        print("Empate.")
    elif jogador1=="1" and jogador2== "2":
        print("Jogador 2 venceu.")
        placarjog2+=1
    elif jogador1== "1" and jogador2=="3":
        print("Jogador 1  venceu.")
        placarjog1+=1
    elif jogador1== "2" and jogador2=="1":
        print("Jogador 1 venceu.")
        placarjog1+=1
    elif jogador1=="2" and jogador2=="3":
        print("Jogador 2  venceu.")
        placarjog2+=1
    elif jogador1=="3" and jogador2=="1":
        print("Jogador 2 venceu.")
        placarjog2+=1
    else: 
        print("Jogador 1 venceu.")
        placarjog1+=1

if placarjog1>placarjog2:
    print("Jogador 1 venceu a melhor de três.")

elif placarjog1<placarjog2:
    print("Jogador 2 venceu a melhor de três.")
else:
    print("Melhor de três deu empate.")
    