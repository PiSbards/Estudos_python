#Função que não retorna valor e que não tem parâmetros

#DECLARANDO A FUNÇÃO
def exibe():
    print("Estudando funções")

#CHAMANDO A FUNÇÃO
exibe()

#FUNÇÃO QUE NÃO RETORNA VALOR E QUE TEM PARÂMETROS
def multiplicacao(valor1,valor2):
    print("Produto:", valor1 * valor2)

print("==================")
multiplicacao(2,3)


#FUNÇÃO QUE RETORNA UM VALOR
def multiplica(valor1,valor2):
    return valor1*valor2

resultado = multiplica(2,5) #or print(multiplica(2,5)); não seria necessário uma nova variavel
print("==================")
print("Produto: ", resultado)


#FUNÇÃO QUE RETORNA MAIS DE UM VALOR
def operacoes(n1,n2):
    return n1*n2,n1+n2,n1-n2

produto, total, resto = operacoes(4,2)
print("==================")
print("Produto: ",produto,"\nTotal: ", total,"\nResto: ", resto)



#RETORNAR MAIS DE UM VALOR USANDO TUPLA
tupla=()
lista=["Produto","Total", "Resto"]
k=0
def multi(valor1,valor2):
    return valor1*valor2
tupla = operacoes(10,3)
print("==================")
while(k<len(tupla)):
    print(lista[k],tupla[k])
    k+=1

#PARAMETROS DEFAULT
def exibir(valor1=0,valor2=20):# é quando o vc atribui os valores do parametro na função
    print("valor1: ",valor1)
    print("valor2: ",valor2)
print("==================")
exibir() #quando coloca valor dentro da chamada de função ele muda os valores do parametro, na posição correspondente

def numero(*args): #o simbolo "*" faz com que sejam parametros "ilimitados"
    for valor in args:
        print(valor)

numero (1,2,3,"casa",[3,4,5])

#FUNÇÕES COMO PARAMETROS
def mult (n1,n2):
    return n1*n2
def expo(v1,v2):
    return pow(v1,v2)
def exbe(a,b,func):
    print(func(a,b))

print("================")
exbe(4,3,mult)
print("================")
exbe(4,3, expo)

#RECEBER UMA LISTA COMO ARGUMENTO/PARAMENTRO
def exibir_lista(lista):
    for i in lista:
        print(i)
print("=====================")
lista_meses=["Janeiro","Fevereiro", "Março", "Abril", "Maio"] #.append == colocar a prox informação na ultima posição

exibir_lista(lista_meses)


