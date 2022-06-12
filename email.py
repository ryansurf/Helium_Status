import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'helium.outage@gmail.com'
msg['To'] = 'coolryanrocks@gmail.com@gmail.com'
#You can alter the subject to be whatever you'd like
msg['Subject'] = 'HELIUM MINER OUTAGE ALERT'
message = 'Your miner "{miner}" is offline!'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('helium.outage@gmail.com', 'Deeznuts44!')

mailserver.sendmail('helium.outage@gmail.com','coolryanrocks @gmail.com',msg.as_string())

mailserver.quit()

