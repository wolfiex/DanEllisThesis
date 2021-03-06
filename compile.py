
import os, sys, glob, re, subprocess
# import clean


def make(filename):
    os.system('pdflatex '+filename)
    print('.')
    bib = []
    bf = glob.glob('*.aux')
    for i in bf:
        os.popen('bibtex '+i)
        os.popen('bibtex '+i)
        bib.append(os.popen('bibtex '+i).read())
    print('.')
    os.system('pdflatex '+filename)
    print('.')
    #err = os.popen('pdflatex '+filename) # .read()

    p = subprocess.Popen(['pdflatex',filename], stdout=subprocess.PIPE)
    err = p.communicate()[0].decode('utf-8',errors='ignore')
    print('.')
    print(re.findall(r'[Ww]arning:.*line\s\d+\.',str(err)) )

    with open('warnings.txt','w') as f:
        f.write('\n'.join(re.findall(r'[Ww]arning:.*line\s\d+\.',str(err))))

        for i in range(2):f.write('------------\n')
        

        for i,b in enumerate(bib):
            print ('-'*10,'\n',bf[i],'\n','-'*10)
            for j in re.split(r'\n',b):
                print(j)
                f.write(j+'\n')

    print('Finished')

def autorun(globstr,filename):
    import ipyReload as ipr
    #conda install -c wolfiex ipyreload

    files = glob.glob(globstr)

    def callback():
        make(filename)


    for i in files:
        print('watching ',i)
        ipr.watch(i,callback)


if __name__ == '__main__':

    try:
        if sys.argv[1]=='True':
            autorun('*/*.tex','thesis.tex')
    except:
        make('thesis.tex')
        #import clean
