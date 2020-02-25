import multiprocessing as mp
import sys,os,glob

def run(x):
	print(x)
	os.system('npm start index.html "%s"'%x)


data = glob.glob('../*/*_data.csv')

#mp.Pool(4).map(run,data)


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