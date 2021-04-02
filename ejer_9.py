frase = input('Ingrese una frase o una palabra: ')

lista_letras = []

for letra in frase:
    if letra == ' ':
        continue
    else:
        lista_letras.append(letra)
        
for letra in lista_letras:
    if lista_letras.count(letra) > 1:
        print(f'Esta palabra o frase \"{frase}\" NO es un Heterograma')
        break
else:
    print(f'Esta palabra o frase \"{frase}\" SI es un heterograma')