# To read the already existing file
"""
f = open("rohit.txt","r")
content = f.read(23)
print(content)

f.close()
"""
"""
# To read line by line
f = open("rohit.txt","rt")
#content = f.read()

for line in f:
    print(line, end="")


f.close()
"""
"""
# Readline function can also be used
f = open ("rohit.txt", "rt")
print(f.readline())
print(f.readline())
f.close()
"""
"""
f = open ("rohit.txt", "rt")
print(f.readlines())
f.close()
"""
