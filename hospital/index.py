from sqlite3 import IntegrityError
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import tkinter
 

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.Bloodpressure=StringVar()
        self.StorageAdvice=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()
       
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
  #===========================================================Dataframe======================================================================================  
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400) 


        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                                font=("times new roman",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)      
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                                font=("times new roman",12,"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350) 
   #=============================================================buttons frame================================================================================
                                              
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70) 

   #=============================================================details frame================================================================================
                                              
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        DetailsFrame.place(x=0,y=600,width=1530,height=190) 
   #==============================================================Dataframeleft=============================================================================
        lblNameTablet=Label(DataFrameLeft,text="Names Of Tablet",font=("ariel",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0) 

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman",12,"bold"),
                                                                                       width=35)  
        comNameTablet["values"]=("Nice","Corona Vaccine","Acetamenophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)


        lblref= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        
        txtref= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        
        lblDose= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets= Label(DataFrameLeft,font=("ariel",12,"bold"),text="No Of Tablets::",padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNooftablets.grid(row=3,column=1)  

        
        lblLot= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Lot::",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissuedate= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissuedate.grid(row=5,column=1)

        lblExpDate= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpdate= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpdate.grid(row=6,column=1)

        lblDailyDose= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Daily Dose",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        
        lblSideeffect= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lblSideeffect.grid(row=8,column=0,sticky=W)
        txtSideeffect= Entry(DataFrameLeft,font=("ariel",13,"bold"),textvariable=self.sideEffect,width=35)
        txtSideeffect.grid(row=8,column=1)


        
        lblFurtherinfo= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Further Information",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        
        lblBloodpressure= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblBloodpressure.grid(row=1,column=2,sticky=W)
        txtBloodpressure= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.Bloodpressure,width=35)
        txtBloodpressure.grid(row=1,column=3)

        
        lblStorage= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        
        lblMedicine= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        
        lblPatientId= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        
        lblNhsNumber= Label(DataFrameLeft,font=("ariel",12,"bold"),text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable= self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        
        lblPatientname= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        
        lblDateofbirth= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Date Of Birth",padx=2,pady=6)
        lblDateofbirth.grid(row=7,column=2,sticky=W)
        txtDateofbirth= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.DateofBirth,width=35)
        txtDateofbirth.grid(row=7,column=3)


        
        lblPatientAddress= Label(DataFrameLeft,font=("ariel",12,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress= Entry(DataFrameLeft,font=("ariel",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        # ========================DataframeRight========================
        self.txtPrescription=Text(DataFrameRight,font=("ariel",12,"bold"),width=46,height=16,padx=2,pady=6 )
        self.txtPrescription.grid(row=0,column=0)
        # =========================Buttons=====================================

        btnPrescription=Button(Buttonframe,command=self.iprescription,text="Prescription",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iexit,text="Exit",bg="green",fg="white",font=("ariel",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
        # =========================Table==============================
        # ============================Scrollbar===========================

        scroll_x=ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(DetailsFrame,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No. of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()
        # ==================Functionality Declaration=======================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
     
        else :
        
               conn=mysql.connector.connect(host="localhost",username="root",password="picasau@189",database="mydata")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                        self.Nameoftablets.get(),
                                                                                                        self.ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberofTablets.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.Issuedate.get(),
                                                                                                        self.ExpDate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.StorageAdvice.get(),
                                                                                                        self.nhsNumber.get(),
                                                                                                        self.PatientName.get(),
                                                                                                        self.DateofBirth.get(),
                                                                                                        self.PatientAddress.get()
                                                                                                    ))
               conn.commit()
               self.fatch_data()
               conn.close()
               messagebox.showinfo("success","Record has been inserted")
           
            
            
            
        

    def update(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="picasau@189",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Name_of_tablets=%s,dose=%s,No_of_tablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,pname=%s,dob=%s,address=%s  where Reference_No=%s",(
               
                                                                                                                                                                                                                         self.Nameoftablets.get(),
                                                                                                                                                                                                                         self.Dose.get(),
                                                                                                                                                                                                                         self.NumberofTablets.get(),
                                                                                                                                                                                                                         self.Lot.get(),
                                                                                                                                                                                                                         self.Issuedate.get(),
                                                                                                                                                                                                                         self.ExpDate.get(),
                                                                                                                                                                                                                         self.DailyDose.get(),
                                                                                                                                                                                                                         self.StorageAdvice.get(),
                                                                                                                                                                                                                         self.nhsNumber.get(),
                                                                                                                                                                                                                         self.PatientName.get(),
                                                                                                                                                                                                                         self.DateofBirth.get(),
                                                                                                                                                                                                                         self.PatientAddress.get(),
                                                                                                                                                                                                                         self.ref.get()
                                                                                                                                                                                                                    ))
        conn.commit()
        self.fatch_data()
        conn.close()
        
        
        messagebox.showinfo("Update","Updated successfully")

    def fatch_data(self) :
            conn=mysql.connector.connect(host="localhost",username="root",password="picasau@189",database="mydata")


 

    def fatch_data(self) :
            conn=mysql.connector.connect(host="localhost",username="root",password="picasau@189",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute ("select * from hospital")  
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()        
    def get_cursor(self,event=""):
            cursor_row=self.hospital_table.focus()
            content=self.hospital_table.item(cursor_row)
            row=content["values"]
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateofBirth.set(row[11])
            self.PatientAddress.set(row[12])
    def iprescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.Bloodpressure.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS number:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateofBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
    def idelete(self):
        if self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            
               Delete=messagebox.askyesno("Delete","Are you sure delete this entry")
               if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="picasau@189",database="mydata")
                    my_cursor=conn.cursor()
                    sql="delete from hospital where Reference_No=%s"
                    value=(self.ref.get(),)
                    my_cursor.execute(sql,value)
               else:
                    if not Delete:
                        return    
               conn.commit()
               self.fatch_data()
               conn.close()
               messagebox.showinfo("success","Data is deleted")
    
    
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.Bloodpressure.set("")
        self.StorageAdvice.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("") 
        self.txtPrescription.delete("1.0",END)  

    def iexit(self):
        iexit=messagebox.askyesno("Hospital Management System","Confirm you want to exit") 
        if iexit>0:
            root.destroy()
            return   
        
if __name__=="__main__":
     root=Tk()
     ob=Hospital(root)
     root.mainloop()