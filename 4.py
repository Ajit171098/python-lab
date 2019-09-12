class student():
    def __init__(self):
        self.id=0
        self.age=0
        self.marks=0
    def validate_marks(self):
        if self.marks>=0 and self.marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False
    def qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks>65:
                return True
            else:
                return False
        else:
            return False
    def setter(self):
        print("Enter marks:")
        self.marks=int(input())
        print("Enter age:")
        self.age=int(input())
        print("Enter id")
        self.id=int(input())
    def getter(self):
        if self.qualification():
            print("Age:{}".format(self.age))
            print("\nMarks:{}".format(self.marks))
            print("\nID:{}\n".format(self.id))
        else:
            print("NOT ELIGIBLE")

n=int(input("ENTER NO OF STUDENTS:"))
object_list=[]
for i in range(n):
    i=student()
    object_list.append(i)
for i in object_list:
    i.setter()
    
for i in object_list:
    i.getter()
    
