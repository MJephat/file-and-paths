import csv

with open('/home/jephat/desktop/phase-3/file-and-paths/Ques 4/student.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)