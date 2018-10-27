import os


n3 = 'sem'

os.mkdir(n3)
fh=open('exam_data_new.txt','r')

st=fh.readlines()

ka = '1ms'


year = ['15','16','17']


branch = ['CS','IS','EC','EE','EI','IM','CH','BT','TE','CV','ML','AT','ME']


reg = ['0','00']

student = []

#####  branchwise sort


for i in year:
    for j in branch:
        s1 = '1.txt'
        k1 = str(i)
        k2 = str(j)
        if i == '15':
            n2 = 6;
        if i == '16':
            n2 = 4;
        if i  == '17':
            n2 = 2;

        if j == 'CS':
            n1 = 1;
        if j == 'IS':
            n1 = 2;
        if j == 'EC':
            n1 = 3;
        if j == 'EE':
            n1 = 4;
        if j == 'EI':
            n1 = 5;
        if j == 'ME':
            n1 = 6;
        if j == 'BT':
            n1 = 7;
        if j == 'ML':
            n1 = 8;
        if j == 'CH':
            n1 = 9;
        if j == 'AT':
            n1 = 10;
        if j == 'TE':
            n1 = 12;
        if j == 'IM':
            n1 = 11;
        if j == 'CV':
            n1 = 13;

        n1= str(n1)
        n2 = str(n2)
        n3 ='sem/'


        filename = n3 + n1 + n2 + s1
        f = open(filename, 'w')
        s2 = k1 + k2
        print(s2)

        stud = []

        for i in range(len(st)):

            if (st[i].__contains__(s2)):
                name = st[i - 1]

                stud.append(name)

                cgpa = st[i+6]
                cgpa = cgpa.replace('CGPA : ', '')
                cgpa = cgpa.replace('TAL', '0')
                cgpa = float(cgpa)
                stud.append(cgpa)
                student.append(stud)
            stud = []


        student.sort(key=lambda r:r[1] , reverse=True)
        for k in range(len(student)):
            v1 = student[k][0]
            f.write(v1)

            if ( student[k][1] == 0):
                v1 = 'TAL'
            else:
                v1 = str(student[k][1])
            f.write(v1)
            f.write('\n')
        student = []

        f.close()

student = []

for i in year:
    for j in branch:
        s1 = '2.txt'
        k1 = str(i)
        k2 = str(j)
        if i == '15':
            n2 = 6;
        if i == '16':
            n2 = 4;
        if i == '17':
            n2 = 2;

        if j == 'CS':
            n1 = 1;
        if j == 'IS':
            n1 = 2;
        if j == 'EC':
            n1 = 3;
        if j == 'EE':
            n1 = 4;
        if j == 'EI':
            n1 = 5;
        if j == 'ME':
            n1 = 6;
        if j == 'BT':
            n1 = 7;
        if j == 'ML':
            n1 = 8;
        if j == 'CH':
            n1 = 9;
        if j == 'AT':
            n1 = 10;
        if j == 'TE':
            n1 = 12;
        if j == 'IM':
            n1 = 11;
        if j == 'CV':
            n1 = 13;

        n3 = 'sem/'

        n1 = str(n1)
        n2 = str(n2)
        filename = n3 + n1 +n2 + s1
        f = open(filename, 'w')
        s2 = k1 + k2
        print(s2)

        for i in range(len(st)):

            if (st[i].__contains__(s2)):
                name = st[i - 1]

                stud.append(name)

                cgpa = st[i+5]
                cgpa = cgpa.replace('SGPA : ', '')
                cgpa = cgpa.replace('TAL', '0')
                cgpa = float(cgpa)
                stud.append(cgpa)
                student.append(stud)
            stud = []


        student.sort(key=lambda r:r[1] , reverse=True)
        for k in range(len(student)):
            v1 = student[k][0]
            f.write(v1)

            if ( student[k][1] == 0):
                v1 = 'TAL'
            else:
                v1 = str(student[k][1])
            f.write(v1)
            f.write('\n')
        student = []

        f.close()

fh.close()