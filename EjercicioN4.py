#Ejercicio Nº4 - Realice un programa que lea dos números y diga cuál es el mayor.

numero_1 = float(input('Ingrese el primer numero: '))
numero_2 = float(input('Ingrese el segundo numero: '))

if numero_1 > numero_2:
    print('El primer numero ingresado: ', numero_1 , 'ES MAYOR al segundo numero ingresado: ', numero_2)
elif numero_1 == numero_2:
    print('Los dos numeros ingresados son iguales')
else:
    print('El segundo numero ingresado: ', numero_2 , 'ES MAYOR al primer numero ingresado: ', numero_1)
