# -*- coding: utf-8 -*-
# Author: Pari Malam
import requests
import os
import time
import sys
import colorama
from colorama import Back, Fore, Style, init

init(autoreset=True)
requests.urllib3.disable_warnings()

if not os.path.exists('Results'):
    os.mkdir('Results')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

fr  =   Fore.RED
fc  =   Fore.CYAN
fy  =   Fore.YELLOW
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
            
def banners():
    print(f"""{Style.BRIGHT + Fore.RED}
    ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗
    ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║
    ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║
    ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ 
                                                                                                                
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════{Style.BRIGHT + Fore.YELLOW}  
                                                    Coded By Pari Malam
                                            [+] Admin Login & Subdomains Scanner [+]
                                                   
                                               Forum: https://dragonforce.io
                                        Telegram: https://telegram.me/DragonForceIO
                                        
                                    Get Started With (pip install -r requirements.txt)
                                                 Usage: python Scanner.py
    {Fore.WHITE}═══════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
banners()


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Example: google.com (Without HTTP/S!)')

target_url = input('URLs'+Fore.RED+' :- '+Fore.GREEN+' ')

print(Fore.RESET+'')

if len(target_url) < 5:
    print('['+Fore.RED+'!'+Fore.WHITE+']'+Fore.YELLOW+' Target is too short!')
    time.sleep(3.0)
    sys.exit()
else:
    pass

if 'http://' in target_url or 'https://' in target_url:
    pass

if 'http://' not in target_url and 'https://' not in target_url:
    target_url = 'https://'+target_url

req = requests.Session()

test = req.get(target_url, verify=False)

time.sleep(5)

if test.status_code == 200:
    pass
else:
    print(Fore.RED+'Cant connect to target!'+Fore.WHITE+' :- '+Fore.YELLOW+''+target_url)
    sys.exit()

target_url = target_url.replace('https://', '')
print(f'''
Method 1:
        Path/Dir & Admin Login Scanner
Method 2:
        Subdomain Scanner {target_url}
''')

select_method = input('Select Method: 1/2'+Fore.RED+' :- '+Fore.WHITE+' ')



def manual_list():
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] URLs => '+Fore.GREEN+''+target_url)

    words = open('Files/wordlist.txt', 'r').read().split()

    for word in words:
        try:
            url = ('https://'+target_url+'/'+word)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()

        try:
            get_req = req.get(url, timeout=5, headers=headers)
            if get_req.status_code == 200:
                print(f'['+Fore.GREEN+'Found!'+Fore.WHITE+'] [w00t!] => '+target_url+'/'+word)
                open('Results/AdminLogin.txt','a').write(url + "\n")
            elif get_req.status_code == 301:
                print(f'['+Fore.RED+'Moved Permanently!'+Fore.WHITE+'] [301] => '+target_url+'/'+word)
            elif get_req.status_code == 403:
                print(f'['+Fore.YELLOW+'Forbidden!'+Fore.WHITE+'] [403] => '+target_url+'/'+word)
            elif get_req.status_code == 404:
                print(f'['+Fore.RED+'URLs Not Found!'+Fore.WHITE+'] [404] => '+target_url+'/'+word)
            elif get_req.status_code == 500:
                print(f'['+Fore.YELLOW+'Internal Server Error!'+Fore.WHITE+'] [403] => '+target_url+'/'+word)
            else:
                print(f'['+Fore.RED+'Failed!'+Fore.WHITE+'] [{get_req.status_code}] => '+target_url+'/'+word)
        except requests.exceptions.Timeout:
            print(f'['+Fore.RED+'Timeout!'+Fore.WHITE+'] [Failed!] => '+target_url+'/'+word)
        except requests.exceptions.RequestException as e:
            print(f'['+Fore.RED+'Error!'+Fore.WHITE+'] [Failed!] => '+target_url+'/'+word)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()


def sub_manual():
    print('['+Fore.GREEN+'*'+Fore.WHITE+'] URLs => '+Fore.GREEN+''+target_url)

    subs = open('Files/subdomains.txt', 'r').read().split()

    for sub in subs:
        try:
            url = ('https://'+sub+'.'+target_url)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()

        try:
            get_req = req.get(url, timeout=5, headers=headers)
            print(f'['+Fore.GREEN+'Found!'+Fore.WHITE+'] [w00t!] => '+sub+'.'+target_url)
            open('Results/subdomains.txt','a').write(url + "\n")
        except Exception:
            print(f'['+Fore.RED+'Not Found!'+Fore.WHITE+'] [Failed!] => '+sub+'.'+target_url)
        except KeyboardInterrupt:
            print('\nBye !')
            time.sleep(3)
            sys.exit()


if select_method == '1':
    manual_list()
elif select_method == '2':
    sub_manual()
else:
    print(Fore.RED+'[ERROR]'+Fore.WHITE+' Please enter Method 1/2! \n Enter for exit.')
    input('')
    sys.exit(1)
