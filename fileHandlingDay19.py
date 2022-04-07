# File handling
#mode
# a -> to append content in the existing file throws error if not exist
# w-> to write content in the existing file throws error if not exist
# r -> to read content of the existing throws error if not exist
# x-> to create new file throwa error if already exist

# source directory while - r, w, a
# destination directory while - x
# open() - takes two parameter 1. source or directory 2. mode
#close() - to close the opened file
# read()- to read whole content of the file
# readline() - to read single line of file
# readlines() - returns all line in list with index
# write() - to append or write content in the file

# read()
# method one - backslash
file = open(r"c:\Users\Dell\Documents\demo.txt")
print(file.read()) # reading file
file.close() # closing file

# method 2 - double forward slash
f = open("c://Users//Dell//Documents//demo.txt")
print(f.read())
f.close()
# append
# method one - single back slash
file = open("c:/Users/Dell/Documents/demo.txt","a")
file.write("\n this is morining magh session of python.")
file.close()
print("\n")
f = open("c:\\Users\\Dell\\Documents\\demo.txt","r")
print(f.read())
f.close()
print("\n")


# difference between append and write
# append -> simply add new content from the last end point of the file 
# writes -> removes or clears all content in the file and adds new conntent

# write

file = open("c:\\Users\\Dell\\Documents\\demo.txt","a")
file.write("\n welcome to mind riser")
file.close() # closing file
f = open("c:\\Users\\Dell\\Documents\\demo.txt","r")
print(f.read())
f.close()
print("\n")

# readline()
f = open("c:\\Users\\Dell\\Documents\\demo.txt","r")
print(f.readline())
print(f.readline())
f.close()
print("\n")

#with parameter
f = open("c:\\Users\\Dell\\Documents\\demo.txt","r")
print(f.readline(3))
print(f.readline(6))
f.close()
print("\n")

# with parameter -> readlines
f = open("c:\\Users\\Dell\\Documents\\demo.txt","r")
print(f.readline(0))
print(f.readline(1))
f.close()
print("\n")



















