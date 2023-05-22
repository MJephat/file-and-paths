import csv

with open('/home/jephat/desktop/phase-3/file-and-paths/Ques 4/student.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open (' .') as file:
    #pass file to csv reader(It creates an object reader)
    reader = csv.reader(file)
    for row in reader:
       print(row)

