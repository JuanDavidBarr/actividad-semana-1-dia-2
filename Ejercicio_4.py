#4. Edad válida
#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

#Bucle para asegurarme que el valor ingresado sea un número y para asegurarme que el valor ingresado sea una edad valida
while True:
    edad_usuario = input('Por favor ingrese su edad: ')
#Asignacion de variable para validar, con el metodo 'is alpha', que los valores ingresados sean letras, de este modo, se le pedira al usuario ingresar valores de nuevo
    validar_edad_usuario = edad_usuario.isalpha()
#condicional para identificar alguna letra en la entrada del usuario o para identificar una edad invalida
    if validar_edad_usuario or int(edad_usuario) < 0 or int(edad_usuario) > 120:
        print('Por favor ingresar una edad valida')
    else:
       print(f'{edad_usuario} es una edad valida')
       break
   