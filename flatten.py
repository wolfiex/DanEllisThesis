'''
Merge individual files into one 

select tex files as arguments
'''


import os,glob,re,sys
import numpy as np

time = os.popen('date').read() 

start = input('type go\n')
if start != 'go': 
    sys.exit('no go')

backup = True

if backup:
    os.system('git add -A')
    os.system('git commit -m "%s"'%time)

print ('commit =', time)

chp = sys.argv[1:]#glob.glob('*_*.tex')
loc = re.compile(r'.*\{(.*)\}\{(.*)\}')    

print ('flattening ',chp)

for c in chp:
    dall = open(c,'r').readlines()
    data = list(filter(lambda x : 'subimport' in x and '%' not in x , dall))
    
    


    where = np.array([loc.match(i).groups() for i in data])

    dirloc = set(where[:,0])
    if len(dirloc) != 1:
        print ('Too many dirs',c,dirloc) 
        continue 
    else:
        dirloc = list(dirloc)[0]
        
    dall = ''.join(dall).replace('\\subimport','%\\subimport').replace('\\chapterbib','\\subimport{%s}{combigned.tex} \n\n\\chapterbib'%dirloc)

    
    if os.path.exists(dirloc+'combigned.tex'):
        print (c, 'EXISTS - skipping.')
        continue
    
    with open(c,'w') as f:
        f.write(dall)

    cmb = open(dirloc+'combigned.tex','w')        

    os.system('mkdir %sgrouped'%dirloc)
    for i in where:
        
        cmb.write('\n')
        cmb.write(open(''.join(i)).read())
        
        #ros.system('mv %s%s %sgrouped/'%(i[0],i[1],dirloc) )
        
    print ('Moved',where,c)
    
    
print('fi')