#Ejercicio Nº2 - Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.

palabra_1 = str(input('Ingrese la primer palabra: ')).lower()
palabra_2 = str(input('Ingrese la segunda palabra: ')).lower()

if palabra_1 == palabra_2:
    print('se verifica que la primer palabra ingresada,siendo: ', palabra_1 , 'ES IGUAL a la segunda palabra ingresada, siendo:', palabra_2)
else:
    print('La primer palabra ingresada, siendo: ', palabra_1 , 'NO ES IGUAL a la segunda palabra ingresada, siendo:', palabra_2)