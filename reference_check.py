'''
Reference Linter

Get all the thesis text and compare references to labels
hilight any mismatches.

Dan Ellis
'''


import os,re
import numpy as np
tf = os.popen('grep -inr subimport *.tex').read()

paths = np.array(re.findall(r'\\subimport{(.*)}{(.*\.tex)}',tf) )  

get = [''.join(i) for i in paths]


thesis = ''

for i in get: thesis+= open(i).read()+'\n'


# CITATIONS 
print('-'*20) 

keys = set([i.replace(' ','') for i in re.findall(r'@[^{]*{(.*),',open('bibtex.bib').read())])

citations = []
for i in re.findall(r'\\cite.{0,1}{([^}]*)}',thesis): citations.extend(i.replace(' ','').split(','))
citations = set(citations)

wrong = set(filter(lambda x: ':' in x, citations))
citations = set(filter(lambda x: ':' not in x, citations))

if len(keys) != len(citations):
    
    print('\u001b[34m' + 'Warning Unused Citations' + '\u001b[0m') 
    for i in keys-citations:
        print ('-- extra: ', i, '--')

    print('\u001b[31m' + 'Citation Missing' + '\u001b[0m') 
    for i in citations-keys:
        print ('-- MISSING: ', i, '--')
        
    print('\u001b[31m' + 'Mistype Cite/Ref' + '\u001b[0m') 
    for i in wrong:
        print ('-- MISSING: ', i, '--')
            
          
# FIGURES 
print('-'*20) 

labels = re.findall(r'\\label{([^}]*)}',thesis)


if len(labels)!= len(set(labels)):
    print('\u001b[31m' + 'Duplicate Labels' + '\u001b[0m')
    for i in set(labels):
        if labels.count(i)>1:
            print ('-- FIX LABEL ', i, '--')
            print (os.popen('grep -inr \label{"%s"} */*.tex'%i).read())

labels = set(labels)

ref = []
for i in re.findall(r'\\[auto]{0,4}ref{([^}]*)}',thesis): ref.extend(i.replace(' ','').split(','))
ref = set(ref)

if len(ref) != len(labels):
    print('\u001b[34m' + 'Warning Unreferenced Items' + '\u001b[0m') 
    for i in labels-ref-set(filter(lambda x:'sec:'in x, labels)):
        print ('-- unref: ', i, '--')
        print (os.popen('grep -inr \label{"%s"} */*.tex'%i).read())


    print('\u001b[31m' + 'Label Missing' + '\u001b[0m') 
    for i in ref-labels:
        print ('-- NOLABEL: ', i, '--')
        print (':'.join(os.popen('grep -inr "%s" */*.tex'%i).read().split(':')[:2])+'\n')




