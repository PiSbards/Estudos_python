import CadastroUsuario as c
import EmissaoAtas as e
import Consulta
resposta ='s'
while(resposta =='s'):
    menu= '''============= PROGAMA TDS10 ==============="
    \r[1] Cadastro Funcionário
    \r[2] Emissão Ata
    \r[3] Consultar/Relatório de Ata
    '''
    print(menu)
    opcao1=int(input("Entre com uma opção: "))
    if(opcao1==1):
        c.CadastroUsuario()
    elif(opcao1==2):
        e.emissaoAta()
    elif(opcao1==3):
        Consulta.consultaAtas()
    
    resposta = input("\nDeseja continuar no menu? [s] para sim, [n] para não: ")