import os, time
path = 'H:\\tests\\'
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:# and file.find('.MOV')>0:
        if file.find('.mp4')>0 and len(file.split(' '))>1:
            rnm1 = file.split(' ')
            newname = rnm1[0]+'_'+rnm1[1]
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file
print "ok"