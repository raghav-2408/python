file = open("sample.txt", "r") # if mode is not specified then by default "read" mode will be taken as a mode!!
file.close()
# print(file.read()) -> error because file has been closed!!