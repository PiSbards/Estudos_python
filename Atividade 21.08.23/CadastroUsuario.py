import os, sqlite3 as s
os.system('cls')

def CadastroUsuario():
    situacao=input("O funcionário é externo? [s] para sim, [n] para não")
    if(situacao.Lower == 's'):
        nome = input("Digite o nome do funcionário")
        email = input("Digite o e-mail do funcionário")
        funcao = 'Externo'
    else:
        nome = input("Digite o nome do funcionário: ")
        email = input("Digite o e-mail do funcionário")
        funcao = input("Digite a função do funcionário:")


    conex =s.connect("BancoDados.db")

    cursor=conex.cursor()

    cursor.execute('''INSERT INTO tabFuncionário(tbNome,tbEmail,tbFuncao) VALUES(?, ?, ?)
    ''', nome, email, funcao)

    conex.commit()
    cursor.close()
    conex.close()