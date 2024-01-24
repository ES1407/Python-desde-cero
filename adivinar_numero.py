# Crear una funcion que adivine un numero del 1 al 50
def advinar_numero():

    print('Piense un numero entre el 1 y el 50')
    print('Escriba si o no')
    respuesta1 = input('Su numero es mayor o igual a 50?: ')

    if respuesta1 == 'si':
        mayor_o_igual_25 = input("Su numero es menor o igual a 25?: ")

    elif respuesta1 == 'no':
        menor_o_igual_25 = input("Su numero es menor o igual a 25?: ")

    elif menor_o_igual_25 == 'si':
        menor_o_igual_15 = input("Su numero es menor o igual a 15?: ")

    elif menor_o_igual_25 == 'no':
        mayor_o_igual_35 = input('Su numero es mayor o igual a 35?: ')


respuesta = advinar_numero()
print(respuesta)
