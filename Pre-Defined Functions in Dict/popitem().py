# 4. popitem()
'''
Syntax:   Dictobj.popitem()
=>This Function is used for Removing the Last (Key,Value) from Dict Object.
=>If we call this function on empty dict then we get KeyError.
'''

d1 = {"name":"sangha","age":32,"height":5.3,"degree":"Btech"}

print(d1,type(d1),id(d1),len(d1))
print(d1.popitem()) # ('degree', 'Btech')
print(d1)# it will remove  "degree":"Btech"

print(d1.popitem())
print(d1)

print(d1.popitem())
print(d1)

print(d1.popitem())
print(d1)

d1.popitem()
print(d1)

print(d1.popitem())  # KeyError: 'popitem(): dictionary is empty'
print(d1)
