import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup


import time
import timeit

start_time = timeit.default_timer()

fh = open('exam_data_new_2.txt','w')
st = '\n'
fh.write(st)
driver = webdriver.Chrome()
driver.get("http://exam.msrit.edu/")

s=time.clock()
flag = 0


ka = '1ms'


year = ['14','15','16','17']


branch = ['cs','is','ec','ee','ei','im','ch','bt','te','cv','ml','at','me']
#branch = ['te']


reg = ['0','00']


captcha=""


count = 0

for j1 in year:
    print(j1)
    for j2 in branch:
        print(j2)
        x1 = 0

        for j in range(1,300):
            print(j)

            if (len(str(j)) == 1):
                usn = ka + j1 + j2 + reg[1] + str(j)
            elif (len(str(j)) == 2):
                usn = ka + j1 + j2 + reg[0] + str(j)
            elif (len(str(j)) == 3):
                usn = ka + j1 + j2 + str(j)

            ele = driver.find_element_by_id('usn')
            ele.clear()
            ele.send_keys(usn)

            if flag == 0:
                captcha = input('enter captcha')
                flag = 1

            ele = driver.find_element_by_id('osolCatchaTxt0')
            ele.clear()
            ele.send_keys(captcha)

            ele.send_keys(Keys.RETURN)

            ele = driver.page_source

            src = bs4.BeautifulSoup(ele, 'lxml')

            try:
                error = 1
                list = []
                for k in src.select('.bannerH'):
                    string = k.text
                    list.append(string)

                list[0] = 'some sh*t'

            except:
                error = 0

            # print(error)

            if error == 0:
                ####
                x1 = 0

                k = src.select('img')
                img = k[3].get_attribute_list('src')
                st = 'http://exam.msrit.edu/'
                img[0] = st + img[0]
                im = img[0]



                info = []
                for k in src.select('.headingdateWhite'):
                    string = k.text
                    info.append(string)
                info.pop()
                info[1] = info[1].replace('USN : ', '')

                ####
                res_1 = []
                s = src.select('.box')
                for k in range(4):
                    string = s[k].text
                    res_1.append(string)

                res_1[0] = res_1[0].replace('Credits Registered', 'Credits Registered : ')
                res_1[1] = res_1[1].replace('Credits Earned', 'Credits Earned : ')
                res_1[2] = res_1[2].replace('SGPA', 'SGPA : ')
                res_1[3] = res_1[3].replace('CGPA', 'CGPA : ')
                # print(res_1)

                ####
                s = src.select('td')
                string = s[17].text
                info.append(string)
                info[2] = info[2].replace('\n', '')
                info[2] = info[2].replace('\xa0', '')
                info[2] = info[2].replace('Department : ', ' \nDepartment : ')

                # print(info)

                ####

                res_2 = []
                for k in src.select('.even'):
                    for i in k.select('td'):
                        string = i.text
                        res_2.append(string)

                for k in src.select('.odd'):
                    for i in k.select('td'):
                        string = i.text
                        res_2.append(string)

                while (res_2.__contains__('')):
                    res_2.remove('')

                res_2[0] = res_2[0].replace('\n', '')
                for i in range(3, len(res_2), 5):
                    res_2[i] = res_2[i].replace('\n', '')
                    res_2[i] = res_2[i].replace('\t', '')

                # print(res_2)

                #####

                for k in src.select('.headingdate'):
                    string = k.text
                    date = string
                    break

                date = date.replace('\n', '')
                date = date.replace('Print					Provisional Grade Card', '')

                # print(date)

                ####
                fh.write(im)
                fh.write('\n')

                for k in range(len(info)):
                    string = info[k]
                    fh.write(string)
                    fh.write('\n')

                for k in range(len(res_1)):
                    string = res_1[k]
                    fh.write(string)
                    fh.write('\n')

                for k in range(len(res_2)):
                    string = res_2[k]
                    fh.write(string)
                    fh.write('\n')

                fh.write('\n')

                driver.back()
                time.sleep(1)

            else:
                driver.back()
                time.sleep(1)
                x1 = x1 + 1
                if (x1 > 10):
                    break


