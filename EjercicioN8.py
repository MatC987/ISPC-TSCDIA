#Ejercicio Nº8 - Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago

importe = float(input('Ingrese el importe: '))

print('Ingresar medio de pago: 1- Contado (descuento del 10%) 2- Tarjeta (interes del 10%) 3- Debito (descuento del 5%)')
medio_pago = int(input('Ingresar opcion de metodo de pago: '))

if medio_pago == 1:
    print('El importe de: $' , importe , 'pesos argentinos siendo el metodo de pago CONTADO (descuento del 10%) , quedara en: $' , importe*0.9 , 'pesos argentinos')
elif medio_pago == 2:
    print('El importe de: $' , importe , 'pesos argentinos siendo el metodo de pago TARJETA (interes del 10%) , quedara en: $' , importe*1.1 , 'pesos argentinos')
elif medio_pago == 3:
    print('El importe de: $' , importe , 'pesos argentinos siendo el metodo de pago DEBITO (descuento del 5%) , quedara en: $' , importe*0.95 , 'pesos argentinos')
else:
    print('Dato ingresado incorrecto, intentar nuevamente:')
