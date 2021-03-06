import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

'''
cd appendices/ && python makeindex.py && cd ../
'''


import re,glob

from nltk.corpus import stopwords
stop = list(stopwords.words('english'))
stop.extend('section subsection subsubsection figure table item paragraph begin end caption autoref includegraph  png pdf textwidth endsubfigure subfigure the is this centering label textbf textit emph fig cite citep width height includegraphics sec use ce ch footnote figures shown use used much often within show contain'.split())


files = glob.glob('../*_*.tex')
files.sort()


corpus = []
title = []
for f in files:
    try:
        dir = open(f,'r').read()
        loc = re.findall(r'\\subimport\{([^\}]+)',dir)[0]
        text = open('../%scombigned.tex'%loc,'r').read().lower()
        title.append(re.findall(r'\\chapter\{([^\}]+)',dir)[0])

        text = re.sub(r'[\._\W\s\d]+',' ',re.sub(r'-|([^\\]\%[^\n]+)','',text ))
        corpus.append(text)
    except:None



vectorizer = TfidfVectorizer(analyzer = 'word',stop_words=set(stop))
vectors = vectorizer.fit_transform(corpus)
names = vectorizer.get_feature_names()
data = vectors.todense().tolist()
# Create a dataframe with the results
df = pd.DataFrame(data, columns=names,index=title)



tfidf = '''
\\chapter{Chapter Keywords}
This section uses the Term Frequency Inverse Document Frequency to determine the keywords of each chapter - a techneque which has been described in \\autoref{ch3} and \\cite{frankenstein}. Text size corresponds to the importance of each word.


'''

N = 100;
for i in df.iterrows():
    print('\n\n',i[0])
    tfidf += '\n\n \\section{%s}\n {\\fontfamily{cmtt}\\selectfont \\parbox{\\textwidth}{\n'%i[0]
    rankings = i[1].sort_values(ascending=False)[:N]
    print(rankings)

    for i in rankings.iteritems():
        tfidf += '\\size{%d}{ %s }'%(1+i[1]*100,i[0].upper())

    #tfidf=tfidf[:-2]
    tfidf+='} }'

with open('keywords.tex','w') as f:
    f.write(tfidf)
