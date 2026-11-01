d1 = {"sno":10,"sname":"guido","mm":{"c":20,"c++":30,"java":40},"sm":{"c":30,"c++":20,"java":30}}
print(d1,type(d1))
v = d1["mm"]
print(v,type(v))
sm = d1["sm"]
print(sm,type(sm))

print("="*80)
for i in d1.items():
    print(i,"==>",type(i),"==>",type(d1))

print("=*")
for v in d1.items():
    print(v)