import mysql.connector
class Operation:
    def __init__(self,h,u,p,d):
        self.h=h
        self.u=u
        self.p=p
        self.d=d

    def AddRegister(self,fn,em,un,pn,pan,add,adh,pas):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("insert into register(fname,email,uname,pno,pan,address,adhar,pas) values('"+fn+"','"+em+"','"+un+"','"+pn+"','"+pan+"','"+add+"','"+adh+"','"+pas+"')")
        con.commit()
        return "Record Added Successfully.."

    def Checklogin(self,u,p):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("select * from register where uname='"+u+"' and pas='"+p+"'")
        data=mycursor.fetchall()
        return data
    
    def forgotpassword(self,u,p):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("update register set pas='"+p+"' where uname='"+u+"'")
        con.commit()
        con.close()
        return "Updated Successfully..."
    


    def GetBalance(self,rid):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("select *  from accdetail  where rid="+str(rid))
        data=mycursor.fetchall()
        return data

    def Addmoney(self,rid,b):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("update accdetail set balance='"+b+"'where rid="+str(rid))
        con.commit()
        con.close()
        return "Amount Added Successfully"
    

    def SendMoney(self,acc,b):
        con=mysql.connector.connect(host=self.h,user=self.u,password=self.p,database=self.d)
        mycursor=con.cursor()
        mycursor.execute("update accdetail set balance=balance +'"+b+"' where AccNo="+str(acc))
        con.commit()
        con.close()
        return "Amount Added Successfully"




        




