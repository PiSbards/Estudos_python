import sqlite3

conex=sqlite3.connect("BancoDados.db") 

cursor = conex.cursor()
cursor.execute('''
    CREATE TABLE tabSugestao(tbSug INTEGER PRIMARY KEY AUTOINCREMENT,
    tbSugestao TEXT)
''')

cursor.execute('''
    CREATE TABLE tabFuncao(tbSit INTEGER PRIMARY KEY,
    tbFuncionario TEXT,
    tbAdministrador TEXT,
    tabExterno TEXT)
''')

cursor.execute('''
    CREATE TABLE tabFuncionario(tbMat INTEGER PRIMARY KEY AUTOINCREMENT,
    tbNome TEXT,
    tbFuncao TEXT,
    tbEmail TEXT,
    FOREIGN KEY(tbSit)
    REFERENCES tabFuncao(tbSit))
''')

cursor.execute('''
    CREATE TABLE tabAtas(tbCod INTEGER PRIMARY KEY,
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
    REFERENCES tabFuncionario(tbMat)
    FOREIGN KEY(tbSug)
    REFERENCES tabSugestao(tbSug)
    FOREIGN KEY (tbMat)
    REFERENCES tabFuncionario(tbMat))
''')


conex.commit()
cursor.close()
conex.close()