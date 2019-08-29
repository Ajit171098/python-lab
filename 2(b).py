
def reverse(s):
    list1=s.split(" ")
    list1.reverse()
    st=" " 
    string=st.join(list1)
    print(string)
    print(string[::-1])


str1=input("enter string\n")
reverse(str1)


