import sqlite3
conn=sqlite3.connect("student_prg.db")


def create_table(conn):
    conn.execute("create table student(name char(20),usn varchar(20) primary key,mobile_no integer,branch char(20))")
    conn.commit()
    print("table created")
def insert_data(conn):
    name=input("enter name")
    usn=input("enter usn")
    mobile=int(input("enter mobile no"))
    branch=input("enter branch")
    conn.execute("insert into student values(?,?,?,?)",(name,usn,mobile,branch))
    conn.commit()

def delete_tb(conn):
    conn.execute("drop table student")
    conn.commit()
def delete(conn):
    n=input("enter the usn of the student to be deleted")
    conn.execute("delete from student where usn=?",(n,))
    conn.commit()

def update(conn):
    print("what u want to update")
    print("1.NAME")
    print("2.MOBILE NO")
    print("3.BRANCH")
    n=int(input())
    if n==1:
        old_name=input("enter old name")
        new_name=input("enter new name")
        conn.execute("update student set name=? where name=?",(new_name,old_name))
        conn.commit()
    elif n==2 :
        old_no=input("enter old no")
        new_no=input("enter new no")
        conn.execute("update student set mobile_no=? where mobile_no=?",(new_no,old_no))
        conn.commit()
    elif n==3:
        old_branch=input("enter old branch")
        new_branch=input("enter new branch")
        conn.execute("update student set branch=? where branch=?",(new_no,old_no))
        conn.commit()
        
def display_all(conn):
    rows=conn.execute("select * from student")
    for row in rows:
        print(row)

def display_specific(conn):
    usn1=input("enter usn")
    rows=conn.execute("select * from student where usn=(?)",(usn1,))
    for row in rows:
        print(row)

while 1:
      print("0.EXIT")
      print("1.CREATE TABLE")
      print("2.INSERT DATA")
      print("3.DELETE STUDENT")
      print("4.DELETE TABLE") 
      print("5.UPDATE STUDENT")
      print("6.DISPLAY ALL")
      print("7.DISPLAY STUDENT")
      m=int(input())

      if m==1:
          create_table(conn)
      elif m==2:
          insert_data(conn)
      elif m==3:
          delete(conn)
      elif m==4:
          delete_tb(conn)
      elif m==5:
          update(conn)
      elif m==6:
          display_all(conn)
      elif m==7:
          display_specific(conn)
      elif m==0:
          break
conn.close()
