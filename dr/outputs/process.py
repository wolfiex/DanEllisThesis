import glob
import pandas as pd
import sklearn
from sklearn.metrics import silhouette_score

fls = glob.glob('*/*.csv')



print (fls)


res = []

for f in fls:
    df = pd.read_csv(f)


    score = silhouette_score(df[['x','y']].values,df.label)
    n= f.split('/')

    res.append([n[0],n[1].split('_')[0],'%.4f'%score,len(set(df.label))])


resdf = pd.DataFrame(res,columns = 'DR input silhouette groups'.split())

resdf = resdf.sort_values(['DR','silhouette'],ascending=False)  

print(resdf.to_latex(index=False))  







print ('fi')