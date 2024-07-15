import smtplib  
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
# ENTENDER O QUE SAO ESSAS PARTES

def send_email(to_addrs, body):
    from_addr = "ztoejrtvbgea2ywr@ethereal.email"
    login = "ztoejrtvbgea2ywr@ethereal.email"
    password = "Dt9YkAJ4VK3ZKRhaU4"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "Confirmação de viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string() 

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    server.quit()