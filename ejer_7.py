lista_nombres = """ 
    'Agustin',
    'Alan',
    'Andrés',
    'Ariadna',
    'Bautista',
    'CAROLINA',
    'CESAR',
    'David',
    'Diego',
    'Dolores',
    'DYLAN',
    'ELIANA',
    'Emanuel',
    'Fabián',
    'Facundo',
    'Facundo',
    'FEDERICO',
    'FEDERICO',
    'GONZALO',
    'Gregorio',
    'Ignacio',
    'Jonathan',
    'Jonathan',
    'Jorge',
    'JOSE',
    'JUAN',
    'Juan',
    'Juan',
    'Julian',
    'Julieta',
    'LAUTARO',
    'Leonel',
    'LUIS',
    'Luis',
    'Marcos',
    'María',
    'MATEO',
    'Matias',
    'Nicolás',
    'NICOLÁS',
    'Noelia',
    'Pablo',
    'Priscila',
    'TOMAS',
    'Tomás',
    'Ulises',
    'Yanina' 
    """
 
evaluacion_1 = ''' 81,
    60,
    72,
    24,
    15,
    91,
    12,
    70,
    29,
    42,
    16,
    3,
    35,
    67,
    10,
    57,
    11,
    69,
    12,
    77,
    13,
    86,
    48,
    65,
    51,
    41,
    87,
    43,
    10,
    87,
    91,
    15,
    44,
    85,
    73,
    37,
    42,
    95,
    18,
    7,
    74,
    60,
    9,
    65,
    93,
    63,
    74  '''
 
evaluacion_2 = """ 30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10  """
 
lista_nombres = lista_nombres.strip()
lista_nombres = lista_nombres.split('\n')

evaluacion_1 = evaluacion_1.split('\n')
evaluacion_2 = evaluacion_2.split('\n')

estudiantes_notas = {}
suma_total = 0


for i in range(len(lista_nombres)):
    estudiantes_notas[lista_nombres[i].replace(',','')] = int(evaluacion_1[i].replace(',','')) + int(evaluacion_2[i].replace(',',''))
    suma_total += int(evaluacion_1[i].replace(',','')) + int(evaluacion_2[i].replace(',','')) 

promedio = suma_total / (len(evaluacion_1) + len(evaluacion_2))


print('Esta la lista con los estudiantes y la suma de sus notas: ')
for estudiante, nota in estudiantes_notas.items():
    print(estudiante, ':', nota)


print('Estos son los estudiantes que no superan el promedio: ')
for estudiante, nota in estudiantes_notas.items():
    if (estudiantes_notas[estudiante] / 2) < promedio:
        print(estudiante, ':', nota)