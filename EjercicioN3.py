#Ejercicio Nº3 - Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.

print('Ingrese el sexo de la persona que va a votar - SOLAMENTE INGRESAR "m" si es masculino o "f" si es femenino')
sexo = str(input('SEXO: ')).lower()
if sexo == "f":
    print('La persona vota en mesa femenina')
elif sexo == "m":
    print('La persona vota en mesa masculina')
else:
    print('Dato ingresado incorrecto, intentar nuevamente:')
