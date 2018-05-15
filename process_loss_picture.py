# -*- coding: utf-8 -*-  
import os
import shutil
from PIL import Image


dic_raw= {}
for root, dirs , files in os.walk("/home/wc/FaceNet/datasets/CASIA-WebFace/raw"):
        #print 'All files numbers:',root, dirs , files
        #print 'All files numbers:',root, dirs , files
        if "raw" not in root[-7:]:         
           dic_raw[root[-7:]] =[i[0:3] for i in files]  

 
print(len(dic_raw))

 
dic= {}
for root_, dirs_ , files_ in os.walk("/home/wc/FaceNet/datasets/CASIA-WebFace/CASIA-WebFace_mtcnnpy_160"):
        #print 'All files numbers:',root, dirs , files
        #print 'All files numbers:',root_ 
        #print "npy_160" in root_[-7:]

        if "npy_160" not in root_[-7:]:
            dic[root_[-7:]] =[i_[0:3] for i_ in files_]  

 
print(len(dic))

list_ = []
for key,val in dic.items():
    list_.append(key)
    #print type(key),type(val)
    #print list_


#print("npy_160" in list_)
cnt = 0
for ii in list_: #  0000045    0000045/***.jpg
     #print dic[ii] == dic_raw[ii]
     for jj in dic_raw[ii]:
         if jj not in dic[ii]:
            print("loss picture: ",str(ii) +"/"+ str(jj))
            #if not os.path.exists("/home/wc/FaceNet/datasets/CASIA-WebFace/loss_picture/"+str(ii)):
            #         os.mkdir("/home/wc/FaceNet/datasets/CASIA-WebFace/loss_picture/"+str(ii))

            #shutil.copyfile("/home/wc/FaceNet/datasets/CASIA-WebFace/raw/"+str(ii) +"/"+ str(jj)+".jpg",\
            #               "/home/wc/FaceNet/datasets/CASIA-WebFace/loss_picture/"+str(ii) +"/"+ str(jj)+".jpg")
            im = Image.open("/home/wc/FaceNet/datasets/CASIA-WebFace/raw/"+str(ii) +"/"+ str(jj)+".jpg")
            im.resize((160, 160))
            im.save("/home/wc/FaceNet/datasets/CASIA-WebFace/CASIA-WebFace_mtcnnpy_160/"+str(ii) +"/"+ str(jj)+".png")
             
            cnt +=1
print("TMD, loss number is :",cnt)
 










    
