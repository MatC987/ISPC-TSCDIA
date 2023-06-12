#Ejercicio Nº7 - Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.
print('Ingrese los lados del triangulo: ')
a = int(input('Ingrese primer lado: '))
b = int(input('Ingrese segundo lado: '))
c = int(input('Ingrese tercer lado: '))

if a == b == c:
    print('El triangulo es EQUILATERO')
elif a != b and b != c and a!= c:
    print('El triangulo es ESCALENO')
else:
    print('El triangulo es ISOSCELES')