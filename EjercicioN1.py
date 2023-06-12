#Ejercicio Nº1 - Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
letra_1 = str(input('Ingrese la primer letra: ')).upper()
letra_2 = str(input('Ingrese la segunda letra: ')).upper()

if letra_1 == letra_2:
    print('se verifica que la primer letra ingresada,siendo: ', letra_1 , 'ES IGUAL a la segunda letra ingresada, siendo:', letra_2)
else:
    print('La primer letra ingresada, siendo: ', letra_1 , 'NO ES IGUAL a la segunda letra ingresada, siendo:', letra_2)