#ipfinder
import subprocess
testy=subprocess.check_output(['nmap','-sP','192.168.1.0/24'])
listy=testy.split('\n')
for kindlehandle in listy:
	if 'kindle' in kindlehandle:
		posi=listy.index(kindlehandle)
		themap=listy[posi]
		themapcut1=themap.split('(')
		themapcut2=themapcut1[1].split(')')
		ip=themapcut2[0]
		print ip
