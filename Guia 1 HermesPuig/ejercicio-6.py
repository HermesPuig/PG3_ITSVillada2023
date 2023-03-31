def cantVocales(frase):
    contvocales = 0
    vocales = ["a","e","i","o","u", "A", "E","I","O","U"]
    for letras in frase:
        if letras in vocales:
            contvocales = contvocales +1
    return contvocales

vocales = cantVocales("ricardo pereyra")
print(vocales)