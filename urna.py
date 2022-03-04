candidatos = {
    83:"JOSE",
    93:"CUCA",
    00:'BRANCO',
}

def votar():
    eleicao = True
    resultado = {
    'JOSE' : 0,
    'CUCA' : 0,
    'BRANCO' : 0,
    'NULL' : 0

    }
    while eleicao:

        candidato = (input("TYPE NUMBER OF CANDIDATE:  "))
        end = 'end'

        if candidato == end:
            print(f'Resultado {resultado}, WINNING {max(resultado)}')
            break


        elif int(candidato) == 83:
            print(f'YOUR VOTER IN CANDIDATE {candidatos[83]}.')
            confir = input(f'to confirm your voted in {candidatos[83]} type 1 ou remake your vote type 0: ')
            if int(confir) == 1:
                print(f'VOTED IN {candidatos[83]} CONFIRMED, THANKS FOR VOTING')
                resultado['JOSE']+= 1
            elif int(confir) == 0:
                print("YOU REMAKING YOUR VOTE")
            else:
                print("TYPE 1 OR 0")
                print("REMAKING YOUR VOTE")
        elif int(candidato) == 93:
            print(f'YOUR VOTER IN CANDIDATE {candidatos[93]}.')
            confir = input(f'to confirm your voted in {candidatos[93]} type 1 or remake your vote type 0: ')
            if int(confir) == 1:
                print(f'VOTED IN {candidatos[93]} CONFIRMED, THANKS FOR VOTING')
                resultado['CUCA'] += 1
            elif int(confir) == 0:
                print("YOU REMAKING YOUR VOTE")
            else:
                print("TYPE 1 OR 0")
                print("REMAKING YOUR VOTE")

        elif int(candidato) == 00:
            print(f'YOUR VOTER IN CANDIDATE {candidatos[00]}.')
            confir = input(f'to confirm your voted type in {candidatos[00]}  1 or remake your vote type 0: ')

            if int(confir) == 1:
                print(f'VOTED IN {candidatos[00]} CONFIRMED, THANKS FOR VOTING')
                resultado['BRANCO']+= 1
            elif int(confir) == 0:
                print("YOU REMAKING YOUR VOTE")
            else:
                print("TYPE 1 OR 0")
                print("REMAKING YOUR VOTE")
        else:
            print(f'YOUR VOTER IN NULL.')
            confir = input(f'to confirm your voted type in NULL 1 or remake your vote type 0: ')
            if int(confir) == 1:
                print(f'VOTED IN NULL CONFIRMED, THANKS FOR VOTING')
                resultado['NULL']+=1
            elif int(confir) == 0:
                print("YOU REMAKING YOUR VOTE")
            else:
                print("TYPE 1 OR 0")
                print("REMAKING YOUR VOTE")
votar()