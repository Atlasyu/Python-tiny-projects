# windows C:\Windows\System32\drivers\etc
# Mac and Linus /etc/hosts
# Only administration can access the hosts document

hosts_temp = 'hosts'
hosts_path = 'C:\Windows\System32\drivers\etc'
# hosts_path = 'C:\n Windows\System32\drivers\etc' \n a new road
# hosts_path = r'C:\n Windows\System32\drivers\etc'  add a r - road

redirect = '127.0.0.1'
website_list = ['www.factbook.com','facebook.com']

import time 
from datetime import datetime as dt

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print ('Working hours...')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)