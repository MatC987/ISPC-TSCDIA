#Ejercicio Nº14 - Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad

mayores_edad = 0
menores_edad = 0
mujeres = 0
varones = 0

for i in range(5):
    edad = int(input('Ingrese edad de la persona:'))
    if edad>=18:
        mayores_edad = mayores_edad + 1
    else:
        menores_edad = menores_edad + 1
    sexo = str(input('Ingrese el sexo de la persona: -"f" si es femenino -"m" si es masculino'))
    if sexo == 'f':
        mujeres = mujeres + 1
    elif sexo == 'm':
        varones = varones + 1
    elif sexo != 'f' and sexo != 'm':
        print('Dato de sexo ingresado incorrecto, Intente nuevamente:')
        break

print('La cantidad de mujeres son:' , mujeres , 'y la cantidad de varones son:' , varones)
print('Las personas mayores de edad son:' , mayores_edad , 'y las personas menores de edad son:' , menores_edad)