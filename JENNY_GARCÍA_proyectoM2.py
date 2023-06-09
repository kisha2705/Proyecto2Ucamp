
# Proyecto Módulo 2

# 1.- Longitud de una frase 

word = input('Enter a word to has between 4 and 8 letters: ')
length = len(word)

# Validar que la longitud esté entre 4 y 8 letras
if length >= 4 and length <= 8:
    print('The word has the correct length. \n')

#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: Hacen falta letras. 
# Solo tiene N letras
if length < 4:
    print(f'Letters are missing. Only has {length} letters. \n')

#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga: Sobran letras. 
# Tiene N letras
if length > 8:
    print(f'There are too many letters. It has {length} letters.\n')

# 2.- Encuentra el cuadrante
print('Bienvenido, este programa te ayudará para saber en que cuadrante se encuentran las coordenas que desees. \n')
# Números de entrada, coordenadas
x =int(input('Ingresa el valor de x: '))

# El programa debe verificar que ninguna coordenada sea 0
while x == 0:
    print('El valor de x no puede ser 0')
    x =int(input('Ingresa el valor de x: '))
    print (f'x = {x}')
    print('Continua')
y =int(input('Ingresa el valor de y: '))
while y == 0:
    print('El valor de y no puede ser 0')
    y =int(input('Ingresa el valor de y: '))
    print (f'y = {y} \nMuy bien' )

print(f'La coordenada es ({x},{y})')

# Identifique en cuál de los 4 cuadrantes se encuentra el punto
if x > 0 and y > 0:
    print ('Se encuentra en el Cuadrante I')
elif x < 0 and y > 0:
    print ('Se encuentra en el Cuadrante II')
elif x < 0 and y < 0:
    print ('Se encuentra en el Cuadrante III')
elif x > 0 and y < 0:
    print ('Se encuentra en el Cuadrante VI')




