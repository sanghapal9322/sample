d1 = {10:22,20:33,30:44}
print(d1,type(d1))
ks = d1.keys()
print(ks)
print(type(ks))

for k  in ks:
    print(k)

for k in ks:
    print(f"{k}==>{d1.get(k)}")

for k in ks:
    print(f"{k}===>{d1[k]}")

for k in d1.keys():
    print(k , "-->",d1.get(k))