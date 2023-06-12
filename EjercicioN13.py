#Ejercicio Nº13 - Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

mayores = 0
menores = 0
lista = []

for i in range(10):
    numero = float(input('Ingrese un numero:'))
    if numero >= 100:
        mayores = mayores + 1
    else:
        menores = menores + 1
    lista.append(numero)

print('Los numeros mayores o iguales a 100 ingresados fueron', mayores , 'y los menores fueron' , menores , '. El numero maximo fue' , max(lista) , 'y el minimo fue' , min(lista))
