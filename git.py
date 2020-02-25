import sys,os

os.system('python clean.py')
os.system('git add -A')

os.system('git commit -m "%s"'%sys.argv[1])
print('push')
os.system('git push')
