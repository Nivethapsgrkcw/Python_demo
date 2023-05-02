tuple=()
num=int(input("enter the no.of values to be stored in the tuple: "))
for i in range(1,num+1):
    val=int(input('enter the values'))
    tuple+=(val,)
print(tuple)
result=int("".join(str(ele)for ele in tuple),2)
print("The decimal value=",result)
