import os

os.mkdir('usn')

fh=open('exam_data_new.txt','r')

st=fh.readlines()

ka = '1ms'


year = ['15','16','17']


branch = ['CS','IS','EC','EE','EI','IM','CH','BT','TE','CV','ML','AT','ME']


reg = ['0','00']

#####  branchwise USN unsorted


for j in year:
    for i in branch:
        s1 = '3.txt'
        k1 = j
        k2 = i
        if j == '15':
            n2 = 6;
        if j == '16':
            n2 = 4;
        if j  == '17':
            n2 = 2;

        if i == 'CS':
            n1 = 1;
        if i == 'IS':
            n1 = 2;
        if i == 'EC':
            n1 = 3;
        if i == 'EE':
            n1 = 4;
        if i == 'EI':
            n1 = 5;
        if i == 'ME':
            n1 = 6;
        if i == 'BT':
            n1 = 7;
        if i == 'ML':
            n1 = 8;
        if i == 'CH':
            n1 = 9;
        if i == 'AT':
            n1 = 10;
        if i == 'TE':
            n1 = 12;
        if i == 'IM':
            n1 = 11;
        if i == 'CV':
            n1 = 13;

        n1= str(n1)
        n2 = str(n2)
        n3 ='usn/'
        filename = n3 + n1 + n2 + s1
        f = open(filename, 'w')
        s2 = k1 + k2
        print(s2)

        for i in range(len(st)):

            if (st[i].__contains__(s2)):
                name = st[i - 1]

                f.write(name)

                cgpa = st[i+6]
                cgpa = cgpa.replace('CGPA : ', '')
                sgpa = st[i + 5]
                sgpa = sgpa.replace('SGPA : ', '')

                f.write(sgpa)

                f.write(cgpa)

        f.close()

