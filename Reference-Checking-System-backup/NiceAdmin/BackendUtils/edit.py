import os
targets=[filename  for filename in os.listdir(os.getcwd()) if 'html' in filename]
def modify(filename,old,new):
    with open(filename,'r') as iowrapper:
        contents=iowrapper.read()

    txt=contents.replace(old,new)
    with open(filename,'w') as iowrapper:
        print(txt,file=iowrapper)


for target in targets:
    modify(target,"BootstrapMade","MATHUB")

print(targets)