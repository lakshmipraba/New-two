def search(sorted_list,n):
 i=0
 while(i<=int(new)):
  if(sorted_list[i]==n):
   print "ur element in the %r position of the list"%i   
   exit(0) 
  else:
   exit
  i=i+1 
 print "-1"
sorted_list=[]
i=0
new=raw_input("enter the no.of elements in ur list:")
while(i<=int(new)):
 print "the %r element in the list"%i
 a=raw_input()
 sorted_list.append(a)
 i=int(i)+1
print sorted_list
n=raw_input("enter the element u want to search:")
search(sorted_list,n)
