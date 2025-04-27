#Verificar si un número está en una lista
#Crea una lista con 5 números.
#Pide un número al usuario y verifica si está en la lista usando in.

lista = [0, 85, 21, 17, 25]
#Bucle para asegurarme que el valor ingresado sea un número
while True:
    numero_usuario = input("Por favor ingrese un número: " )
#Asignacion de variable para validar, con el metodo 'is alpha', que los valores ingresados sean letras, de este modo, se le pedira al usuario ingresar valores de nuevo
    validar_numero_usuario = numero_usuario.isalpha()
#condicional para identificar alguna letra en la entrada del usuario
    if validar_numero_usuario:
        print("Por favor ingrese solo números")
    else:
        break
#convertimos la informacion ingresada en enteros
numero_usuario = int(numero_usuario)
#condicional y uso del operador 'in' para buscar el numero ingresado en la lista
if numero_usuario in lista:
    print(f'{numero_usuario} esta en la lista')
else:
    print(f'{numero_usuario} no esta en la lista')