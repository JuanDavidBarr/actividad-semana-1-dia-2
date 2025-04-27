#1. Menor de tres números
#Pide tres números al usuario.
#Usa condicionales (if) para decir cuál es el más pequeño.


#Bucle para asegurarme que el valor ingresado sea un número
while True:
    numero_1, numero_2, numero_3 = input("Por favor ingrese el primer número: " ), input("Por favor ingrese el segundo número: "), input("Por favor ingrese el tercer número: ")
#Asignacion de variable para validar con el metodo 'is alpha' que los valores ingresados sean letras, de este modo, se le pedira al usuario ingresar valores de nuevo
    validar_numero1, validar_numero2, validar_numero3 = numero_1.isalpha(), numero_2.isalpha(), numero_3.isalpha()
#condicional para identificar alguna letra en la entrada del usuario
    if validar_numero1 or validar_numero2 or validar_numero3:
        print("Por favor ingrese solo números")
    else:
        break
#convertimos la informacion ingresada en enteros
numero_1, numero_2, numero_3 = int(numero_1), int(numero_2), int(numero_3)
#condicional para comparar los numeros y establecer cual es el menor
if numero_1 < numero_2 and numero_1 < numero_3:
    print(f"El número {numero_1} es el menor")
elif numero_2 < numero_3 and numero_2 < numero_1:
    print(f"El número {numero_2} es el menor")
else:
    print(f"El número {numero_3} es el menor")
