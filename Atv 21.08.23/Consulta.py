import os
import pesquisa as p, sqlite3 as s
os.system('cls')
def consultaAtas():
    resposta = 's'
    while(resposta=='s'):
        menu = '''============= CONSULTA DE ATAS ==============="
        \r[1] Consultar ata única
        \r[2] Emitir Relatório
        '''
        print(menu)
        opcao=int(input('Digite a sua opção:'))
        if(opcao == 1):
            busca = p.pesquisa()
            conex = s.connect("BancoDados.db")

            cursor = conex.cursor()
            cursor.execute('SELECT * FROM tabAtas', busca)
            linha = cursor.fetchall()
            for i in linha:
                print(i)
            
            cursor.close()
            conex.close()

        if(opcao == 2):
            resp = 's'
            while(resp == 's'):
                menu2 = '''============ RELATÓRIOS ===============
                \r[1]Relatório por funcionário
                \r[2]Relatório por Setor
                \r[3]Relatorio por data
                '''
                print(menu2)
                op = int(input('Digite a sua opção: '))
                if(op == 1):
                    pesFunc = p.pesquisa()
                    conex = s.connect("BancoDados.db")

                    cursor = conex.cursor()
                    cursor.execute ('SELECT * FROM tabAtas WHERE tbMat='+pesFunc+'')
                    linha = cursor.fetchall()
                    for i in linha:
                        print(i)

                    cursor.close()
                    conex.close()
                elif(op == 2):
                    pesSetor = input("Digite o setor que deseja procurar: ")
                    conex = s.connect("BancoDados.db")

                    cursor = conex.cursor()
                    cursor.execute ('SELECT * FROM tabAtas WHERE tbSetor= '+pesSetor+'')
                    documento = cursor.fetchall()
                    for i in documento:
                        print(i)

                    cursor.close()
                    conex.close()
                elif(op == 3):
                    pesData = input("Digite a data que deseja pesquisar: ")
                    conex = s.connect("BancoDados.db")

                    cursor = conex.cursor()
                    cursor.execute ('SELECT * FROM tabAtas WHERE tbMat='+pesData+'')
                    documento = cursor.fetchall()
                    for i in documento:
                        print(i)
                    
                    cursor.close()
                    conex.close()


        resposta = input("Deseja continuar neste menu? [s] para sim, [n] para não: ")