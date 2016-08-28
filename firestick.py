#!/usr/bin/python
import os #for shell commands
import urllib #attempting to just get the live file
import subprocess #hopefull this does away with the os shit
yesno='n' #Initializing the ip verification variable

#defining the function that actually installs kodi
def installkodi(addy):
	raw_input('Ok, here we go. This will probably take a minute\n\n\n\n\n\n\n\n\n\n\nPRESS ENTER')
	subprocess.call('adb kill-server',shell=True)
	subprocess.call('adb connect '+addy,shell=True)
	subprocess.call('adb install kodi.apk',shell=True)
	raw_input('\n\n\n\n\n\n\n\n\n\nProvided no errors happened there, you should be good to go. Have a good one.\n\n\n\n\n\n\n\n\n\n\nPlease press enter to close the program')


raw_input('Welcome to the program that will fuck up your Firestick\n\nPress enter to continue')

#while yesno!='y':
#	ip=raw_input('First off, what is the IP address of your firestick on the network? \n\n(by the way, you should already have plugged it in and hooked it up to the network):')
#	#figuring out whether or not you're stupid
#	yesno=raw_input("So that\'s " + ip + "? (y/n):")

testy=subprocess.check_output(['nmap','-sP','192.168.1.0/24'])
listy=testy.split('\n')
for kindlehandle in listy:
	if 'kindle' in kindlehandle:
		posi=listy.index(kindlehandle)
		themap=listy[posi]
		themapcut1=themap.split('(')
		themapcut2=themapcut1[1].split(')')
		ip=themapcut2[0]
		print 'Looks like your firestick IP is '+ip+'. Does that seem right? \n\n\nDon\'t care. \n\n\n\n\nWe''re going for it'


	
dly=raw_input('Do you need to download the apk file to install? (y/n):')
if dly=='y':
	print 'attempting a thing'
	urllib.urlretrieve('http://mirrors.kodi.tv/releases/android/arm/kodi-16.1-Jarvis-armeabi-v7a.apk','kodi.apk')
else:
	raw_input('\n\n\n\nOk...If you already have the Kodi apk, it just has to be in the same directory as this program and named \'kodi.apk\'\n\n\n\n\n\n\press enter to continue')
installkodi(ip)
