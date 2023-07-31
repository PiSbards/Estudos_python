'''
input("") = comando de entrada(sempre será string, precisa converter se for outro tipo)
print() = comando de saida
pode-se atribuir multiplas váriaveis de mesmo jeito ex: var1, var2= 99,98
operadores matematicos  + (soma)
                        - (subtração)
                        / (divisão)
                        * (multiplicação)
                        **(potencia)
                        %(modulo)
                        //(coeficiente inteiro)
operadores comparação == (igual)
                      != (diferente)
                      < (menor)
                      > (maior)
                      <= (menor igual)
                      >= (maior igual)
operadores lógicos   not(não)
                     and(e)
                     or(ou)
operadores de atribuição =
                         +=
                         *=
                         -=
                         /= 
                         //=
                         %=
                         **=
if():

else:
for a in lista #quantidade de vezes é determinada com a quantidade da lista, se o usuário decidir usar uma quantidade de loops expecificos usar range(var)
    print(a)

lista = []

while()

método/função - def
def soma (n1,n2)
    resultado = n1+n2
    return resultado
'''
nome = input("Entre com seu nome:") #comando de entrada pode ser colocada direto na variável

print("seu nome é: ",nome) #comando de saida
idade = int(input("Digite a sua idade:")) #comando de entrada + comando de converção
if(idade>=18 and idade <=45):
    print("Você tem ",idade,"anos \nvocê é maior de idade\n mas você ainda é jovem")

elif(idade>45 and idade<60):
    print("Você possui ",idade,"anos \nVocê maior de idade\n você é um adulto")

elif(idade>=60):
    print("Você é maior de idade",idade,"Você é idoso")
else:
    print("Você é menor de idade")
