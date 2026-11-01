# values()
d1 = {"Telangana":"Hydrabad","Maharashtra":"Mumubai","Tamilnadu":"Chennai","karnataka":"banglore"}
print(d1,type(d1))
value = d1.values()
print(value)
print(type(value))

print("="*80)
for i in value:
    print(i)