'''
Merge individual files into one 

select tex files as arguments
'''


import os,glob,re,sys
import numpy as np

time = os.popen('date').read() 


backup = True

if backup:
    os.system('git add -A')
    os.system('git commit -m "%s_title"'%time)

print ('commit =', time)

heading = re.compile(r'(?<=\\section\*{0,1}\{).*?(?=\})')

#|\\chapter\*{0,1}\{(.*?)\}|\\paragraph\*{0,1}\{(.*?)\}')   
 
files = glob.glob('*/combigned.tex')

for f in files:
        print(f)
        text = open(f,'r').read()
        new = heading.sub( lambda x: str(x.group()).title(), text)

        with open(f,'w') as replace:
            replace.write(new)
            
            
            
            

    
print('fi')