import os
Odontologia = 0
Ginecologia = 0
Consulta_General = 0
Maternidad = 0
Infancia = 0
def fnt_selector(op):
    global Odontologia
    global Ginecologia
    global Consulta_General
    global Maternidad
    global Infancia
    if op == '1':
        Odontologia += 1
    if op == '2':
        Ginecologia += 1
    if op == '3':
        Consulta_General += 1
    if op == '4':
        Maternidad += 1
    if op == '5':
        Infancia += 1
    
def fnt_reporte():
    print(' ¡REPORTE DE ASISTENCIAS! ')
    print(f'ODONOLOGIA: {Odontologia}')
    print(f'GINECOLOGIA: {Ginecologia}')
    print(f'CONSULTA GENERAL: {Consulta_General}')
    print(f'MATERNIDAD: {Maternidad}')
    print(f'INFANCIA: {Infancia}')

control = True
while (control == True):
    os.system('cls')
    op = input('Seleccione una opcion \n1. Odontologia \n2. Ginecologia \n3. Consulta General \n4. Maternidad \n5. Infancia \n0. terminar\nSalir - Para finalizar \n->  ')

    if op == '0':
        fnt_reporte()
        input('enter para continuar')
    elif op == 'salir':
        control = False
    elif op == '1':
        fnt_selector(op)
    elif op == '2':
        fnt_selector(op)
    elif op == '3':
        fnt_selector(op)
    elif op == '4':
        fnt_selector(op)
    elif op == '5':
        fnt_selector(op)
    else:
        input('opcion incorrecta')