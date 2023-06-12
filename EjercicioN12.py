#Ejercicio Nº12 - Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares

print('Ingresar cuatro numeros: ')

pares = []
impares = []
for i in range(4):
    num = int(input('Ingrese un numero:'))
    
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

print('Los numeros pares ingresados son:' , pares , 'y los numeros impares ingresados son:' , impares , 'y la suma de los numeros pares es:' , sum(pares))