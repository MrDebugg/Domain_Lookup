import requests
import time
import os
from bs4 import BeautifulSoup

URL = 'https://www.whois.com/whois/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
lookup = raw_input('\033[1;31;40m [*] ' + '\033[1;32;40m Input The Domain name to lookup: ')

def check_price():

    os.system("clear")
    page = requests.get(URL + lookup, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    raw_data2 = soup.find(id="registrarData").get_text()
    print (raw_data2)
    go = raw_input('\033[1;31;40m [*] ' + '\033[1;32;40m Press Enter To Quit and to save the gathered informations...')
    os.system("clear")
    print ("\033[1;31;40m [*] " + "\033[1;32;40m Saving The Snagged Informations as " + lookup + ".txt")
    time.sleep(8)
    file = open(lookup + ".txt",'w')
    file.write(raw_data2)
    file.close()

check_price()
