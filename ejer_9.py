frase = input('Ingrese una frase o una palabra: ')



for letra in frase:
    if frase.count(letra) > 1:
        print(f'Esta palabra o frase \"{frase}\" NO es un Heterograma')
        break
else:
    print(f'Esta palabra o frase \"{frase}\" SI es un heterograma')
        