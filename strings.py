a = "mohit"
b = '''this is multiline string

and it works'''
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