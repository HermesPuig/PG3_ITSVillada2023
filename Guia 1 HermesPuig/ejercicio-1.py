def buscarindice(lista:list, valorabuscar:int):
    for index, value in enumerate(lista):
        if value == valorabuscar:
            return index
    
print (buscarindice([8,12,9,45], 12))
