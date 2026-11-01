# pop(key)
'''
=>Syntax:   Dictobj.pop(Key)
=>This Function is used for Removing the (Key,Value) from Dict Object Based On Value of Key.
=>If the Value of Key Does not Exist then we get KeyError.

'''

d1 = {10:"python",20:"java",30:"c++",40:"c"}
print(d1,type(d1),len(d1),id(d1))

d1.pop(10) # 10 value of key will be remove
print(d1,len(d1))

d1.pop(20)
d1.pop(30)
d1.pop(40)
print(d1,type(d1),len(d1),id(d1))

print("="*60)
a={}.pop(10)
print(a) #KeyError: 10

d1.pop(100)
print(d1,type(d1),len(d1),id(d1)) # KeyError: 100