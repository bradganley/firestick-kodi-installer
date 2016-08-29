#!/usr/bin/python
import os #for shell commands
import sys # for auto ip stuff
import socket #more ip stuff
import netifaces # "" 
import urllib #attempting to just get the live file
import subprocess #hopefully this does away with the os shit

myiface = 'enp0s5'

#Converts subnet mask to slash notation (found online).
def get_net_size(netmask):
    binary_str = ''
    for octet in netmask:
        binary_str += bin(int(octet))[2:].zfill(8)
    return str(len(binary_str.rstrip('0')))

#Function to check for programs we need.
def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

#Defining the function that actually installs kodi
def installkodi(addy):
	raw_input('\nOk, here we go. This will probably take a minute...\n\n\nPRESS ENTER\n')
	subprocess.call('adb kill-server',shell=True)
	subprocess.call('adb connect '+addy,shell=True)
	subprocess.call('adb install kodi.apk',shell=True)
	raw_input('\n\n\nProvided no errors happened there, you should be good to go. Have a good one.\n\n\nPlease press enter to close the program')

#Function to download kodi if needed.
def getkodi():
	#If kodi.apk doesn't exist, download it.	
	if not os.path.isfile('kodi.apk'):
		print '\nattempting a thing...\n'
		urllib.urlretrieve('http://mirrors.kodi.tv/releases/android/arm/kodi-16.1-Jarvis-armeabi-v7a.apk','kodi.apk')

#Try to get the IP for automatic install.
def getfireip():
	print("\nBe patient as we try to locate the firestick on your network...\n")
	
	#Get machine ip and netmask to know network to search.	
	addrs = netifaces.ifaddresses(myiface)
	ipinfo = addrs[socket.AF_INET][0]
	address = ipinfo['addr']
	netmask = ipinfo['netmask']
	cidr=get_net_size(netmask.split('.'))

	#Find firestick and return ip.
	findfire=subprocess.check_output('nmap -sS -p8008 --open '+address+'/'+cidr+' | grep -B 4 Amazon | cut -d " " -f 5 | head -n 1', shell=True)
	print '\nLooks like your firestick IP is '+findfire.rstrip()+'. Does that seem right? \n\nDon\'t care. \n\nWe\'re going for it\n\n'
	return str(findfire.rstrip())


#Begin running program and display options to end users.
def main():

	print('Welcome to the program that will fuck up your Firestick!')

	ans=True
	while ans:
		print ("""
		1.) Automatic Install
		2.) Manual Install
		3.) Exit
		""")
		ans=raw_input("What would you like to do? \n") 
		if ans=="1": 
			#Check if nmap is installed before running autoinstall.
			if cmd_exists("nmap") == False:
				exit('\nAuto install requires nmap to be installed, install, and try again.\n')
			
			#If automatic install tell the user and try to grab ip and pass to installkodi.		
			print("\nTrying autoinstall (noob friendly)...\n")
			getkodi()
			installkodi(getfireip())
			exit()
		elif ans=="2":
			#If manual install ask user for ip, pass to installkodi.		
			print("\nRunning in manual mode (advanced users)...\n") 
			ipaddr=raw_input('\nWhat is the ip address of your firestick?\n')		
			getkodi()		
			installkodi(ipaddr)
			exit()
		elif ans=="3":
			#Message for users who exit install.		
			print("\nPsh we didn't want you running this anyway!\n")
			exit()
		else:
			#Message for options outside what we defined.
			print("\nMmmm we gave you your options...\n") 

#Check if script is run as root, or sudo root, else exit.
if not os.geteuid() == 0:
	exit('Script must be run as root or with sudo command.')

#Check if ADB is installed.
if cmd_exists("adb") == False:
	exit('\nADB is required for both install options, please install before running.\n')

main()
