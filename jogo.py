perguntas = [['Seu animal gosta de bananas?', 'macaco']]

while True:
    print('Pense em um animal...')

    acertou = False

    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]} (s/n): ')

        if resposta == 's':
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    if not acertou:
        novo_animal = input('Desisto! Em qual animal você pensou? ')
        nova_pergunta = input(f'Qual pergunta ajudaria a diferenciar um {novo_animal} de um {pergunta[1]}? ')
        resposta_correta = input(f'Para {novo_animal}, a resposta para "{nova_pergunta}" seria (s/n)? ')

        if resposta_correta == 's':
            perguntas.append([nova_pergunta, novo_animal])
        else:
            perguntas.insert(0, [nova_pergunta, novo_animal]) 

    resposta = input('Quer jogar novamente? (s/n): ')
    if resposta != 's':
        print('Ok! Foi bom jogar com você!')
        break
