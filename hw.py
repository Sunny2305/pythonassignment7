def fileHandle(file):
    try:
        f=open(file,"+a")
        f.writelines(["rollno = 17 ","Name = Sunny ","Class = TYIF "])
        f.seek(0)
        print(f.readline())
    except IOError:
        print("File Operation Failed")

fileHandle(input("Enter the file name to perform operation: "))