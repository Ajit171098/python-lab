class CallDetail(object):
    def __init__(self):
        self.caller=None
        self.called=None
        self.duration=None
        self.type=None
        
class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        
        calldetails_obj=[]
        for i in range(3):
            calldetails_obj.append(CallDetail())
        for i in range(3):
            calldetails_obj[i]=list_of_call_string[i].split(",")
        self.list_of_call_objects=calldetails_obj

    def display(self):
        j=0
        for i in self.list_of_call_objects:
            print("CALL {} DETAILS:".format(j+1))
            print("Caller No:",i[0])
            print("Called No:",i[1])
            print("Duration :",i[2])
            print("Type of call:",i[3])
            print("\n")
            j=j+1
            

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
u=Util()
u.parse_customer(list_of_call_string)
u.display()
