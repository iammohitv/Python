# ref : https://replit.com/@codewithharry/13-Day13-String-Methods#main.py
a = "#mohit#####"
b = '''this is multiline string

and it works'''
c = "mohitKKK"
print("king, " + a)
print(b)
print(a[0]) #0 indexing in strings


#looping in string

for i in b:
    print(i)

#string slicing
print(a[0:4]) #prints 0123 index of a
print(a[:4])
print(a[1:4])
print(a[0:-3]) #prints 0 till len(a)-3 5-3 basically 2 hence 01

print(len(a)) #length of string is printed

#strings are immutable
# whenever we apply string functions we are getting a new string basically
print(a.upper())
print(a.lower())

print(a.rstrip('#')) #removes last # doesnot work in start
print(a.replace('m','s')) # replaces m to s

print(b.split(" "))# takes space as delimeter
print(b.split())
print(c.capitalize()) #this turns first letter into caps and other all into lower
print(a.count("#"))
print(a.endswith("#"))

print(a.find("#")) # returns first occurence of # if string is not there it will return -1

# print(a.index("*")) returns error as * is not there in a
#islower() returns true/false
