#Ejercicio Nº9 - Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

print('Ingresar los tres numeros: ')

numero1 = float(input('Ingresar primer numero:'))
numero2 = float(input('Ingresar segundo numero:'))
numero3 = float(input('Ingresar tercer numero:'))

lista_numeros = [numero1,numero2,numero3]

maximo = max(lista_numeros) # valor mas grande

if maximo%2 == 0:
    print('El maximo valor ingresado es' , maximo , 'y es un numero PAR')
else:
    print('El maximo valor ingresado es' , maximo , 'y es un numero IMPAR')