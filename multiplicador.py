#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import os
import sys

def ahora_fecha():
    fecha = time.strftime("%Y-%m-%dT%X %Z")
    return fecha


def cleaning():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


def nombre_archivo():
    fecha = time.strftime("%Y-%m-%d_%H%M")
    nombre = "Resultado %s.txt" % (fecha)
    return nombre


billetes = [1000, 500, 200, 100, 50, 20]
decorador_str = "*"*80

cleaning()

def decorador():
    print('*' * 110)

def nombre():
    print(" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ██████╗  ██████╗ ██████╗  █████╗ ")
    print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗")
    print("██║     ███████║██║     ██║     ██║   ██║██║     ███████║██║  ██║██║   ██║██████╔╝███████║")
    print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║██║  ██║██║   ██║██╔══██╗██╔══██║")
    print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║██████╔╝╚██████╔╝██║  ██║██║  ██║")
    print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝")
    print("                                                                                          ")

decorador_resultado = '''
██████╗ ███████╗███████╗██╗   ██╗██╗     ████████╗ █████╗ ██████╗  ██████╗
██╔══██╗██╔════╝██╔════╝██║   ██║██║     ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗
██████╔╝█████╗  ███████╗██║   ██║██║        ██║   ███████║██║  ██║██║   ██║
██╔══██╗██╔══╝  ╚════██║██║   ██║██║        ██║   ██╔══██║██║  ██║██║   ██║
██║  ██║███████╗███████║╚██████╔╝███████╗   ██║   ██║  ██║██████╔╝╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝
'''

def decorador_resultado():
    print("██████╗ ███████╗███████╗██╗   ██╗██╗     ████████╗ █████╗ ██████╗  ██████╗ ")
    print("██╔══██╗██╔════╝██╔════╝██║   ██║██║     ╚══██╔══╝██╔══██╗██╔══██╗██╔═══██╗")
    print("██████╔╝█████╗  ███████╗██║   ██║██║        ██║   ███████║██║  ██║██║   ██║")
    print("██╔══██╗██╔══╝  ╚════██║██║   ██║██║        ██║   ██╔══██║██║  ██║██║   ██║")
    print("██║  ██║███████╗███████║╚██████╔╝███████╗   ██║   ██║  ██║██████╔╝╚██████╔╝")
    print("╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝  ╚═════╝ ")
    print("                                                                           ")

def main():
    decorador()
    nombre()
    decorador()
    #print('\t\t\tMultiplicador')
    decorador()
    mil = 0
    qui = 0
    dos = 0
    cie = 0
    cin = 0
    vei = 0

    m_mil = 0
    m_qui = 0
    m_dos = 0
    m_cie = 0
    m_cin = 0
    m_vei = 0

    cantidades = [mil, qui, dos, cie,cin, vei]
    multiplicados = [m_mil,m_qui ,m_dos, m_cie, m_cin, m_vei]

    for i in range(0,6):
        cantidades[i] = input('\nCantidad de Billetes de {}:\t'.format(billetes[i]))
        if cantidades[i] == '':
                multiplicados[i] = 0
        else:
            multiplicados[i] = int(cantidades[i]) * int(billetes[i])

    cleaning()
    decorador()
    #nombre()
    decorador()
    print(decorador_resultado())
    print("\t\t" + ahora_fecha())
    decorador()
    print('\tBillete\t\tCantidad\tImporte')
    decorador()
    fichero = open(nombre_archivo(),'w')
    fichero.write(ahora_fecha()+'\n')
    fichero.write("\tResultado de Multiplicador" + "\n")
    fichero.write(decorador_str+'\n')
    for i in range(0,6):
        #archivo_salida = open()
        fichero.write('\t{:,} \tx \t{}\t:\t{:,}\n'.format(billetes[i], cantidades[i], multiplicados[i]))
        print('\t{:,} \tx \t{}\t:\t{:,}'.format(billetes[i], cantidades[i], multiplicados[i]))
    decorador()
    suma = 0
    for i in range(0,6):
        suma += multiplicados[i]
    fichero.write(decorador_str+'\n')
    fichero.write('********\tSuma Total:\t$\t{:,}\t\t\t\t********\n'.format(suma))
    fichero.write(decorador_str)
    fichero.close()
    print('********\tSuma Total:\t$\t{:,}\t\t\t\t********'.format(suma))
    decorador()


def escribiendo_en_archivo():
    pass


if __name__ == '__main__':
    main()
    #decorador_resultado()
