
class validate:
    def __init__(self):
        self.str1=None
 
    def check_string(self):
         l=[]
         for i in self.str1:
            if i in ('{','(','['):
               l.append(i)
            elif i=='}':
               a=l.pop()
               if a!='{':
                  return False
            elif i==')':
               a=l.pop()
               if a!='(':
                  return False
            elif i==']':
               a=l.pop()
               if a!='[':
                  return False
         if len(l)==0:
             return True
         else:
             return False

    def setter(self):
           self.str1=input("Enter string:")
v=validate()
v.setter()
n=v.check_string()
if n==False:
    print("string is invalid")
else:
    print("string is valid")



           
    
        
    
