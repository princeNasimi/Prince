#coding=utf
import uuid
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Nasimi.py')
P = '\1b[1;97m' # PUTIH
M = '\1b[1;91m' # MERAH
H = '\1b[1;92m' # HIJAU
K = '\1b[1;93m' # KUNING
B = '\1b[1;94m' # BIRU
U = '\1b[1;95m' # UNGU
O = '\1b[1;96m' # BIRU MUDA
N = '\1b[0m'    # WARNA MATI
A = '\1b[1;90m' # WARNA ABU ABU
BN = '\1b[1;107m' # BELAKANG PUTIH
BBL = '\1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\1b[1;105m' # BELAKANG PINK
BB = '\1b[1;104m' # BELAKANG BIRU
BK = '\1b[1;103m' # BELAKANG KUNING
BH = '\1b[1;102m' # BELAKANG HIJAU
BM = '\1b[1;101m' # BELAJANG MERAH
BA = '\1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)

ugen2=[]
ugen=[]

for xd in range(5000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
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
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(uaku2)

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
	ugen.append(uaku)


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

logo=("""
 _  __ _  _      _____
/ |/ // \/ \  /|/  __/
|   / | || |\ ||| |  _
|   \ | || | \||| |_//
\_|\_\\_/\_/  \|\____\ Nasimi
                                                                 
\3[1;37m----------------------------------------------
→   Owner      :  PRinCe Nasimi
→   Facebook   :  https://www.facebook.com/princenasimi11
→   Github     :  Princenasimi
→   Tool Type  : Nasimi
\1b[1;97m→   Version    :  1
\3[1;37m----------------------------------------------""")

def lines():
	print('\3[1;37m----------------------------------------------')
 
loop = 0
oks = []
cps = []
try:
    print('\ Updating...\\33[1;37m Please Wait\33[0;97m\ Update don ')
    proxy = requests.get('https://raw.githubusercontent.com/ALI-https://www.facebook.com/princenasimi11JUTT/Ahmed/main/update.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubushttps://www.facebook.com/princenasimi11ercontent.com/ALI-JUTT/files/main/version.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
        os.system('curl -L https://raw.githuhttps://www.facebook.com/princenasimi11busercontent.com/ALI-JUTT/ali/main/ali.py > ali.py')
        os.system('NASIMI')
    else:pass
except:print('\\33[1;31mNo internet connection ... \33[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\'+text+o),
        sys.stdout.flush();time.sleep(1)

def riaz():
	os.system('clear')
	print(logo)
	print('[1] AFG Random Cloning menu')
	print('[2] Bangladish Random Cloning')
	print('[3] Create File dumping')
	print('[4] Follow me on Facebook')
	print('\1b[1;91m[5] Exit Main menu')
	print('\3[1;37m----------------------------------------------')
	riaz1 = input('[•] Select option  : ')
	if riaz1 =='1':
		annu()
	if riaz1 =='5':
		riaz()
	if riaz1 =='3':
		os.system('xdg-open https://youtubhttps://www.facebook.com/princenasimi11e.com/channel/UCEvniQzw5VfxGdpTT4RUf3A')
	if riaz1 =='4':
		os.system('xdg-open https://youtube.com/chhttps://www.facebook.com/princenasimi11annel/UCEvniQzw5VfxGdpTT4RUf3A');riaz()
	if riaz1 =='2':
		bangla()
	else:
		print('\\33[1;31mChoose valid option\33[0;97m')
		riaz()


def annu():
    os.system('clear')
    print(logo)
