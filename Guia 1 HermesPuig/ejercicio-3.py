def pintar(ancho, largo, caracter):
    for _ in range(largo): 
        for _ in range(ancho):
            print(caracter, end="")
        print()

ancho = int(input("ingrese el ancho: "))
largo = int(input("ingrese el largo: "))
caracter = (input("ingrese el caracter: "))

print (pintar (ancho,largo,caracter))
