import smtplib
from email.mime.text import MIMEText


def enviar_email(destinatario, assunto, mensagem, remetente="focusflowlda@gmail.com", password="xbku iqei uftg irin"):
    msg = MIMEText(mensagem)
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    # Gmail SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remetente, password)
        server.sendmail(remetente, destinatario, msg.as_string())
