#/usr/bin/python3 
# -*- coding:utf-8 -*- 

from twilio.rest import Client 
import os, sys 
import time

os.system('clear')
ACCOUNT_SID = ""
AUTH_TOKEN = ""
from_ = "" 
client = Client(ACCOUNT_SID, AUTH_TOKEN)

global end, verde, azul, amarelo, vermelho, purpleClaro, normal, cyanClaro, W, R, G, O, B, P, C, GR
end = '\033[0m'

W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
amarelo= '\033[1;33m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
time.sleep(8./90)

def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + G + String)
        sys.stdout.flush()
print('')

BannerOld = """
+===========================================+
| Script Teste Python 1.0 UPDATE 10/06/18   |
+===========================================+
| Date: 10/06/2018                          |
| Hour: 19:10                               |
| https://github.com/MECZINRj               |
+===========================================+
| [1] -> Escrever uma mensagem. <-          |
| [2] -> Enviar spam. <-                    |
+===========================================+   
"""

BannerEnd = """
+===========================================+
| Script Teste Python 1.0 UPDATE 10/06/18   |
+===========================================+
| Date: 10/06/2018                          |
| Hour: 19:10       					    |
| https://github.com/MECZINRj               |
+===========================================+
|			    [SCRIPT END]                |
+===========================================+
"""


print azul + BannerOld
print('')
slowprint(P+" NCF SCRIPT - 2018 ")
print('')
Animation(" SMS - SPAM NCF ")
print('')

try:
	opt = raw_input(amarelo + '[x] Escolha uma opção:')
except KeyboardInterrupt:
	print(vermelho+"\n \n [x] Saindo...")
	time.sleep(3)
	print cyanClaro + BannerEnd
	exit()
print('')

def Ma1n():
	global body, to, from_ 
	body = raw_input(cyanClaro + "[x] Digite sua Mensagem:")
	print('')
	to =   raw_input(cyanClaro + '[x] Digite numero da vitima:')
	print('')
	img =  raw_input(amarelo + "[x] Deseja enviar uma imagem? [y/N]")
	if img == 'y':
		img2 = raw_input(amarelo + '[x] Enviar mais de uma [1] imagen? [y/N]')
		print('')
		if img2 == 'n':
			SendImage(to)
		elif img2 == 'y':
			MultipleImages(to)
	elif img == 'n':
		SendMessage(to)
	else:
		print('')
		print(vermelho + '[x] Opção errada...\n')
		main()
	return body, to, from_


def SendMessage(to):
	try:
		message = client.messages.create(
		    body = body, 	
	    	to = to,
	    	from_ = from_,
		)
		print('')
		print(verde +' SMS - SPAM NCF  %s' % to)
		print('')
		print (vermelho + '[*] ID > '+azul+message.sid+end)
		print('')
		time.sleep(25)
	except:
		pass


def SendImage(to):
	print('')
	Animation("  SMS - SPAM NCF   ")
	print('')
	media_url = raw_input("[*] Digite a url da sua imagem > ")
	message = client.messages.create(	
   		body = body, 
   		to = to,
  	 	from_ = from_,
 	 	media_url = media_url,
	)
	print('')
	print ('[+] '+verde+'[x]'+vermelho+' Imagem  Enviada Com Sucesso!' + end)
	print('')

