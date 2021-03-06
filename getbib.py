'''
A program to span all folders and collate bibliography entries.

Checks:
    - duplicated key names
    - missing Keys
    - missing Years
    - missing ID
    - missing Author

Additions:
    - url to howpublished
'''
import glob, os, re
import bibtexparser
from bibtexparser.bparser import BibTexParser,BibDatabase
from bibtexparser.bwriter import BibTexWriter

os.system('mv bibtex.bib bibtex.bibbackup')

fbib = glob.glob('./*/*.bib')


title_correct=[
['Voc','VOC'],
['Dsmacc','DSMACC'],
['Tuv','TUV'],
['Geoschem','GEOSChem'],
['Kpp','KPP'],
['Mcm','MCM'],
]


print(fbib)

stp = re.compile(r'"|\'|\{|\}|')

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

keys = []

for i in fbib:
    txt = open(i).read()
    keys.extend(re.findall(r'@[^{]*{(.*),',txt))

    with open(i) as bibtex_file:
        print(i)
        bdata = bibtexparser.load(bibtex_file, BibTexParser(common_strings = True))
        entries.extend(bdata.get_entry_list())


for i in range(len(entries)):
    try:entries[i]['ID']
    except:
        print('--\n\n\nREMOVAL IMMINENT\n',entries[i])
        continue

    try:
        title = entries[i]['title'].title()
        for j in title_correct:
            title = title.replace(*j)
        entries[i]['title'] = title
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

    try:entries[i]['journal']
    except:
        try: entries[i]['journal'] = entries[i]['publisher']
        except:
            #print('---\n\n'+entries[i]['ID']+'\nNo Journal\n',entries[i])
            entries[i]['journal'] = 'online'

    try:
        url = entries[i]['url'].replace('\\url','')
        entries[i]['note']= '\\url{%s}'%stp.sub('',url)
        del entries[i]['url']
        del entries[i]['howpublished']
    except:
        None
    try:del entries[i]['keywords']
    except:None
    try:del entries[i]['abstract']
    except:None

dup(entries,'ID')
dup(entries, 'title')


entries = list(filter(lambda x: not hasattr(x,'ID'),entries))

entries.sort(key=lambda x: x['year'], reverse=True)
entries.sort(key=lambda x: x['ID'], reverse=True)

db.entries = entries


if len(keys)!= len(set(keys)):
    print('\u001b[31m' + 'Duplicate Keys' + '\u001b[0m')
    for i in set(keys):
        if keys.count(i)>1:
            print ('-- Duplicate ', i, '--')

if len(set(db.entries_dict.keys())) != len(set(keys)):
    print('\u001b[31m' + 'Unparsed Keys' + '\u001b[0m')
    for i in set(keys) - set(db.entries_dict.keys()):
        print ('-- MISSING: ', i, '--')





writer = BibTexWriter()
writer.indent = '   '
writer.comma_first = False  # place the comma at the beginning of the line
with open('bibtex.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))

print('bibtex written')
