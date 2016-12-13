names={}
names[1]=5
names[2]=10
names[3]=15
names[4]=20
names[5]=25

key=input("key:")

if key in names.keys():
  print "yes"
  print names[key]
else:
  print "no"
