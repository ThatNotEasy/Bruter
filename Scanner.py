# Author: Pari Malam

import requests, os, sys, colorama, urllib3, concurrent.futures, signal
from sys import stdout
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor
init(autoreset=True)
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if not os.path.exists('Results'):
    os.mkdir('Results')

os.system('cls' if os.name == 'nt' else 'clear')

def banners():
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{Fore.YELLOW}[BRUTER] - {Fore.GREEN}PERFORM WITH LOGIN FINDER & SUBDOMAIN SCANNER\n")
banners()

def pari_admin():

    url = input(f"{Fore.YELLOW}[DOMAIN]{Fore.RED} .: {Fore.WHITE}")
    if not url.startswith('https://') and not url.startswith('http://'):
        target_url = 'https://' + url
    else:
        target_url = url
    with open('Files/wordlist.txt', 'r') as f:
        admins = [admin.strip() for admin in f.readlines()]
    num_threads = int(input(f"{Fore.YELLOW}[THREAD]{Fore.RED} .: {Fore.WHITE}"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for admin in admins:
            try:
                full_url = f"{target_url}/{admin}/"
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                future = executor.submit(check_url, full_url, headers)
                futures.append(future)
            except:
                print(f"{Fore.YELLOW}[BRUTER]{Fore.GREEN} .:{Fore.RED} [ERROR OCCURRED!]{Fore.GREEN} - {Fore.WHITE}{full_url}")

        for future in concurrent.futures.as_completed(futures):
            result, full_url = future.result()
            if result == 200:
                print(f"{Fore.YELLOW}[BRUTER]{Fore.RED} .: {Fore.WHITE}{full_url}{Fore.RED} - {Fore.GREEN}[W00T!]")
                open('Results/Administrators.txt', 'a').write(full_url + "\n")
            elif result == 404:
                print(f"{Fore.YELLOW}[BRUTER]{Fore.GREEN} .:{Fore.RED} [NOT FOUND!]{Fore.GREEN} - {Fore.WHITE}{full_url}")
            else:
                print(f"{Fore.YELLOW}[BRUTER]{Fore.GREEN} .:{Fore.RED} [INVALID/TIMEOUT!]{Fore.GREEN} - {Fore.WHITE}{full_url}")
    return False


def check_url(full_url, headers):
    try:
        response = requests.get(full_url, headers=headers, verify=True)
        return response.status_code, full_url
    except requests.exceptions.RequestException:
        return None, full_url

def parimalam(sub, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    full_url = f"http://{sub}.{url}"
    try:
        response = requests.get(full_url, headers=headers, verify=True)
        if response.status_code == 200:
            print(f"{Fore.YELLOW}[BRUTER]{Fore.RED} .: {Fore.WHITE}{full_url}{Fore.RED} - {Fore.GREEN}[W00T!]")
            with open('Results/Subdomains.txt', 'a') as f:
                f.write(full_url + "\n")
        else:
            print(f"{Fore.YELLOW}[BRUTER]{Fore.GREEN} .: {Fore.WHITE}{full_url}{Fore.RED} - {Fore.RED}[NOT FOUND!]")
    except requests.exceptions.RequestException:
        print(f"{Fore.YELLOW}[BRUTER]{Fore.GREEN} .: {Fore.WHITE}{full_url}{Fore.RED} - {Fore.RED}[INVALID/TIMEOUT!]")
    return False

def pari_subs():
    url = input(f"{Fore.YELLOW}[DOMAIN]{Fore.RED} .: {Fore.WHITE}")
    subs = open('Files/subdomains.txt', 'r').read().split()

    num_threads = int(input(f"{Fore.YELLOW}[THREAD]{Fore.RED} .: [DEFAULT: 10]: {Fore.WHITE}"))
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for sub in subs:
            futures.append(executor.submit(parimalam, sub, url))
        
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"{Fore.YELLOW}[BRUTER] {Fore.RED}.: [ERROR!]{Fore.GREEN} - {Fore.WHITE}{str(e)}")
    return False

if __name__ == '__main__':
    try:
        print(f"{Fore.RED}[1] - {Fore.YELLOW}LOGIN FINDER & DIRECTORY SCANNER\n{Fore.RED}[2] - {Fore.YELLOW}SUBDOMAINS SCANNER\n")
        choice = input(f"{Fore.YELLOW}[BRUTER]{Fore.RED} .: {Fore.WHITE}")
        if choice == '1':
            pari_admin()
            signal_handler
        elif choice =='2':
            pari_subs()
            signal_handler
        else:
            print(f"{Fore.RED}WHUTTT ARE YOU DOIN? GO CRYYYYY!")
    except KeyboardInterrupt:
        print(f"{Fore.YELLOW}[Bruter] {Fore.RED}-{Fore.RED} KeyboardInterrupt!{Fore.GREEN} [BYE BITCH!]")
        sys.exit()