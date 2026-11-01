d1 = {
    "sno":10 ,
    "name":"sangha",
    "mid_marks":{"c":30,"c++":20,"java":25},
    "end_sem_marks":{"c":25,"c++":30,"java":29},
    "cname":"MSIT"
}

print(d1,type(d1))
for i,j in d1.items():
    print(i,"==>",j,"==>",type(j),"==>",type(d1))