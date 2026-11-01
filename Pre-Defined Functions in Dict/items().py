d1 = {"sno":100,"sname":"guido","course":"python"}
print(d1,type(d1))

print("="*80)
val = d1.items()
print(val)
print(type(val))

print("="*80)
for value in d1.items():
    print(value)

print("="*80)
for sk in d1.items():
    print(sk[0],"==",sk[1])

print("="*80)
for v in val:
    print(v[0],"==",v[1])