#check NTP server and sync time
import sys
import subprocess
import time

print('[NTP]Sync Time Start...')
subprocess.call('date', shell=True)
cmd = 'ntpd -p time.stdtime.gov.tw'
subprocess.call(cmd, shell=True)

for i in range(1,11):
	print i
	time.sleep(1)
subprocess.call('date', shell=True)
print('[NTP]Sync Time End...')
sys.exit(0)
