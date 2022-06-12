
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send(miner):
    msg = MIMEMultipart()
    #To and from are the same emails; you're emailing yourself
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'your_email@gmail.com'
    #You can alter the subject to be whatever you'd like
    msg['Subject'] = 'HELIUM MINER OUTAGE ALERT'
    message = f"Your miner {miner} is offline!"
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    #You need to make an app password in Gmail's settings
    mailserver.login('your_email@gmail.com', 'app_password')

    mailserver.sendmail('your_email@gmail.com','your_email@gmail.com', msg.as_string())

    mailserver.quit()

