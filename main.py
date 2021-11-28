from Helium_Scrape import check_status
from text import send_text

result = check_status()

if result != 'online' and result != 'Online':
    send_text()

