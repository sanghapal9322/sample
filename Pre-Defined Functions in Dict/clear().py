'''
Syntax:   DictObj.clear()
=>This Function is used for Removing all the(Key,Value) from Dict Object.
=>When we call clear() on empty dict then we get None as Result OR Space as Result

'''

d1 = {10:2,30:3,40:4}
print(d1,type(d1))

d1.clear()
print(d1)
print(d1.clear())  # ----> None

print({}.clear()) # ----> None


