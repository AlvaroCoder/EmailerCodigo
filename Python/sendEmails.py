import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from htmlEmail import htmlEmail

def sendListEmails(lista_correos=list):
    email_cs = "ieeecs.directiva@gmail.com"
    pass_cs = "whxgdpygtrrsvtwm"
    email_subject = "Invitación al grupo de Whatssap de Introducción a Python"
    html_message = htmlEmail()
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    for key,correo in enumerate(lista_correos):
        if type(correo) == str:
            receiver_email = correo
        
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

            print(f"Email #{key} send to -> {receiver_email}!")

lista_emails = ["evan.quispe@alum.udep.edu.pe","evelynlochu-2003@hotmail.com","anachv111@gmail.com","nicolecipriani6@gmail.com","marianacc03@gmail.com"]
sendListEmails(lista_correos=lista_emails)