

frase = input('Ingrese una frase: ')
cadena = input('Ingrese una cadena: ')

ocurrencias = frase.lower().count(cadena.lower())



print("""La cantidad de veces que \"{0}\" aparece en la frase \"{1}\" 
      es: {2}""".format(cadena, frase, ocurrencias) )

#Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres
#TRES TRISTES TIGRES, TRAGABAN TRIGO EN UN TRIGAL, EN TRES TRISTES TRASTOS, TRAGAN TRIGO TRES TRISTE TIGRES