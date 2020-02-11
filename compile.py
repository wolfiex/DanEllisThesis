
import os 
def make(filename):
    os.system('pdflatex '+filename)
    
    bib = []
    bf = glob.glob('*.aux')
    for i in bf:
        bib.append(os.popen('bibtex '+i).read())
        
    os.system('pdflatex '+filename)
    err = os.popen('pdflatex '+filename).read()

    print(re.findall(r'[Ww]arning:.*line\s\d+\.',err) )

    for i,b in enumerate(bib):
        print ('-'*10,'\n',bf[i],'\n','-'*10)
        for j in re.split(r'\n',b):
            print(j)

    print('Finished')
    
def autorun(globstr,filename):
    import glob
    import ipyReload as ipr 
    #conda install -c wolfiex ipyreload
    
    files = glob.glob(globstr)
    
    def callback():
        make(filename)
        
    
    for i in files:
        print('watching ',i)
        ipr.watch(i,callback)
        
        
if __name__ == '__main__':
    autorun('*/*.tex','thesis.tex')