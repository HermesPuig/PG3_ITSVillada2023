def esbisiesto(año:int ):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
año = int(input("ingrese el año: "))

if esbisiesto(año):
    print ( "es biciesto")
else:
    print ( "no esbiciesto")
