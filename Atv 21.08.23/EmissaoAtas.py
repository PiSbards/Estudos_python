import os, sqlite3 as s
os.system('cls')
def emissaoAta():
    resposta = 's'
    while(resposta=='s'):
        menu = '''============= EMISSÃO DE ATAS ==============="
        \r[1] Emitir Ata
        \r[2] Emitir Sugestão
        '''
        print(menu)
        opcao=int(input('Digite a sua opção:'))
        if(opcao == 1):
            tituloAta=input("Digite o título da Ata:")
            dataEmissao = int(input("Qual a data de Emissão da ata: "))
            participantes = int(input("Quantos participantes na reunião:"))
            dataInicio = int(input("Digite o dia de inicio da reunião:"))
            horaInicio = int(input("Digite a hora que iniciou a reunião: "))
            dataTermino = int(input("Digite a data de término da reunião:"))
            horaTermino = int(input("Digite a hora de término da reunião:"))            
            pauta = input("Digite a pauta da reunião: ")
            setor = input("Digite o setor da reunião: ")
            descricao = input("Descrição da ata: ")
            palavraChave = input("Digite até 5 palavras chaves")
            conex =s.connect("BancoDados.db")

            cursor=conex.cursor()

            cursor.execute('''INSERT INTO tabAtas(tbTitulo, tbDataEmissao, tbParticipantes,
            tbDataInicio,
            tbHoraInicio,
            tbDataTermino,
            tbHoraTermino,
            tbPauta,
            tbSetor,
            tbDescricao,
            tbPalavraChave) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', tituloAta, participantes, dataInicio, horaInicio, dataTermino, horaTermino, pauta, setor, descricao, palavraChave)

            conex.commit()
            cursor.close()
            conex.close()
        elif(opcao == 2):

            sugestao=input("Digite a sugestão:")
            conex =s.connect("BancoDados.db")

            cursor=conex.cursor()

            cursor.execute('''INSERT INTO tabSugestao(tbSugestao) VALUES(?)
            ''', sugestao)

            conex.commit()
            cursor.close()
            conex.close()
        
        resposta = input("\nDeseja continuar neste menu? [s] para sim, [n] para não: ")
