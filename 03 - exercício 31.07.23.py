#CALCULO DE MÉDIA
notas=[]
for i in range(4):
    notas.append(float(input("Entre com a nota: ")))

def media(notas):
    soma=notas[0]+notas[1]+notas[2]+notas[3]
    return soma/4

notas_media=media(notas)
print("============")
print("Média: ",notas_media)