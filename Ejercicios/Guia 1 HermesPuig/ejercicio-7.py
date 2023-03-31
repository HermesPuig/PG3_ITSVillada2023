def esStep(numero):
    numtostring = str(numero)
    cant = 0
    for i in range(len(numtostring)):
        if i != len(numtostring) - 1:
            if abs(int(numtostring[i]) - int(numtostring[i+1])) == 1:
                cant += 1

    return cant == (len(numtostring) - 1)
print(esStep(123))
