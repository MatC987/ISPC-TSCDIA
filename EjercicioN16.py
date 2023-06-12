#Ejercicio Nº16 - Leer 15 números negativos y convertirlos a positivos e imprimir dichos números

lista_negativos = []

for i in range(15):
    numero = float(input('Ingrese un numero:'))
    if numero <0:
        lista_negativos.append(-1*numero)
    
print('Los numeros ingresados convertidos a postivos son:' , lista_negativos)