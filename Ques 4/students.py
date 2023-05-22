import csv

with open('/home/jephat/desktop/phase-3/file-and-paths/Ques 4/student.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('/home/jephat/desktop/phase-3/file-and-paths/Ques 4/student.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[1] < '18':
            with open ('/home/jephat/desktop/phase-3/file-and-paths/Ques 4/young_student.txt','a') as student_file:
                student_file.write(str(row)+ '\n')
        else:
            print

