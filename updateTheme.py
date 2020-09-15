import os
import sys
#os.system('git init')
os.system('git add .')
if len(sys.argv) < 2:
	os.system('git commit -m "update"')
else:
	os.system('git commit -m "' + ' '.join(sys.argv[1:]) + '"')
os.system('git push origin master')

# 强制更新
# os.system('git push -f -u origin master')