import os
import sys
#os.system('git init')
os.system('git add .')
if len(sys.argv) < 3:
	os.system('git commit -m "update"')
else:
	os.system('git commit -m "' + argv[2] + '"')
os.system('git push origin master')