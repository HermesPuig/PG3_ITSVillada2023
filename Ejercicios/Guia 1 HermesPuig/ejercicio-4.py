def ordenar(lista):
    for i in range(len(lista),1,-1):
        for j in range(0,i-1):
            if lista[j] < lista[j+1]:
                lista[j],lista[j+1] =lista[j+1], lista[j]

    return lista
lista= []

for i in range(5):
    valor = int(input("ingrese un numero: "))
    lista.append(valor)

print(print)

print(ordenar(lista))