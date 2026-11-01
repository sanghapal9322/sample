d1={"sno":10,"name":"RS","mm":{"c":25,"c++":28},"sm":{"c":60,"c++":55},"cn":"JNTU"}
print(d1,type(d1))
print("="*80)
print("values of key :")
for k in d1:

    print(k)
print("="*80)
print("values of value :")
for k,v in d1.items():
    print(v)


print("="*80)
print("values of key  and values of value :")
for k,v in d1.items():
    print(k, "===>",v)

print("="*80)

print("values of key and values of value and type of value and type of d1 object")


for k,v in d1.items():
    print(k,"==>",v,"==>",type(v),"==>",type(d1))

print("="*80)


v = d1.get("mm")
print(v)

v = d1.get("sm")
print(v)

# or variablename = object[key]

v = d1["mm"]
print(v)

v = d1["sm"]
print(v)

