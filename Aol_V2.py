#!/usr/bin/python2
#coding=utf-8

try:
	import random
	import sys
	import os
	import time
	import mechanize
	from mechanize import Browser
	os.system('clear')
	
except ImportError:
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

os.system('rm -rf live.txt')
os.system('rm -rf die.txt')
os.system('rm -rf error.txt')

die = 0
live = 0
error = 0	
sara = 0
d = 0
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

os.system('clear')
print(logo)
print('')
print('')
email = raw_input('Enter a file name:\033[1;33m ')
time.sleep(1)
muwa = open(email , 'r').readlines()
os.system('rm -rf .txt')
os.system('rm -rf die.txt')
os.system('rm -rf live.txt')
os.system('rm -rf error.txt')

count = 0 
total = open(email , 'r').readlines()
for line in total:
	count += 1



output = open('.txt', 'w')
for line in muwa:
	output.write(line.replace('@aol.com', '').replace('|Locked account', ''))
output.close()

mula = open('.txt', 'r').readlines()
	
	
os.system('clear')
print(logo)
print('')
print('')
print('\033[1;32m[ + ] CHECKING STARTED...\033[1;37m')
print('')
print('\033[1;33m[ + ] CHECKING :  ' + str(sara) +' / '+ str(count)+ '\033[1;37m')
print('')
print('\033[1;33m[ + ] TOTAL EMAILS :  {}'.format(count) + '\033[1;37m')
print('')
print('\033[1;32m[ ✓ ] DIE :  {}'.format(die) + '\033[1;37m')
print('')
print('\033[1;31m[ x ] LIVE :  {}'.format(live) + '\033[1;37m')
print('')
print('\033[1;31m[ x ] ERROR :  {}'.format(error) + '\033[1;37m')
print('')
print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
print('')
print('\033[1;32m[ + ] OWNER :  MOHA'+'\033[1;37m')
for line in mula:
		def nama():
			namas = ['Moha' , 'Mohamed', 'John', 'Albert', 'Ahmed']
			return random.choice(namas)
		def lnama():
			lnamas = ['Abdi', 'Abdirahman', 'Andrew', 'Davis', 'Khan']
			return random.choice(lnamas)
		def paas():
			pasis = ['moha123', 'mohaabdi', 'mohamoha', 'maxamed123', 'muwah123']
			return random.choice(pasis)
		def phon():
			nums = ['0633323046', '0636871801', '0637109349', '0634276015', '0634560458']
			return random.choice(nums)
		def gend():
			ganda = ['Male', 'Female']
			return random.choice(ganda)
		def days():
			monsa = ['01', '11', '22', '25', '18']
			return random.choice(monsa)
		def years():
			yara = ['1979', '1985', '1989', '1990', '2000']
			return random.choice(yara)
			
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
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
		time.sleep(1)
		
		if 'https://login.aol.com/account/challenge/' in moha:
			domain = '@aol.com'
			mum = open('die.txt', 'a')
			mum.write(line.strip()+domain+'\n')
			mum.close()
			sbal = str(sara) + ' / ' + str(count)
			saka = line.strip()+domain
			now = datetime.now()
			Time = now.strftime("%H:%M:%S")
			bot_message = "Hi 𝕄𝕆ℍ𝔸℡ ̇༗. I Fucked New Account ✅ "+"\n━━━━━━━━━━━━"+"\n.❖. 𝐄𝐌𝐀𝐈𝐋: "+saka+"\n.❖. 𝐓𝐈𝐌𝐄: "+Time+"\n.❖. 𝐂𝐑𝐀𝐂𝐊𝐈𝐍𝐆...: "+sbal+"\n.❖. 𝐎𝐖𝐍𝐄𝐑: MOHA"+"\n━━━━━━━━━━━━\n𝗖𝗛:- 𝗦𝗼𝗺𝗮𝗹𝗶𝗛𝗮𝗰𝗸𝗲𝗿"
			bot_token = token
			bot_chatID = id
			send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
			response = requests.get(send_text)
			die += 1
			d += 1
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CHECKING STARTED...' + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CHECKING :  ' + str(sara) +' / '+ str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL EMAILS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] DIE : {}'.format(die) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] LIVE :  {}'.format(live) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] ERROR :  {}'.format(error) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;32m[ + ] OWNER :  MOHA '+'\033[1;37m')
			
		elif moha == 'https://login.aol.com/account/create?specId=yidreg&done=https%3A%2F%2Fwww.aol.com&intl=us&context=reg':
			domain = '@aol.com'
			muwah = open('live.txt', 'a')
			muwah.write(line.strip()+domain+'\n')
			muwah.close()
			live += 1
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CHECKING STARTED...' + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CHECKING :  ' + str(sara) +' / '+ str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL EMAILS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] DIE :  {}'.format(die) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] LIVE :  {}'.format(live) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] ERROR :  {}'.format(error) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;32m[ + ] OWNER :  MOHA'+'\033[1;37m')
			
		else:
			domain = '@aol.com'
			meme = open('error.txt', 'a')
			meme.write(line.strip()+domain+ '\n')
			meme.close()
			error += 1
			os.system('clear')
			print(logo)
			print('')
			print('')
			print('\033[1;32m[ + ] CHECKING STARTED...' + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] CHECKING :  ' + str(sara) +' / '+ str(count) + '\033[1;37m')
			print('')
			print('\033[1;33m[ + ] TOTAL EMAILS :  {}'.format(count) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] DIE :  {}'.format(die) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] LIVE :  {}'.format(live) + '\033[1;37m')
			print('')
			print('\033[1;31m[ x ] ERROR :  {}'.format(error) + '\033[1;37m')
			print('')
			print('\033[1;32m[ ✓ ] SENT TELEGRAM :  {}'.format(d) + '\033[1;37m')
			print('')
			print('\033[1;32m[ + ] OWNER :  MOHA '+'\033[1;37m')