## EJERCICIOS
# ejercicio 1

# crear un programa que pida al usuario su edad e imprima, si es mayor o menor de edad
edad:int=int(input("ingrese su edad: "))
if edad < 18:
    print("eres un chibolin menor de edad")
else:
    print("tu ya eres un ciudadano") 


# ejercicio 2
#crear un programa que pregunte la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor
#de 5 años puede ingrasar gratis, si tiene entre 5 y 18 años debe pagar s/.10 y si es mayor de 18 años debera pagar s/.25 .
edad_usuario:int=int(input("ingrese su edad: ")) 
if edad_usuario < 5:
    print("usted ingresa gratis")
elif edad_usuario >= 5 and edad_usuario <= 18:
    print("usted debera pagar s/.10 por su entrada")
else:
    print("usted debera pagar s/.25 por su entrada")