dict1={}
dict2={}
dict3={}

dict1[1]=10
dict1[2]=20
dict2[3]=30
dict2[4]=40
dict3[5]=50
dict3[6]=60

print dict1
print dict2
print dict3

dict1.update(dict2)
dict1.update(dict3)

print dict1
