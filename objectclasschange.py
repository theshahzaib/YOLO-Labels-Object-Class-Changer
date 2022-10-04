
import glob

text_files=glob.glob("penvalid/*")

for fl in range(len(text_files)):
    data=(open (text_files[fl],'r')).read().split('\n')

    datstr=[]
    for i in data[0:-1]:
        i='4'+i[1:]+'\n'
        datstr.append(i)

    datstr=''.join(datstr)

    with (open (text_files[fl],'w')) as tfile:
        tfile.write(datstr)

