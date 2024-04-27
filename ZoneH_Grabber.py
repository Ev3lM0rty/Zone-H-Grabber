import requests
import re
import sys
import os
import platform
from colorama import Fore, Style, init

init(autoreset=True)
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
os.system('cls')
banner = '''

  ______                       _        _____           _     _                
 |___  /                      | |      / ____|         | |   | |               
    / / ___  _ __   ___ ______| |__   | |  __ _ __ __ _| |__ | |__   ___ _ __  
   / / / _ \| '_ \ / _ \______| '_ \  | | |_ | '__/ _` | '_ \| '_ \ / _ \ '__| 
  / /_| (_) | | | |  __/      | | | | | |__| | | | (_| | |_) | |_) |  __/ |    
 /_____\___/|_| |_|\___|      |_| |_|  \_____|_|  \__,_|_.__/|_.__/ \___|_|    
                                                                               
\t\tTelegram Channel Link : t.me/Ev3l_m0rty_Channel / Telegram Admin Link: t.me/Ev3l_m0rty'''
print(banner)
zhe_coockie = input('\t\t\ Enter ZHE : ')
phpsessid_coockie = input('\t\t\ Enter PHPSESSID : ')
cookie = {
    "ZHE": zhe_coockie,
    "PHPSESSID": phpsessid_coockie
}

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    if platform.system() == 'Windows':
        os.system('cls')

def display_banner():
    print(banner)
    print("\t\t\ |1| Grabb Sites By Notifier")
    print("\t\t\ |2| Grabb Sites By Onhold")

def zonehgrabber():
    choice = int(input("\t\t\ Enter Your option Number (1-2): "))
    if choice == 1:
        var1 = input("\t\t\ Enter notifier: ")

        for i in range(1, 51):
            var2 = requests.get("http://www.zone-h.org/archive/notifier=" + var1 + "/page=" + str(i), cookies=cookie)
            var3 = var2.content
            print('\t\t ! Grab From sites : ' + 'http://www.zone-h.org/archive/notifier=' + var1 + '/page=' + str(i) + ' !')
            if b'<html><body>-<script type="text/javascript"' in var3:
                print("\t\t ! False Cookies - re-enter cookies !")
                sys.exit()
            elif b'<input type="text" name="captcha" value=""><input type="submit">' in var3:
                print("\t\t ! Verify The Capcha In Zone-H !")
                sys.exit()
            else:
                rgio_urls = re.findall(b'<td>(.*)\n							</td>', var3)
                if b'/mirror/id/' in var3:
                    for rgioo in rgio_urls:
                        drq0 = rgioo.replace(b'...', b'')
                        print('    \t\t[' + '+' + '] ' + drq0.split(b'/')[0].decode())
                        with open(var1 + '.txt', 'a') as rr:
                            rr.write("http://" + drq0.split(b'/')[0].decode() + '\n')
                else:
                    print("\t\t ! Grabb Sites completed !")
                    sys.exit()

    elif choice == 2:
        for sssss in range(1, 51):
            qie = requests.get("http://zone-h.org/archive/published=0" + "/page=" + str(sssss), cookies=cookie)
            var5 = qie.content

            if b'<html><body>-<script type="text/javascript"' in var5:
                print("\t\t ! False Cookies - re-enter cookies !")
                sys.exit()

            elif b"captcha" in var5:
                print("\t\t ! Verify The Capcha In Zone-H !")
            else:
                rgio_urlss = re.findall(b'<td>(.*)\n							</td>', var5)
                for rgioox in rgio_urlss:
                    drqqq = rgioox.replace(b'...', b'')
                    print('    \t\t[' + '+' + '] ' + drqqq.split(b'/')[0].decode())
                    with open('onhold_zone.txt', 'a') as rrr:
                        rrr.write("http://" + drqqq.split(b'/')[0].decode() + '\n')
    else:
        print("\t\t ! Error !")

def main():
    clear_screen()
    display_banner()
    zonehgrabber()
    
if __name__ == "__main__":
    main()
