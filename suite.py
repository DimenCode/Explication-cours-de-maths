n = input("n= ")
t = 0
n = int(n)

while(t < 20):
  if(n % 2 == 0):
    n = n/2
  else:
    n = n*3+1
  print("U"+str(t)+" = "+str(n))
  t = t+1
