from xml.dom import minidom
import glob
import os
import pandas as pd
from pandas import ExcelWriter

diccionario_valido = []

def open_file(file_name):
    try:
        doc = minidom.parse(file_name)
    except:
        print(file_name + "\tArchivo no compatible")
        return False

    doc = minidom.parse(file_name)

    datos_cfdi = doc.getElementsByTagName("cfdi:Comprobante")
    for dato in datos_cfdi:
        get_version = dato.getAttribute("Version")
        if(get_version):
            serie_Factura = dato.getAttribute("Serie")
            folio_Factura = dato.getAttribute("Folio")
            total_Factura = float(dato.getAttribute("Total"))
            str_total = "{:,.2f}".format(total_Factura)

        else:
            print(file_name + "\tNo es CFDI Version 3.3")
            serie_Factura   = ""
            folio_Factura   = ""
            total_Factura   = ""
            str_total       = ""
            rfc_emisor      = ""
            uuid_cfdi       = ""
            fecha_timbrado  = ""
            return False

    datos_emisor = doc.getElementsByTagName("cfdi:Emisor")
    for dato in datos_emisor:
        rfc_emisor      = dato.getAttribute("Rfc")
        nombre_emisor   = dato.getAttribute("Nombre")
        #print(rfc_emisor)


    datos_receptor = doc.getElementsByTagName("cfdi:Receptor")
    for dato in datos_receptor:
        rfc_receptor    = dato.getAttribute("Rfc")
        nombre_receptor = dato.getAttribute("Nombre")
        #print(rfc_receptor)


    datos_Complementos = doc.getElementsByTagName("cfdi:Complemento")
    for dato in datos_Complementos:
        datos_Timbrado = dato.getElementsByTagName("tfd:TimbreFiscalDigital")
        for datoTimbrado in datos_Timbrado:
            uuid_cfdi       = datoTimbrado.getAttribute("UUID")
            fecha_timbrado  = datoTimbrado.getAttribute("FechaTimbrado")

    folio_unido = serie_Factura + folio_Factura
    escribiendo_en_archivo((rfc_emisor, folio_unido , str_total , fecha_timbrado, uuid_cfdi))
    #diccionario_valido += [{'RFC':rfc_emisor, 'Folio':serie_Factura + folio_Factura, 'Total': str_total, 'Fecha':fecha_timbrado, 'UUID':uuid_cfdi}]
    valores_unidos = (rfc_emisor + "\t" + serie_Factura + folio_Factura + "\t" + str_total + "\t" + fecha_timbrado + "\t" + uuid_cfdi)
    print(valores_unidos)


print("*" * 115)
def os_operations():
    x = os.getcwdb()
    os.chdir("../")
    print(x)
def escribiendo_en_archivo(rfc,folio,importe,fecha,uuid):
    file = open("archivo_factura.txt","w")
    file.write(rfc,folio,importe,fecha,uuid)
    file.close()


labels = ['RFC','Folio','Importe','Fecha','UUID']

if __name__ == '__main__':
    contador = 0
    archivos = glob.glob("*.xml")
    for i in archivos:
        contador += 1
        open_file(i)

    print("Numero de Archivos consultados:\t", contador)