# for diploma people

year = ['15','16','17']

for j1 in year:
    print(j1)
    for j2 in branch:
        print(j2)
        x1 = 0


        for j in range(400, 500):
            print(j)

            if (len(str(j)) == 1):
                usn = ka + j1 + j2 + reg[1] + str(j)
            elif (len(str(j)) == 2):
                usn = ka + j1 + j2 + reg[0] + str(j)
            elif (len(str(j)) == 3):
                usn = ka + j1 + j2 + str(j)

            ele = driver.find_element_by_id('usn')
            ele.clear()
            ele.send_keys(usn)



            ele = driver.find_element_by_id('osolCatchaTxt0')
            ele.clear()
            ele.send_keys(captcha)

            ele.send_keys(Keys.RETURN)

            ele = driver.page_source

            src = bs4.BeautifulSoup(ele, 'lxml')

            try:
                error = 1
                list = []
                for k in src.select('.bannerH'):
                    string = k.text
                    list.append(string)

                list[0] = 'some sh*t'

            except:
                error = 0

            # print(error)

            if error == 0:
                ####
                x1 = 0

                k = src.select('img')
                img = k[3].get_attribute_list('src')
                st = 'http://exam.msrit.edu/'
                img[0] = st + img[0]
                im = img[0]

                info = []
                for k in src.select('.headingdateWhite'):
                    string = k.text
                    info.append(string)
                info.pop()
                info[1] = info[1].replace('USN : ', '')

                ####
                res_1 = []
                s = src.select('.box')
                for k in range(4):
                    string = s[k].text
                    res_1.append(string)

                res_1[0] = res_1[0].replace('Credits Registered', 'Credits Registered : ')
                res_1[1] = res_1[1].replace('Credits Earned', 'Credits Earned : ')
                res_1[2] = res_1[2].replace('SGPA', 'SGPA : ')
                res_1[3] = res_1[3].replace('CGPA', 'CGPA : ')
                # print(res_1)

                ####
                s = src.select('td')
                string = s[17].text
                info.append(string)
                info[2] = info[2].replace('\n', '')
                info[2] = info[2].replace('\xa0', '')
                info[2] = info[2].replace('Department : ', ' \nDepartment : ')

                # print(info)

                ####

                res_2 = []
                for k in src.select('.even'):
                    for i in k.select('td'):
                        string = i.text
                        res_2.append(string)

                for k in src.select('.odd'):
                    for i in k.select('td'):
                        string = i.text
                        res_2.append(string)

                while (res_2.__contains__('')):
                    res_2.remove('')

                res_2[0] = res_2[0].replace('\n', '')
                for i in range(3, len(res_2), 5):
                    res_2[i] = res_2[i].replace('\n', '')
                    res_2[i] = res_2[i].replace('\t', '')

                # print(res_2)

                #####

                for k in src.select('.headingdate'):
                    string = k.text
                    date = string
                    break

                date = date.replace('\n', '')
                date = date.replace('Print					Provisional Grade Card', '')

                # print(date)

                ####
                fh.write(im)
                fh.write('\n')

                for k in range(len(info)):
                    string = info[k]
                    fh.write(string)
                    fh.write('\n')

                for k in range(len(res_1)):
                    string = res_1[k]
                    fh.write(string)
                    fh.write('\n')

                for k in range(len(res_2)):
                    string = res_2[k]
                    fh.write(string)
                    fh.write('\n')

                fh.write('\n')

                driver.back()
                time.sleep(1)

            else:
                driver.back()
                time.sleep(1)
                x1 = x1 + 1
                if (x1 > 10):
                    break




fh.close()

driver.close()

end_time = timeit.default_timer()

print('time : ', end_time-start_time)