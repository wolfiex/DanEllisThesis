import multiprocessing as mp
import sys,os,glob

def runme(x):
	print(x)
	os.system('npm start index.html "%s"'%x)


data = glob.glob('../*/*/legend.png')

#mp.Pool(4).map(run,data)



for f in data:
	n = f.split('/')
	i = n[1]
	j = n[2]

	sf = '''\\begin{subfigure}[b]{0.25\\linewidth}
    \\centering
    \\includegraphics[width=\\textwidth]{outputs/%s}
    \\caption{%s}
    \\label{fig:legend_%s_%s}
\\end{subfigure}'''%(f.replace('../',''),j,i,j)
	print(sf)
