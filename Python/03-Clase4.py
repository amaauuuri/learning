#Escribir con una y dobles comillas es exactamente lo mismo
caracter = "c"
print(type(caracter))

name = 'Amauri'
print(type(name))

#las comillas triples son sensibles a los saltos de linea
name2 = '''Amauri  


3'''
print(name2)



nombre = "Amauri Garcia"
last_name = "    Garcia Guevara   "
print(last_name)
print(name + " " + last_name)   #ponemos comillas y un espacio para imprimirlo en pantalla con mas sentido
print(name * 5)   #podemos decir cuantas veces queremos que se repita esa variable
print(5 * name)   #podemos decir cuantas veces queremos que se repita esa variable de forma inversa
print(len(name))
print(name.lower())   #hace que todas las letras se vuelvan minusculas
print(name.upper())  #hace que todas las letras se vuelvan mayusculas
print(last_name.strip()) #elimina todos los espacios antes y despues del texto

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])