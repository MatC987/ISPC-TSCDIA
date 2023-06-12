#Ejercicio Nº5 - Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.
print('Ingrese el tipo de divisa con el que desea operar: indicar "p" para pesos argentinos y "d" para dolares estadounidenses')
divisa = str(input('tipo de divisa: ')).lower()
if divisa == 'p' or divisa == 'd':
    cotizacion_d = float(input('Ingrese cotizacion dolar estadounidense/peso argentino: '))
    cantidad_divisa = float(input('Ingrese monto de operacion: '))

    if divisa == 'p':
        dolares = cantidad_divisa/cotizacion_d
        print('El monto de $' , cantidad_divisa , ' pesos argentinos equivale a U$D' , dolares , 'dolares estadounidenses')
    elif divisa == 'd':
        pesos = cantidad_divisa*cotizacion_d
        print('El monto de U$D' , cantidad_divisa , ' dolares estadounidenses equivale a $' , pesos , 'pesos argentinos')
else:
    print('Dato ingresado incorrecto, intentar nuevamente:')
