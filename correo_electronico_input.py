### Opcion 1
def validar_correo():
    
    correo_electronico = input('Ingrese su correo electronico: ')
    

    for letra in correo_electronico:
        if letra == "@":
            print('Su correo electronico es valido!')
            return correo_electronico
                 
    print("El correo electrónico ingresado no es válido.")
    return None

### Opcion 2
def validar_correo_2():   
    correo_electronico = input('Ingrese su correo electronico: ')
    
    is_mail_valid = False
    for letra in correo_electronico:
        if letra == "@":
            is_mail_valid = True
                 
    return is_mail_valid

### Opcion 1
resultado = validar_correo()
if resultado != None:
    print("Su correo electronico es:",resultado)

### Opcion 2
resultado = validar_correo_2()
if resultado == True:
    print("Su correo electronico es valido:",resultado)
else:
    print("Su correo electronico no es valido:",resultado)