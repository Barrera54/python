#Nombre del archivo: validar.py
#autor:Samuel barrera
#Fecha:marzo 18/2023
#Descripcion:Programa que valida nombre,edad y correo
while True:
 menu=""""
  Bienvenidos al alregistro de usuario,llene los campos  que le soliten y seleccione del 1 al 3:
  [1]Digitar su nombre
  [2]Digitar su edad
  [3]Digitar su correo electronico
  [4]salir del programa
  """
 print(menu)
 opcion = input('Entre la opcion 1,2,3 o 4: ')
 if opcion =='1':
  while True:
      nombre = input('DIGITE SU NOMBRE: ')
      if nombre.isalpha():
        print('Su nombre es: ',nombre)
 else:
         print('su nombre esta mal digitado')
 if opcion =='2':
     while True:
        edad = input('Digite su edad: ')
        if edad.isnumeric():
         print('Su edad es: ',edad)
 else:
        print('Su edad esta mal copiada')
 if opcion =='3':
      while True:
       correos = input('Entra tu correo: ')
       if correos.find('@')>=0 and correos.find('.')>=0:
        print('Tu correo es: ',correos)
 else:
       print('Metiste mal correo')