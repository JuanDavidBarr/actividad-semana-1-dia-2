#Lista vacía y append()
#Crea una lista vacía llamada nombres.
#Pide al usuario su nombre y agrégalo a la lista usando append().
#Muestra la lista final.

nombres = []
nombre_usuario = input('Ingrese su nombre ')
#Convertimos el texto del usuario en minuscula para manejar el mismo formato
nombre_usuario = nombre_usuario.lower()
#Usamos el metodo 'append' para agregar el nombre del ususario enla lista
nombres.append(nombre_usuario)
print(nombres)



