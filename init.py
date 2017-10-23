#execute when boot
import sys
import subprocess

print('[System]Start')

#fix git-pull(once)
print('[System]fix git-pull bug')
subprocess.call('ln -s /usr/bin/git /usr/lib/git-core/git', shell=Ture)

#sync system time
subprocess.call('python ntp.py', shell=True)

#check OTA

#run AnySense
print('[System]AnySense Start')
subprocess.call('python AnySense.py', shell=True)

print('[System]Init done!')
sys.exit(0)
