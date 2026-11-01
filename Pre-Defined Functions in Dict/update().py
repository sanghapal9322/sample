# update()
d1 = {10:100,20:200,30:300}
d2 = {1:1000,2:2000,3:3000}
print(d1,type(d1),id(d1))
print(d2,type(d2),id(d2))
d1.update(d2)
d2.update(d1)
print(d1,type(d1),id(d1))
print(d2,type(d2),id(d2))