def MultipleImages(to):
	numbers = raw_input(amarelo + '[x] Digite o numero de imagens [2/3] > ')
	print('')
	if numbers == '2':
		media_url1 = raw_input(amarelo + '[x] Digite a url da sua primeira imagem:')
		media_url2 = raw_input(amarelo + '[x] Digite a url da sua segunda imagem:')
		print('')
		message = client.messages.create(
			body = body,   # Message body, if any
	    	to = to,	
    		from_ = from_,
    		media_url=[
       		 	media_url1,
        		media_url2,
    		],
		)
		print('')
		print(verde+'[x]'+vermelho+'Imagens Enviadas Com Sucesso!...')
		print('')
	elif numbers == '3':
		media_url1 = input('[1] Digite a url da sua Primeira imagem:')
		media_url2 = input('[2] Digite a url da sua Segunda imagem:')
		media_url3 = input('[3] Digite a url da sua Terceira imagem:')
		print('')
		message = client.messages.create(
			body = body,  # Message body, if any
    		to=to,
    		from_=from_,
    		media_url=[
   		   		media_url1,
   		     	media_url2,
        		media_url3,
    		],
		)
		print('')
		print(verde+'[x]'+vermelho+'Imagens Enviadas Com Sucesso!...')		
	else:
		print('')
		print(vermelho + "Digite uma opção valida...")
		print('')

def Retrieving():
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	for message in client.messages.list():
		Historico = (message.body)
		print ("Historico de mensagens Enviadas:", Historico )


def SpamNumber():
	global body, to, from_
	body = raw_input(cyanClaro + "[x] Digite sua Mensagem:")
	print('')
	to =   raw_input(cyanClaro + '[x] Digite numero da vitima:')
	print('')
	FloodNumber = int(input(verde + "Digite o numero de Flood:"))
	print('')
	img =  raw_input(amarelo + "[x] Deseja enviar uma imagem? [y/N]")
	print('')
	if img == 'y':
		img2 = raw_input(amarelo + '[x] Deseja enviar mais de uma [1] imagen? [y/N]')
		print('')
		if img2 == 'n':
			for i in rage(1, FloodNumber+1):
				SendImage(to)
				print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
				print('')
		elif img2 == 'y':
			for i in rage(1, FloodNumber+1):
				MultipleImages(to)
				print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
				print('')

	for i in range(1, FloodNumber+1):
		SendMessage(to)
	print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
	print('')

def SPAM():
	global body, to, from_
	print(vermelho + "+==========================================+")
	print(vermelho + "|              Modo de Spam                |")
	print(vermelho + "+==========================================+")
	print('')
	options = raw_input(verde+"[x] Deseja Usar uma lista de Numeros [y/N]?")
	if options == 'n'.lower():
		SpamNumber()
		exit()
	else:
		pass
	print('')	
	body = raw_input(cyanClaro + "[x] Digite sua Mensagem:")
	print('')
	wordlist =   raw_input(cyanClaro + '[x] Digite Sua Lista de Numeros:')
	print('')
	to = open(wordlist, 'r').readlines()
	from_ = from_
	FloodNumber = int(input(verde + "Digite o numero de Flood:"))
	print('')
	img =  raw_input(amarelo + "[x] Deseja enviar uma imagem? [y/N]")
	print('')
	if img == 'y':
		img2 = raw_input(amarelo + '[x] Deseja enviar mais de uma [1] imagens? [y/N] ')
		print('')
		if img2 == 'n':
			for i in rage(1, FloodNumber+1):
				SendImage(to)
				print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
				print('')
		elif img2 == 'y':
			for i in rage(1, FloodNumber+1):
				MultipleImages(to)
				print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
				print('')

	for i in range(1, FloodNumber+1):
		for Number in to:
			SendMessage(Number)
		print purpleClaro + "\r SMS - SPAM NCF - Total enviados: %i" % i
		print('')


def main():
	if opt == '1':
		try:
			Ma1n()
		except KeyboardInterrupt:
			print(vermelho + '\n \n[-] Saindo...')
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
			exit()
	elif opt == '3':
		try:
			Retrieving()		
		except KeyboardInterrupt:
			print(vermelho + "\n \n[-] Saindo....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd
	elif opt == '2':
		try:
			SPAM()
		except KeyboardInterrupt:
			print(vermelho+"\n \n[-] Saindo....")
			time.sleep(3)
			os.system('clear')
			print cyanClaro + BannerEnd

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print(vermelho+'\n\n[-] Saindo...')
		time.sleep(3)
		os.system('clear')
		print cyanClaro + BannerEnd
		exit()
