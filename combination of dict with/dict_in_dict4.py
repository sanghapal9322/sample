d1 = {'sno': 10, 'name': 'RS', 'mm': {'c': 25, 'c++': 28, 'os': 22, 'python': 30, 'tm': 105}, 'sm': {'c': 60, 'c++': 55, 'os': 22, 'python': 30, 'tm': 167}, 'cn': 'JNTU'}
print(d1,type(d1))
delet_c = d1.get("sm").pop("c")
print(delet_c)

print(d1)
