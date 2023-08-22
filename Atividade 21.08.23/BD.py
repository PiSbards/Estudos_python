import sqlite3

conex=sqlite3.connect("BancoDados.db") 

cursor = conex.cursor()

cursor.execute('''
    CREATE TABLE tabAtas(tbCod INTERGER PRIMARY KEY,
    tbTitulo TEXT,
    tbDataEmissao INTERGER,
    tbParticipantes TEXT,
    tbDataInicio INTERGER,
    tbHoraInicio INTERGER,
    tbDataTermino INTERGER,
    tbHoraTermino INTERGER,
    tbPauta TEXT,
    tbSetor TEXT,
    tbDescricao TEXT,
    tbPalavraChave TEXT,
    FOREIGN KEY (tbMat)
    REFERENCES tabFunc(tbMat))
''')

cursor.execute('''
    CREATE TABLE tabFuncionario(tbMat INTERGER PRIMARY KEY AUTOINCREMENT,
    tbNome TEXT,
    tbFuncao TEXT,
    tbEmail TEXT,
    FOREIGN KEY(tbSit)
    REFERENCES tabFunção(tbSit))
''')

cursor.execute('''
    CREATE TABLE tabFuncao(tbSit INTERGER PRIMARY KEY,
    tbFuncionario TEXT,
    tbAdministrador TEXT,
    tabExterno TEXT)
''')

conex.commit()
cursor.close()
conex.close()