from PIL import Image
import os
import glob

def read_image(cwd,newpath):
cwd='/home/fly/下载/2/'
newpath='/home/fly/下载/1/'
 for roots,dirs,files in os.walk(cwd):
  print(dirs)
  for i in dirs:
   print(i)
   os.chdir(cwd+i)
   for pic in glob.glob('*.jpg'):
    _,image=pic.split('_')
    img=image.split('.')[0]
    print(img)
    if len(img)!=0:
     if int(img)%2!=0:
      im=Image.open(pic)
      im.save(newpath+i+'/'+pic)
