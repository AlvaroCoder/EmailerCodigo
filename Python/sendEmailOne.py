import pandas as pd
import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from htmlEmail import htmlEmail

alumnos = pd.read_csv('Data\TALLER DE PROGRAMACIÓN_ INTRODUCCIÓN A PYTHON.csv')
lista_correos = alumnos['Correo electrónico personal o alumnos (UDEP) ']

email_cs = "ieeecs.directiva@gmail.com"
pass_cs = "whxgdpygtrrsvtwm"
email_subject = "Invitación al grupo de Whatssap de Introducción a Python"
html_message = htmlEmail()
smtp_server = 'smtp.gmail.com'
smtp_port = 587
receiver_email = "yicsson.camacho@alum.udep.edu.pe"
    
msg = MIMEMultipart()
msg['From'] = email_cs
msg['To'] = receiver_email
msg['Subject'] = email_subject

msg.attach(MIMEText(html_message,'html'))

context = smtplib.SMTP(smtp_server, smtp_port)
context.starttls()

context.login(email_cs, pass_cs)

context.sendmail(email_cs, receiver_email, msg.as_string())

context.quit()

print(f"Email Send to {receiver_email}!")