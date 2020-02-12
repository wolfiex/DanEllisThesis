import os 
import glob

ext = 'aux\|bbl\|blg\|log\|nav\|out\|snm\|toc\|dvi\|lof\|lot\|bcf'.split('\|')

fs = []

for ft in ext: fs.extend(glob.glob('*/*.%s'%ft))
for ft in ext: fs.extend(glob.glob('*.%s'%ft))



for f in fs:
    print('removing ',f)
    os.system('rm '+f.replace(' ','\ '))
    
    
print('all clean')