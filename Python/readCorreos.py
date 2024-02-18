import pandas as pd
from sendEmails import sendListEmails

alumnos = pd.read_csv('Data\TALLER DE PROGRAMACIÓN_ INTRODUCCIÓN A PYTHON.csv')
lista_correos = alumnos['Correo electrónico personal o alumnos (UDEP) ']
lista_correos_2= []

for key,correo in enumerate(lista_correos):
    if type(correo) == str:
        lastPartEmail = correo.split("@")
        extEmail = lastPartEmail[1]
        if extEmail.strip() != "alum.udep.edu.pe":
            if extEmail.strip() != "gmail.com":
                if extEmail.strip() == "hotmail.com":
                    extEmail=extEmail.lower()
                    nameEmail = lastPartEmail[0].lower()
                    nuevoCorreo = nameEmail+"@"+extEmail
                    lista_correos_2.append(nuevoCorreo)
                    continue

                nameEmail = lastPartEmail[0].lower()
                extEmail = "alum.udep.edu.pe"
                nuevoCorreo = nameEmail+"@"+extEmail
                lista_correos_2.append(nuevoCorreo)

# sendListEmails(lista_correos=lista_correos_2)

