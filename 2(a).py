def search1(list1,k):
    if k in list1:
        return (1)
    else:
       return (0)
n=int(input("Enter the no of elements in the list\n"))
list2=[]
print("Enter elements")
for i in range(0,n):
    a=int(input())
    list2.append(a)
no=int(input("Enter the no to be searched\n"))
result=search1(list2,no)
print(result)
    
    
    
   
