from Helium_Scrape import check_status
from email import send_email

result = check_status()

if result != 'online' and result != 'Online':
    send_email()

