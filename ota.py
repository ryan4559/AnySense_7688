#check version from https://github.com/ryan4559/AnySense_7688
import sys
import subprocess
import os
import json
import urllib
import urllib2

currentVersion = 0.1

print('[OTA]OTA Start: Retrieve Version Info...')
#version info URL
url = 'http://raw.githubusercontent.com/ryan4559/AnySense_7688/master/version.info'

data = json.load(urllib2.urlopen(url))
netVersion = float(data['VERSION'])

#check version
print '[OTA]Check Version...'
need_update = 0

if netVersion > currentVersion:
	print '[OTA]Need Update!\nCurrent Version:',currentVersion,'--> New Version:',data['VERSION']
	print '[OTA]Clone New Version from github'
	need_update = 1
elif netVersion == currentVersion:
	print '[OTA]No New Version'
	sys.exit(0)

#Clone from github
retcode = 0
if need_update:
	cmd = 'git clone https://github.com/ryan4559/AnySense_7688'
	print cmd
	retcode = subprocess.call(cmd, shell=True)
#=====write under here=====

sys.exit(0)
