#5. ¿Está en la lista de invitados?
#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

lista_invitados = ['jorge', 'camilo', 'bladimir', 'valeria', 'luisa', 'mariana']
nombre_usuario = input('Ingrese por favor su nombre: ' )
#Convertimos el texto del usuario en minuscula para manejar el mismo formato
nombre_usuario = nombre_usuario.lower()
#condicional y uso del operador 'in' para buscar el nombre ingresado en la lista
if nombre_usuario in lista_invitados:
    print(f'{nombre_usuario} esta en la lista de invitados')
else:
    print(f'{nombre_usuario} no esta en la lista de invitados')