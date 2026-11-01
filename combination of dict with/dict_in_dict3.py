d1={"sno":10,"name":"RS","mm":{"c":25,"c++":28},"sm":{"c":60,"c++":55},"cn":"JNTU"}
print(d1,type(d1))

'''
get() this function give values of value by passing value of key.. if value of key does not exist then we get non as result or space as result
dictobj[key]  = this is same as get() but difference is when key is not present in a given dict it will gives keyError
'''

print("="*70)
v=d1.get("mm")
print(v)
value = d1["mm"]
print(value)
print("="*70)
v = d1.get("sm")
print(v)
value=d1["sm"]
print(value)

# add the value in mm "os":22
v_add = d1.get("mm")["os"]=22
print(v_add)
print(d1)  #

v_ad = d1["mm"]["python"]=30
print(v_ad)
print("=======addition of all marks of mm ========")
add = d1.get("mm").get("c") + d1.get("mm").get("c++") + d1.get("mm").get("os") + d1.get("mm").get("python")
mm = d1.get("mm")
print("mm=",mm)
print("addition of total subject marks : = ",add)
print(d1)

print("="*70)

# add sm "os":22 and "ptython":30
d1["sm"]["os"]=22
d1["sm"]["python"]=30
sm= d1.get("sm")
print("sm=:",sm)
print("====addtion of all marks ======")
add = d1["sm"]["c"] + d1["sm"]["c++"] + d1["sm"]["os"] + d1["sm"]["python"]
print(add)
print(d1)

print("="*70)

# calculate all marks of mm and add to the mm into the tm
d1["mm"]["tm"]=d1.get("mm").get("c")+d1.get("mm").get("c++")+d1.get("mm").get("os")+d1.get("mm").get("python")
print(d1,type(d1))
# calculate all marks of sm and add to the sm into the tm
d1["sm"]["tm"]=d1.get("sm").get("c")+d1.get("sm").get("c++")+ d1.get("sm").get("os") + d1.get("sm").get("python")
print(d1)
