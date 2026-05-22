a = int(input('A:'))
b = int(input("B:"))
opertion = input('Add/sub/mul/div:')
if(opertion=="Add"):
 print(a+b)
elif(opertion=="sub"):
   print(a-b)
elif(opertion=='mul'):
  print(a*b)
elif(opertion=='div'):
  print(a/b)
else:
  print('invalid opertion')
