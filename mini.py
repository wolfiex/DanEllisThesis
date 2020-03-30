
import os,glob,re,sys
import numpy as np

time = os.popen('date').read()

start = input('type go\n')
if start != 'go':
    sys.exit('no go')

backup = True

if backup:
    os.system('git add -A')
    os.system('git commit -m "minfy: %s"'%time)

print ('commit =', time)
