import requests
from bs4 import BeautifulSoup
import re
import time 
import os, sys
correct_cookie = ''
mob = ''
klaida = ''

def jungiames(nick, psw):
	login_headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
	}
	login_url = "http://tob.lt/index.php?id=log2"
	login_data = {
	"nick": nick,
	"pass": psw,
	"null": "Jungtis"
	}
	login_request = requests.post(login_url, headers=login_headers, data=login_data, allow_redirects=True)
	login_soup =BeautifulSoup(login_request.content, 'lxml')
	print("Slapyvardis: " + nick)
	print("Slaptazodis: " + psw)
	login_page = login_soup.select_one("a[href*=zaisti]")
	login_check_url = "http://tob.lt/" + login_page['href']
	global password
	password = login_check_url[-52:]
	rlcu = requests.get(login_check_url, headers=login_headers)
	soup_rlcu = BeautifulSoup(rlcu.content, 'lxml')
	ar_klaida = soup_rlcu.find('b').text
	if ar_klaida == "Blogi duomenys!":
		print("Blogi duomenys...")
		sys.exit()
	else:
		correct_cookie = rlcu.cookies['PHPSESSID']



def attack():
	time.sleep(5)
	error = ''
	mob_name = ''
	kovu_url = ''
	if mob == 1:
		error = "none"
		mob_name = "Ziurke"
		mob_lvl = "1"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=0&psl=0"
	if mob == 2:
		error = "none"
		mob_name = "Peliu lizdas"
		mob_lvl = "2"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=1&psl=0"
	if mob == 3:
		error = "none"
		mob_name = "Motinine ziurke"
		mob_lvl = "5"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=2&psl=0"
	if mob == 4:
		error = "none"
		mob_name = "Dvarfas"
		mob_lvl = "10"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=3&psl=0"
	if mob == 5:
		error = "none"
		mob_name = "Skeletas"
		mob_lvl = "20"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=4&psl=0"
	if mob == 6:
		error = "none"
		mob_name = "Golem"
		mob_lvl = "50"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=5&psl=0"
	if mob == 7:
		error = "none"
		mob_name = "Dvasia"
		mob_lvl = "80"
		kovu_url = "http://tob.lt/kova.php?nick=" + nick + "&pass=" + password + "&id=kova0&vs=6&psl=0"
	elif error != "none":
		print("[X] Klaida:" + klaida)
	# kovu_url = 'kova.php?nick=testbotas&pass=NDEzYjhkZDk5NjYxN2Rm83df9ff27b2f7f48c15df0c75bdb06dc&id=kova0&vs=0&psl=0'
	cookie = {
	"PHPSESSID": correct_cookie
	}
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
	}
	print("======================================")
	print("[INFO] Atakuojamas mobas: " + mob_name)
	print("[LVL] Atakuojamo mob lvl: " + mob_lvl)
	print("======================================")
	r = requests.get(kovu_url, headers=headers, cookies=cookie)
	soup = BeautifulSoup(r.content, 'lxml')
	x = soup.select_one("a[href*=kd]")
	url2 = 'http://tob.lt' + x['href']
	time.sleep(2)
	r2 = requests.get(url2, headers=headers, cookies=cookie)
	soup2 = BeautifulSoup(r2.content, 'lxml')

nick = input('Slapyvardis: ')
psw = input('Slaptazodis: ')
print('''
1. Ziurke
2. Peliu lizdas
3. Motinine ziurke
4. Dvarfas
5. Skeletas
6. Golem
7. Dvasia
	''')
mob = int(input('Pasirinkimas: '))
os.system('cls')
jungiames(nick, psw)
i = 1
while i < 99999999:
	print("[INFO] AUTOKOVOTOJAS ATLIKO VEIKSMU:", + i)
	attack()
	i += 1