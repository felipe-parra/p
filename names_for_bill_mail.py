# -*- coding:utf-8 -*-

receivers = {"A": "ALONSO",
             "D": "DECASA",
             "V": "DON VASCO",
             "G": "GAPSA",
             "C": "GONAC",
             "L": "LA ASUNCION",
             "F": "FJ CORONA",
             "N": "NIETO",
             "X": "NISSAN",
             "Z": "PCZ",
             "P": "PEPSICO",
             "R": "RAGON",
             "S": "SAHUAYO",
             "Y": "YOA"
             }

senders = {"E":"EUDES", "V":"VIEMPRO"}

message = ""


def subject_mail(sender, receiver):
    subject_name = "Pago %s / %s" % (sender, receiver)
    print(subject_name)
    return subject_name


def question_sender():
    while True:
        message_q = ""
        for i in senders:
            message_q += "'%s': '%s' " % (i,senders[i])
        q_sender = input("Escoger el Remitente\n" + message_q)[0:1].upper()
    
        try:
            for valor in senders:
                if(q_sender == valor):
                    #print(senders[valor])
                    return senders[valor]
        except:
            print("ATENCION: Ingresar un dato correcto")

 
def question_receiver():
    while True:
        message_r = ""
        for i in receivers:
            message_r += "'%s': '%s'\n" % (i,receivers[i])
        q_receiver = input("Escoger el Destinatario\n" + message_r)[0:1].upper()
    
        try:
            for valor in receivers:
                if(q_receiver == valor):
                    #print(receivers[valor])
                    return receivers[valor]
        except:
            print("ATENCION: Ingresar un dato correcto")

def question_files():
    message_f = "Cuantos archivos :\t"
    while True:
        q_files = input(message_f)[0:1]
        try:
            q_files = int(q_files)
            if(q_files == 1):
                filename = input("Ingresar numero de Factura\t")
                list_name = [filename]
                #print(body_mail(list_name))
                return body_mail(list_name)
        except:
            print("Error con el valor ingresado")

                
def body_mail(filenames):    
    if (len(filenames) == 1):
        message = "Comprobante%s de pago de la%s Factura%s No%s" %("","","",". ")
        filename = filenames[0]
        print(message + filename)
        return filename
    
    elif(len(filenames) > 1):
        names = ""
        message = "Comprobante%s de pago de la%s Factura%s No%s" %("s","s","s",".:\n ")
        print(message)
        for i in filenames:
            names += i + "\n"
            print(i)
        return names
    

if __name__ == '__main__':
    subject_mail(question_sender(),question_receiver())
    question_files()
    #body_mail(["A1417075"])
    #body_mail(["A1417075","A1417076", "A1417077"])
