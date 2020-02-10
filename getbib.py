'''
A program to span all folders and collate bibliography entries
'''
import glob, os
import bibtexparser
from bibtexparser.bparser import BibTexParser,BibDatabase
from bibtexparser.bwriter import BibTexWriter

fbib = glob.glob('./*/*.bib')



def locate(x):
    return print('\u001b[31m' + os.popen('grep -inr "%s" */*.bib'%x).read() + '\u001b[0m')
 

def dup(x,property):
    y = [i[property] for i in x]
    if len(x) != len(set(y)):
        for j in set(y):
            if y.count(j)>1:
                print('--Duplicate %s %s'%(property,j))
                locate(j)


db = BibDatabase()
entries = []

for i in fbib:
    with open(i) as bibtex_file:
        bdata = bibtexparser.load(bibtex_file, BibTexParser(common_strings = True))
        entries.extend(bdata.get_entry_list())
        

for i in range(len(entries)):
    try:entries[i]['ID']
    except:
        print('--\n\n\nREMOVAL IMMINENT\n',entries[i])
        continue

    try:entries[i]['title'] = entries[i]['title'].title()
    except:
        print('--\n\n'+entries[i]['ID']+'\nNo title\n',entries[i])
        entries[i]['title'] = 'UNTITLED'
        locate(entries[i]['ID'])
    try:entries[i]['year']
    except:
        print('---\n\n'+entries[i]['ID']+'\nNo year\n',entries[i])
        locate(entries[i]['ID'])
        entries[i]['year'] = '2020'
        print ('note="Accessed: 2020-1-1",')
    

dup(entries,'ID')
dup(entries, 'title')


entries = list(filter(lambda x: not hasattr(x,'ID'),entries))

entries.sort(key=lambda x: x['year'], reverse=True)
entries.sort(key=lambda x: x['ID'], reverse=True)

db.entries = entries

writer = BibTexWriter()
writer.indent = '   ' 
writer.comma_first = False  # place the comma at the beginning of the line
with open('bibtex.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))
    
os.system('pdflatex thesis.tex')
bib = []
for i in glob.glob('*/*.aux'):
    bib.append(os.popen('bibtex '+i).read())
    
os.system('pdflatex thesis.tex')
err = os.popen('pdflatex thesis.tex').read()
print('end')
print(bib)

