# Write a Python code snippet to open a file named "data.txt" in read mode and print its contents.


with open('/home/jephat/desktop/phase-3/file-and-paths/file/data.txt') as hello_file:
     hello_content = hello_file.read()
print(hello_content)