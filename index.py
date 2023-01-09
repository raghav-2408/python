file = open("sample.txt", "r")
print(file.read())
file.close()
# print(file.read()) -> error because file has been closed!!