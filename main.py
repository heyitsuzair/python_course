# f = open('myFile.txt', 'r')
# while True:
#     line = f.readline()

#     if not line:
#         break
#     print(line)


f = open('myFile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()