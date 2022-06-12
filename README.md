# Helium_Status
Program that checks status(offline/online) of a Helium Miner. If the miner is offline the user is sent a warning via email to let them know. I use this so I do not have to obsessivley check to see if my miner is online and running as expected, the code does so for you.

## How to Use

You __ONLY__ need to download: Helium_Scrape.py, main.py, and send_email.py. Make sure you keep all these files in the same directory. Once you have done all the steps below, only "main.py" needs to be ran.

1: Open Helium_Scrape.py. You need to edit the __url__ variable to contain the address of your miner. Copy the address as show below and paste it in 
specified area of the url.

![alt text](address.png)

2: Open your Gmail. In your gmail app, click "Manage Your Google Account" in the top right.
            Click on security, and make sure 2-step verification is ON.
            Create an App password. Use this instead of your actual emails password, and input it in "send_email.py" where is asks for app_password.
            
3: In "send_email.py", replace all the required texts with your email/App password you just created. 

4: Your code is good to go! I run mine my "main.py" using cron on a rasberry pi everyday at 8am(How to: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/)
            If you do not have a rasberry pi/Linux device with cron, you can run the "main.py" automatically upon boot. More info here:             https://stackoverflow.com/questions/29338066/run-python-script-at-os-x-startup


