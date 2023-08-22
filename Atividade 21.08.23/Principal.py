import CadastroUsuario as c
resposta1='s'
while(resposta1 =='s'):
    menu= '''============= PROGAMA TDS10 ==============="
    \r[1] Cadastro Funcionário
    \r[2] Emissão Ata
    \r[3] Consultar Ata
    '''
    print(menu)
    opcao1=int(input("Entre com uma opção: "))
    if(opcao1==1):
        c.CadastroUsuario()
    elif(opcao1==2):
        emissãoAta()
    elif(opcao1==3):
        consultaAta()
    
    resposta=input("\nDeseja continuar no menu? [s] para sim, [n] para não: ")