import smtplib  # Biblioteca para envio de e-mails via protocolo SMTP
from email.mime.text import MIMEText  # Para criar o conteúdo (corpo) do e-mail em formato de texto simples

# Função para enviar um e-mail
def enviar_email(destinatario, assunto, mensagem, remetente="focusflowlda@gmail.com", password="xbku iqei uftg irin"):
    # Cria o corpo do e-mail com a mensagem fornecida
    msg = MIMEText(mensagem)
    msg["Subject"] = assunto  # Define o assunto do e-mail
    msg["From"] = remetente   # Define o remetente do e-mail
    msg["To"] = destinatario  # Define o destinatário do e-mail

    # Conecta-se ao servidor SMTP do Gmail usando SSL (porta 465)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remetente, password)  # Faz login na conta do remetente
        server.sendmail(remetente, destinatario, msg.as_string())  # Envia o e-mail
