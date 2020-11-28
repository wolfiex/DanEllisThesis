'''
A script to generate the corrections diff

vim example.txt -c "hardcopy > example.ps | q"; ps2pdf example.ps

pip install grip

npm install -g markdown-pdf
'''

import os,glob,re

diff_folder = './diff/'

# os.system('rm %s*.html'%diff_folder)

files = ['thesis.tex']
title = ['Thesis.tex']


chs = list(glob.glob('*_*.tex'))
chs.sort()

for f in chs:

    loc = re.findall('subimport{(.+)/}{combigned.tex}',open(f).read())[0]
    title.append(f)
    files.append(loc+'/combigned.tex')


title.extend(['Glossary','Bibliography'])
files.extend(['glossary.tex','bibtex.bib'])


changes = ['# DanEllisThesis - Change Log','-------------------------']

for i,f in enumerate(files):
    
    changes.append('## ' + title[i])
    
    # submit corrections thesis.tex
    cmd = 'git diff --ignore-space-at-eol -b -w --ignore-blank-lines submit corrections %s '%f #> %s%s'%(f,diff_folder,outname)

    data = os.popen(cmd).readlines()
    print(f,len(data))
    edit = []
    previous = ''
    for i in data:
        i = i.strip('\\n')
        
        if len(i)<5: continue

        # if previous[1:10] == i[1:10]:
        #     edit.append('_a a_')##joint edit
        
        if i[0]=='-':
            edit.append('###### '+i)
        elif i[0]=='+':
            edit.append('##### '+i)
        elif i[0]=='@':
            i = i.split('@@')
            edit.append('### '+i[1])
            #edit.append('#### '+i[-1])
            ## part description not useful
        else:
            edit.append('#### '+i)
            
        previous = i
            
    changes.extend(edit)
    
with open(diff_folder+'changes.md' ,'w') as f:
    f.write('\n'.join(changes))
    
os.system('cd diff && markdown-pdf --css-path my.css changes.md')