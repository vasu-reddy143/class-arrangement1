'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def class_arrangement(vv):
 N = len(vv)
 o1 = 0
 z1 = 0
 for i in range(N):
  if (vv[i] == 'B'):
   o1 += 1
  else:
   z1+= 1
 if (o1 > z1 + 1 or z1 > o1 + 1):
  return -1
 if (N % 2):
  number = (N + 1) // 2
  evenone = 0
  evenzero = 0
  for i in range(N):
   if (i % 2 == 0):
    if (vv[i] == 'B'):
     evenone+=1
    else:
     evenzero+=1
  if (o1 > z1):
   return number-evenzero
  else:
   return number-evenzero
 else:
  oddone = 0
  evenone = 0
  for i in range(N):
   if (vv[i] == 'B'):
    if (i % 2):
     oddone+=1
    else:
     evenone+=1
  return min(N // 2 - oddone, N // 2 - evenone)
vv = input()
print(class_arrangement(vv),end="")
