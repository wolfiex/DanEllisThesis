import sys,os

os.system('python clean.py')
os.system('git add -A')


size = os.path.getsize('thesis.pdf')/(1024*1024)
print ('\n\nthesis size: %.2f MB\n\n'%size)

if size>100:
    print('removing thesis.pdf - its too large')
    os.system('git rm --cached thesis.pdf')


os.system('git commit -m "%s"'%sys.argv[1])
print('push')
os.system('git push')
