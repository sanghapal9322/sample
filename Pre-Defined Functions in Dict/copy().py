# 2.copy()
'''
Syntax: DictObj2=DictObj1.copy()
=>This Function is used for Copying the content of DictObj1 into Dictobj2( Implements Shallow Copy).
'''
d1 = {"name":"sangha","age":20,"height":5.2} # {'name': 'sangha', 'age': 20, 'height': 5.2} <class 'dict'> 1965066841472
print(d1,type(d1),id(d1))
print(f"===================shallow copy =================")
d2 = d1.copy()
print(d2,type(d2),id(d2)) # {'name': 'sangha', 'age': 20, 'height': 5.2} <class 'dict'> 1965067264512
print("="*50)
d2["roll_no"]=23
d2["city"]="hyd"
print(d2,type(d2),id(d2))
print(d1,type(d1),id(d1))
print("="*50)
print(f"===================Deep copy =================")
d3 = d1
print(d3,type(d3),id(d3))
print(d1,type(d1),id(d1))
