import time
from datetime import datetime as dt

#window host path


hostPath=r"c:\Windows\System32\drivers\etc\hosts"
redirected="127.0.0.1"
#website that you wanterd to block
Websites=["www.youtubw.com","youtube.com"]

while True:
    #duration during which website blogger will work
    if dt(dt.now().year,dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month,  dt.now().day,18):
        print("Sorry not allowed...")

        with open(hostPath, 'r+') as file:
            content=file.read()
            for site in Websites:
                if site in content:
                    pass
                else:
                    file.write(redirected+" "+site+"\n")

    else:
        with open(hostPath,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not  any(site in line for site in Websites):
                    file.write(line)

            file.truncate()
            print("Allowed access!")
            time.sleep(5)