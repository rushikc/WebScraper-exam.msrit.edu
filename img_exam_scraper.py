


import time
import os
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

os.mkdir('img')

fh = open('examdata.txt','r')

text = fh.readlines()

flag = 0
count = 1988
for k in text:
    # if(k.__contains__('Thumbnail_User_Original_11074_20150725133344.jpg') or flag):
    #     flag = 1
    # if(k.__contains__('http://exam.msrit.edu//images') and flag):

    if (k.__contains__('http://exam.msrit.edu//images')):
        url = k;
        k = k.replace('http://exam.msrit.edu//images/students/','')
        url = url.replace(' ','%20')
        k = 'img/'+ k;
        print(k)
        time.sleep(0.01)
        urllib.request.urlretrieve(url,k)
        count +=1
        print(count)

fh.close()





