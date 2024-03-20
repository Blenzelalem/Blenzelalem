num1=int(input("input number 1"))
num2=int(input("input number 2"))
print("choose from / or //")
op=input("input choice of division")

res=0
if op== '/':
     res=float(num1/num2)
elif op=='//':
     res=int(num1/num2)
else:
      print("character not specified")
print(num1,op,num2,"=", res)