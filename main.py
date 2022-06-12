from Helium_Scrape import check_status
from send_email import send

result = check_status()[0]
name = check_status()[1]

if result != 'online' and result != 'Online':
    send(name)
send(name)

