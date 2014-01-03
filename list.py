list=[]
n=raw_input("enter the no.of elements in ur list:")
i,ad=0,0
while (i<=int(n)):
 print "the %r element in the list"%i
 new=raw_input()
 list.append(new)
 ad = int(ad)+int(new)
 i=int(i)+1
print"Ur list:" 
print list
print"The sum of elements in u'r list is:"
print int(ad)

