#Ejercicio Nº11 - Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente

numero = int(input('Ingrese un numero:'))
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']


if 1 <= numero <= 12:
    print('El mes correspondiente es:' , meses[numero-1])
else:
    print('Dato ingresado incorrecto, intentar nuevamente:')