'''
Merge individual files into one 

select tex files as arguments
'''


import os,glob,re,sys
import numpy as np

time = os.popen('date').read() 


backup = False

if backup:
    os.system('git add -A')
    os.system('git commit -m "%s_title"'%time)

print ('commit =', time)

heading = re.compile(r'\\[sub]{0,6}section\*{0,1}\{(.0*)\}|\\chapter\*{0,1}\{(.0*)\}|\\paragraph\*{0,1}\{(.0*)\}')   
 
files = glob.glob('*/combigned.tex')

for f in files:
        print(f)
        
        text= open(f,'r').read()
        for i in heading.finditer(text):
            print (i)
    
print('fi')