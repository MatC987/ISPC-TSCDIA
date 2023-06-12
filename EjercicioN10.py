#Ejercicio Nº10 - Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

numero = int(input('Ingrese un numero:'))
dias = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']


if 1 <= numero <= 7:
    print('El dia de la semana es:' , dias[numero-1])
else:
    print('Dato ingresado incorrecto, intentar nuevamente:')
