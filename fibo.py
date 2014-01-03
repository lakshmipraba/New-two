def fib(n):
 a,b,c,new=0,1,1,0
 if(int(n)<=1):
  print n
 else:
  while(c<=int(n)):  
   new=a+b
   b=a
   a=new
   c=c+1
  print new  
print"the value of n:"
n=raw_input()
fib(n)
