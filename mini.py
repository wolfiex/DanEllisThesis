
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

files = glob.glob('*/combigned.tex')

for i in files:

    data = open(i,'r').read()

    data = re.sub(r'\n\s*%[^\n]+','',data)

    os.system('mv %s %s'%(i,i.replace('combigned','grouped/combigned')))

    with open(i,'w') as f:
        f.write(data)


    print(i);

print('fi')
