#Ejercicio Nº15 - Leer 10 números y mostrar solamente los números positivos, y su sumatoria

lista_positivos = []

for i in range(10):
    numero = float(input('Ingrese un numero:'))
    if numero >=0:
        lista_positivos.append(numero)
    
print('Los numeros positivos ingresados son:' , lista_positivos , 'y su sumatoria es:', sum(lista_positivos))
