def LeerDocument():
    '''La función lee un fichero y guarda la información 
    en una variable tipo lista.
    Cada dato de la lista es una línea del documento
    
    Parámetros: 

    Entrada: Ruta del fichero
    
    Salida: Lista de datos del fichero'''

    import os

    with open ('LibroCuentas.txt' , 'r',) as file:
        documento = file.readlines()
        
    return documento

def IdentificarPagado():
    '''La funcion lee las lineas de la lista,
    y devuelve las lineas pagadas.
    
    Parámetros:
    
    Entrada: Lista generada en la función anterior
    
    Salida: Lineas pagadas'''

    import os

    with open ('LibroCuentas.txt' , 'r',) as file:
        documento = file.readlines()

    lista = input('Que elemento quieres saber si esta pagado: ').upper()
    for linea in documento:
            if lista in linea:
                pagado = print('PAGADO')
            else:
                pagado = print('NO PAGADO')

    return pagado

LeerDocument()

IdentificarPagado()