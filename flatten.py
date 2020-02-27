import os


time = os.popen('date').read() 


os.system('git add -A')
os.system('git commit -m "%s"'%time)