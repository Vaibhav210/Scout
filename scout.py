import os
import argparse
from pyfiglet import Figlet
from termcolor import colored
import random
import string
import time
#import re


parser = argparse.ArgumentParser()
parser.add_argument('-d','--domainname', type=str, help="Give domain for reconnaissance")
args=parser.parse_args()



def recons(domainname):


	banner()
	dn = domainname.split('/')
	print(domainname)
	 
	s = dn[-1].split('.')

	z = "grep -v 'Failed' "
	os.system('mkdir output')

	if os.path.exists('output/{}'.format(s[0])) == True:
		let = string.ascii_lowercase
		r = ''.join(random.choice(let) for i in range(5))
		s[0] = s[0] + r

		print(colored(("Your output will be saved in output/{}".format(s[0])),'yellow'))
		os.makedirs('output/{}'.format(s[0]))


	else:

		print(colored("Your output will be saved in: output/{}".format(s[0]),'yellow'))
		os.system('mkdir output/{}'.format(s[0]))



	print(colored("______________________________________________Host tool is started______________________________________________\n",'cyan'))

	phuss = 'host '+ domainname +' > '+'output/{}'.format(s[0]) + '/Host_output.txt'
	os.system(phuss)
	
	time.sleep(3)
	os.system(z + 'output/{}'.format(s[0]) + "/Host_output.txt")

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("___________________________________________Traceroute tool is started___________________________________________\n",'cyan'))

	trace = 'sudo traceroute -I '+ domainname +' > '+'output/{}'.format(s[0]) + '/Traceroute_output.txt'
	os.system(trace)
	
	os.system(z + 'output/{}'.format(s[0]) + "/Traceroute_output.txt")

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("______________________________________________Whois tool is started_____________________________________________\n",'cyan'))

	who = 'whois ' + domainname + ' > '+'output/{}'.format(s[0]) + '/Whois_output.txt'
	os.system(who)
	
	time.sleep(3)
	who_sed = "sed -n '1,22p' "
	os.system(z + 'output/{}'.format(s[0]) + "/Whois_output.txt" + "|" + who_sed + 'output/{}'.format(s[0]) + "/Whois_output.txt")

	print(colored("\n-------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("_____________________________________________DNSrecon tool is started____________________________________________\n",'cyan'))

	dns = 'dnsrecon -d '+ domainname +' > '+'output/{}'.format(s[0]) + '/Dnsrecon_output.txt'
	os.system(dns)
	
	time.sleep(3)
	dns_sed = "sed -r 's/^.{4}//' "
	os.system(z + 'output/{}'.format(s[0]) + "/Dnsrecon_output.txt" + "|" + dns_sed + 'output/{}'.format(s[0]) + "/Dnsrecon_output.txt")

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("____________________________________________Subfinder tool is started___________________________________________\n",'cyan'))

	sub = 'subfinder -d '+ domainname +' -silent' +' > '+'output/{}'.format(s[0]) + '/Subfinder_output.txt'
	os.system(sub)

	time.sleep(3)
	os.system(z + 'output/{}'.format(s[0]) + "/Subfinder_output.txt") 

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("______________________________________________Nmap tool is started______________________________________________\n",'cyan'))
	
	nmap(s,z)

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')


	print(colored("_____________________________________________Dirsearch tool is started__________________________________________\n",'cyan'))

	dir = 'python3 dirsearch/dirsearch.py -u ' + domainname + ' -o ' + 'output/{}'.format(s[0]) + "/Dirsearch_output.txt" + ' -q'
	time.sleep(3)
	os.system(dir)

	print(colored("\n------------------------------------------------------DONE------------------------------------------------------",'red'))
	print('\n')

	


def nmap(s,z):

	#pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
	
	grep = "grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' " + 'output/{}'.format(s[0]) + "/Host_output.txt" + ' > ' + 'output/{}'.format(s[0]) + "/ips.txt"
	os.system(grep)

	with open('output/{}'.format(s[0]) + "/ips.txt") as fh:
		fstring = fh.readlines()

	for ip in fstring:
		
		print(colored("\nNmap Scan Is In Progress For " + ip,'yellow'))

		mapp = 'sudo nmap -v -sC -sV -O -T5 ' +ip.strip()+ ' >> ' + 'output/{}'.format(s[0]) + '/Nmap_output.txt'
		#print(mapp)
		os.system(mapp)
		time.sleep(3)
		os.system(z + 'output/{}'.format(s[0]) + "/Nmap_output.txt")




def banner():

	banner1= Figlet(font='slant')
	print(colored(banner1.renderText("               SCOUT"),"red"))

	banner2= Figlet(font='digital')
	print(colored(banner2.renderText("                  Let's Automate Reconnaissance"),"magenta"))

	print(colored('[WRN] USE WITH CAUTION. YOU ARE RESPONSIBLE FOR YOUR ACTIONS.','yellow'))
	print(colored('[WRN] DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE.\n','yellow'))



if __name__=='__main__':
	recons(args.domainname)
