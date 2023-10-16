"""
#To create a txt file and write in the file
#Or to replace the content of already existing file
f = open("rohit2.txt","w")
f.write("Rohit is a good boy.")
f.close()
"""
"""
# Now to ignore replace and rather add new content
#In already existing file
f = open("rohit2.txt","a")
f.write("Rohit is the king of this universe.\n")
f.close()
"""
"""
f = open("rohit2.txt","a")
a = f.write("Rohit is the king of this universe.\n")
print(a)
f.close()
"""
#Handle both read and write
f = open("rohit.txt","r+")
print(f.read())
f.write("Thank you.\n")
f.close()
