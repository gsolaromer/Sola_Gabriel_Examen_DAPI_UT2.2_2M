corredor = input('Dime el nombre del corredor: ')
hora = input('Dime la hora: ')
kilometro = input('Dime el kilometro: ')
termino = input('Dime si ha terminado la carrera: ')
diccionario = {'Corredor' : corredor , 'Hora' : hora , 'Kilometro' : kilometro , 'Termino' : termino}


if termino == 'si':
    print (f'(El corredor a las {hora} estaba en el km {kilometro})')
else:
    print('nose')