import os
os.system('cls')

resposta = 's'
while(resposta=='s'):
    menu = '''============= EMISSÃO DE ATAS ==============="
        \r[1] Emitir Ata
        \r[2] Emitir Sugestão
        \r[3] conclusão da ata
        '''
    opcao=int(input('Digite a sua opção:'))
    if(opcao==1):
        tituloAta=input("Digite o título da Ata:")
        participantes = int(input("Quantos participantes na reunião:"))
        dataInicio = int(input("Digite o dia de inicio da reunião:"))
        horaInicio = int(input("Digite a hora que iniciou a reunião: "))
        pauta = input("Digite a pauta da reunião: ")
        