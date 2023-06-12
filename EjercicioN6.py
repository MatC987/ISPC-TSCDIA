#Ejercicio Nº6 - Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”

edad = int(input('Ingrese edad: '))

if edad > 16:
    print('El usuario puede votar')
else:
    print('El usuario NO puede votar')