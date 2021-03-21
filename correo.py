#módulos necesarios
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def enviarCorreo(rutaDestinatarios, rutaCredenciales, cuerpo, asunto):
    """Función cuyo próposito es enviar un correo de forma automática, desde la cuenta indicada en el archivo.txt de rutaCredenciales
    hasta las cuentas indicadas en el archivo .txt  rutaDestinatarios, envia las strings introducidas en cuerpo y asunto
    Muestra por la terminal las cuentas que van a recibir el correo"""
    #Lectura de los archivos
    f = open(rutaCredenciales, 'r')
    user = f.readline()
    user.split("\n")
    psw = f.readline()
    psw.split("\n")
    f.close()
    f = open(rutaDestinatarios, 'r')
    destinatarios = f.readlines()
    print (destinatarios)
    f.close()
    #Crea el objeto mensaje
    msg = MIMEMultipart()
    #Asigna los parámetros
    msg['From'] = user
    msg['Subject'] = asunto
    #añade el "cuerpo" del mensaje
    msg.attach(MIMEText(cuerpo, 'plain'))
    #crea el servidor
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    #inicia sesión
    server.login(user, psw)
    #envia los mensajes
    for a in range(0,len(destinatarios)):
        server.sendmail(msg['From'], destinatarios[a].replace("\n",""), msg.as_string())
    server.quit()