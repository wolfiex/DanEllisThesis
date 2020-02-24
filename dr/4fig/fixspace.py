import glob,os

fl = glob.glob('*/*.pdf')

for i in fl:
	os.system('mv %s %s'%(i,i.replace
