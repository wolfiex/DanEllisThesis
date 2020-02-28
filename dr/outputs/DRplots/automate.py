import multiprocessing as mp
import sys,os,glob
import numpy as np

def runs(x):
	print(x)
	os.system('npm start index.html "%s"'%x)


data = glob.glob('../*/*_data.csv')

mp.Pool(4).map(runs,data)


#make subplots
wht = 'AE'
for f in glob.glob('../%s/*_data.csv'%wht):
    i = f.split('/')[-1]
    j = i.split('_')[0]
    
    sf = '''\\begin{subfigure}[b]{0.25\\linewidth}
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/DRplots/plots/%s_%s}
    \\caption{%s}
    \\label{fig:%s_%s}
\\end{subfigure}'''%(wht,i.replace('_data.csv','.png'),j,wht,j)
    print(sf)
    
    
    

dirs = np.array([i.split('/') for i in glob.glob('../*/*/legend.png')])
    
print ('\n\n\n\n')
    

for f in dirs:
    wht = f[1]
    i = f[2]
    
    sf = '''\\begin{subfigure}[b]{0.22\\linewidth}
    \\centering
    \\includegraphics[height =\textwidth,angle=-90]{outputs/%s/%s/legend.png}
    \\caption{%s}
    \\label{fig:legend_%s_%s}
\\end{subfigure}'''%(wht,i,i,wht,i)
    print(sf)