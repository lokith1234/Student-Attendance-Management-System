import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox

connection = sqlite3.connect("school.db")
crsr = connection.cursor()
t_data=()

def main():
    crsr.execute("CREATE TABLE IF NOT EXISTS teach_table (Username NOT NULL UNIQUE, Password NOT NULL, Class NOT NULL)")
    crsr.execute("CREATE TABLE IF NOT EXISTS stud_table (ROLLNO TEXT PRIMARY KEY,StudentName TEXT NOT NULL,GRADE TEXT NOT NULL,SECTION TEXT NOT NULL)")
    crsr.execute("CREATE TABLE IF NOT EXISTS stud2_table (RNO TEXT NOT NULL,Day DATE NOT NULL,Attendance CHAR NOT NULL)")
    connection.commit()
    global window,uname,passw,uname_entry,pass_entry
    window=Tk()
    window.geometry('1350x730')
    window.title("Student Attendance Management System")

    label = Label(window,height=700,width=700)
    label.place(x=1350,y=0)
    uname_entry =StringVar()
    pass_entry=StringVar()
    uname=''
    passw=''

    uname_label=Label(window,text="Username",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    uname_label.place(x=640,y=270)
    uname_entry=Entry(window,width=20,font=("bold",17),textvariable=uname,bg='#808080')
    uname_entry.place(x=570,y=295)

    pass_label=Label(window,text="Password",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    pass_label.place(x=640,y=340)
    pass_entry=Entry(window,width=20,font=("bold",17),textvariable=passw,bg='#808080',show='*')
    pass_entry.place(x=570,y=365)

    login_button= Button(window,text='LOG IN',font=("bold",17),width=15,bg='#7FFFD4',fg='green',command=verify)                        
    login_button.place(x=585,y=425)

    create_button=Button(window,text="Create User",font=("bold",17),fg='blue',bg='#7FFFD4',command=create)
    create_button.place(x=615,y=500)

    char='DESKTOP APPLICATION STUDENT ATTENDANCE MANAGEMENT SYSTEM'
    title_label=Label(window,text=char,font=("Lato",35,"bold"),fg='red',bg='#3D426B')
    title_label.place(x=60,y=50)

def verify():
    global uname,passw,user
    uname=uname_entry.get()
    passw=pass_entry.get()
    d2=crsr.execute('''SELECT Username,Password FROM teach_table''')

    if (uname,passw) in d2:
        window.destroy()
        attendance()
        
    else:
        inv=messagebox.showinfo('Error!',"Invalid credentials")
        invuname=Entry(window,width=20,font=("bold",17),bg='pink')
        invuname.place(x=570,y=295)
        invpass_entry=Entry(window,width=20,font=("bold",17),bg='pink')
        invpass_entry.place(x=570,y=365)
        retry_button= Button(window,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close1)                        
        retry_button.place(x=585,y=425) 

def attendance(): 
    global window3,stu,tdata,entr,dat,rno,sect
    window.destroy
    window3=Tk()
    window3.geometry('1350x730')
    window3.title("Students Attendance Details")
    window3.configure(bg='#7FFFD4')
    window3.resizable(False,False)
    
    canvas=Canvas(window3, width=1350, height=730,bg='#7FFFD4')
    canvas.pack()
    canvas.create_line(675,150,675,450, fill="black", width=2)
    data=crsr.execute('''SELECT * FROM teach_table''') 
    for i in data:
        if i[0]==uname:
            tdata=i
    sect=tdata[2].split('-')

    stu=StringVar()
    dat=StringVar()
    entr=StringVar()
    rno=StringVar()

    label2=Label(window3,height=3,width=1350,bg='#007ba7')
    label2.place(x=0,y=10)
    home=Button(window3,text='⌂ HOME',font=('Lato',20),fg='black',bg='blue',command=close2)
    home.place(x=60,y=17)

    welcome="Welcome, "+uname+" to attendance details of class "+tdata[2]
    wel_label=Label(window3,height=3,width=1350,bg='green')
    wel_label.place(x=0,y=55)
    wel=Label(window3,text=welcome,font=("bold",25),fg='black',bg='green')
    wel.place(x=0,y=55)

    head1_label=Label(window3,text="To Mark Absence for a Specific Date",font=("bold",20),fg='#3D426B',bg='#7FFFD4')
    head1_label.place(x=210,y=130)
    head2_label=Label(window3,text="To Add a New Student",font=("bold",20),fg='#3D426B',bg='#7FFFD4')
    head2_label.place(x=865,y=130)

    date_label=Label(window3,text="Enter Date (dd/mm/yyyy)",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    date_label.place(x=275,y=180)
    date_entry=Entry(window3,width=20,font=("bold",17),textvariable=dat,bg='#808080',fg='white')
    date_entry.place(x=255,y=210)
    
    Rollno_label=Label(window3,text="Enter Student Roll Number (Eg:5G11, 5A34)",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    Rollno_label.place(x=810,y=180)
    rollno_entry=Entry(window3,width=20,font=("bold",17),textvariable=rno,bg='#808080',fg='white')
    rollno_entry.place(x=855,y=210)
    
    enter_label=Label(window3,text="Enter Absentee(s) Roll Number \n (If multiple separate by a comma without spaces)",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    enter_label.place(x=170,y=275)
    ent=Entry(window3,width=20,font=("bold",17),textvariable=entr,bg='#808080',fg='white')
    ent.place(x=255,y=320)
    ent_button=Button(window3,text="Enter",font=("Lato",17),fg='green',bg='#808080',command=abs)
    ent_button.place(x=280,y=365)
    
    non_button=Button(window3,text="None",font=("Lato",17),fg='green',bg='#808080',command=AllP)
    non_button.place(x=380,y=365)

    add_label=Label(window3,text="Enter Student Name",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
    add_label.place(x=900,y=290)
    s_add=Entry(window3,width=20,font=("bold",17),textvariable=stu,bg='#808080')
    s_add.place(x=855,y=320)
    add_button=Button(window3,text="Add",font=("Lato",17),fg='green',bg='#808080',command=add)
    add_button.place(x=930,y=365)

    att_button=Button(window3,text="This Month's Attendance",font=('bold',17),fg='blue',bg='#7FFFD4',command=avgatt)
    att_button.place(x=570,y=490)

def add():
    global rno
    stud=stu.get()
    roll=rno.get()
    s_data=(roll,stud,sect[0],sect[1])
    try:
        i='INSERT INTO stud_table VALUES (?,?,?,?)'
        crsr.execute(i,s_data)
        correct=messagebox.showinfo("Success!","Student Added")
        connection.commit()

    except sqlite3.IntegrityError:
        inv=messagebox.showinfo("Error!","Invalid details")
        invstud=Entry(window3,width=20,font=("bold",17),bg='pink')
        invstud.place(x=855,y=320)
        retry3_button= Button(window3,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close4)                        
        retry3_button.place(x=585,y=425)
    
def abs():
    global enter,date
    date=str(dat.get())
    enter=tuple(str(entr.get()).split(','))
    ph=','.join('?'*len(enter))

    AllP()
    connection.commit()
    try:
        if date!='' and set(enter).issubset(rolls):
            q=f"UPDATE stud2_table SET Attendance='A' WHERE RNO in ({ph}) AND Day="
            q+="'"+date+"'"
            crsr.execute(q,enter)
            connection.commit()
            right=messagebox.showinfo("Success!","Absence Recorded")
        else:
            raise NameError
        
    except:    
        inv=messagebox.showinfo("Error!","Invalid Details")
        inventr=Entry(window3,width=20,font=("bold",17),bg='pink')
        inventr.place(x=255,y=320)
        retry4_button= Button(window3,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close4)                        
        retry4_button.place(x=590,y=425)
    connection.commit()

def AllP():
    global date, rolls
    date=dat.get()
    if date in [i for i in crsr.execute('select Day from stud2_table where RNO like "?%"',''.join(sect))]:
        inv=messagebox.showinfo("Error!","Absence Already Marked for Date!")
        inventr=Entry(window3,width=20,font=("bold",17),bg='pink')
        inventr.place(x=255,y=320)
        retry4_button= Button(window3,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close4)                        
        retry4_button.place(x=590,y=425)
    else:
        rolls=crsr.execute('''SELECT ROLLNO from stud_table WHERE Grade=? AND Section=?''',sect)
        l=[]
        for i in rolls:
            l.append(i[0])
        
        for i in l:

            q='INSERT INTO stud2_table VALUES(?,?,?)'
            s=(i,date,'P')
            crsr.execute(q,s)
            connection.commit()
        
def avgatt():
    try:
        window3.destroy()
        avgatt()
    except:
        global window4
        window4=Tk()
        window4.geometry('1350x730')
        window4.title("Monthly Attendance Details")
        window4.configure(bg='#7FFFD4')
        window4.resizable(False,False)
        global mont
        global ast

        ast=StringVar()
        mont=StringVar()

        label2=Label(window4,height=3,width=1350,bg='#007ba7')
        label2.place(x=0,y=10)
        home=Button(window4,text='⌂ HOME',font=('Lato',20),fg='black',bg='blue',command=close5)
        home.place(x=60,y=17)

        mon_label=Label(window4,text="Enter Month (mm) Eg: For February - 02; For June - 06\n(Required for both)",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
        mon_label.place(x=470,y=90)
        mon_entry=Entry(window4,width=20,font=("bold",17),textvariable=mont,bg='#808080',fg='white')
        mon_entry.place(x=570,y=140)

        per_label=Label(window4,text="Daily Class Attendance Percentage for the Month",font=("Lato",20),fg='#3D426B',bg='#7FFFD4')
        per_label.place(x=170,y=220)

        avgcla_button=Button(window4,text="Average Class Attendance",font=("Lato",17),fg='green',bg='#808080',command=classavg)
        avgcla_button.place(x=270,y=287)

        astu_label=Label(window4,text="Indivdual Student Attendance",font=("bold",20),fg='#3D426B',bg='#7FFFD4')
        astu_label.place(x=830,y=220)
        astu1_label=Label(window4,text="Enter Student Roll Number",font=("Lato",17),fg='#3D426B',bg='#7FFFD4')
        astu1_label.place(x=865,y=255)
        astu_entry=Entry(window4,width=20,font=("bold",17),textvariable=ast,bg='#808080')
        astu_entry.place(x=850,y=287)

        stuper_button=Button(window4,text="Average Student Attendance",font=("Lato",17),fg='green',bg='#808080',command=perstu)
        stuper_button.place(x=837,y=325)

def perstu():
    month=mont.get()
    astu=ast.get()

    if month=='' or astu=='':
        inv()
    else:
        tot=0
        c=0
        a=crsr.execute('''SELECT * FROM stud2_table where RNO=?''',(astu,))
        for i in a:
            if i[0].startswith(''.join(sect)) and i[1][3:5]==month:
                tot+=1
                if i[2]=='P' and i[0]==astu:
                    c+=1

        if tot!=0:
            cper=str(round((c/tot)*100,2))
            t="The student's average attendance for the month is: "+cper+'%'
            cper_label=Label(window4,font=("bold",17),fg='#3D426B',bg='#7FFFD4',width=1350,height=700)
            cper_label.place(x=0,y=360)
            cper_label=Label(window4,text=t,font=("bold",23),fg='#3D426B',bg='#7FFFD4')
            cper_label.place(x=450,y=360)

            canvas = Canvas(window4, bg='#7FFFD4', width=750, height=300)
            canvas.place(x=300, y=400)

            scrollbar = Scrollbar(window4, orient="vertical", command=canvas.yview)
            scrollbar.place(x=1037, y=404, height=300)

            student_frame = Frame(canvas, bg='#7FFFD4',highlightbackground='blue')
            canvas.create_window((0, 0), window=student_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
            Label(student_frame, text="Roll No", font=("bold", 24), bg='#7FFFD4',fg='#3D426B').grid(row=0, column=0, padx=10, pady=0)
            Label(student_frame, text="Date", font=("bold", 24), bg='#7FFFD4',fg='#3D426B').grid(row=0, column=1, padx=219, pady=0)
            Label(student_frame, text="Attendance", font=("bold", 24), bg='#7FFFD4',fg='#3D426B').grid(row=0, column=2, padx=10, pady=0)

            a=1
            for i in crsr.execute('select * from stud2_table where RNO=?',(astu,)):
                if i[1][3:5]==month:
                    Label(student_frame, text=i[0], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=0, padx=10, pady=5)
                    Label(student_frame, text=i[1], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=1, padx=10, pady=5)
                    Label(student_frame, text=i[2], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=2, padx=10, pady=5)
                    a+=1

            student_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        else:
            inv()

def classavg():
    month=mont.get()
    if month=='':
        inv()
    else:
        tot=0
        c=0
        month=mont.get()
        a=crsr.execute('''SELECT * FROM stud2_table''')
        for i in a:
            if i[0].startswith(''.join(sect)) and i[1][3:5]==month:
                tot+=1
                if i[2]=='P':
                    c+=1

        if tot!=0:
            sper=str(round((c/tot)*100,2))
            t="The class's average attendance for the month is: "+sper+'%'
            sper_label=Label(window4,font=("bold",17),fg='#3D426B',bg='#7FFFD4',width=1350,height=700)
            sper_label.place(x=0,y=360)
            sper_label=Label(window4,text=t,font=("bold",23),fg='#3D426B',bg='#7FFFD4')
            sper_label.place(x=450,y=360)

            canvas = Canvas(window4, bg='#7FFFD4', width=750, height=300)
            canvas.place(x=300, y=400)

            scrollbar = Scrollbar(window4, orient="vertical", command=canvas.yview)
            scrollbar.place(x=1037, y=404, height=300)

            student_frame = Frame(canvas, bg='#7FFFD4',highlightbackground='blue')
            canvas.create_window((0, 0), window=student_frame, anchor="nw")

            canvas.configure(yscrollcommand=scrollbar.set)
            Label(student_frame, text="Roll No", font=("bold", 24), fg='#3D426B',bg='#7FFFD4').grid(row=0, column=0, padx=10, pady=0)
            Label(student_frame, text="Date", font=("bold", 24), fg='#3D426B',bg='#7FFFD4').grid(row=0, column=1, padx=219, pady=0)
            Label(student_frame, text="Attendance", font=("bold", 24),fg='#3D426B', bg='#7FFFD4').grid(row=0, column=2, padx=10, pady=0)

            a=1
            for i in crsr.execute('select * from stud2_table'):
                if i[1][3:5]==month and i[0].startswith(''.join(sect)):
                    Label(student_frame, text=i[0], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=0, padx=10, pady=5)
                    Label(student_frame, text=i[1], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=1, padx=10, pady=5)
                    Label(student_frame, text=i[2], bg='#7FFFD4',fg='black',font=('bold',18)).grid(row=a, column=2, padx=10, pady=5)
                    a+=1

            student_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        else:
            inv()

def inv():
    invmon=Entry(window4,width=20,font=("bold",17),bg='pink')
    invmon.place(x=570,y=140)
    invastu=Entry(window4,width=20,font=("bold",17),bg='pink')
    invastu.place(x=850,y=287)
    inv=messagebox.showinfo("Error!","Invalid details")
    retry3_button= Button(window4,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close6)                        
    retry3_button.place(x=585,y=287)

def create():
    try:
        window.destroy()
        create()
    except:
        global u,p,s,window2 
        s=''
        u=''
        p=''
        window2=Tk()
        window2.configure(bg="#7FFFD4")
        window2.geometry('1350x730')
        window2.title("New User")
        window2.resizable(False,False)
        u=StringVar()
        p=StringVar()
        
        label2=Label(window2,height=3,width=1350,bg='#007ba7')
        label2.place(x=0,y=10)
        home=Button(window2,text='⌂ HOME',font=('Lato',20),fg='#3D426B',bg='blue',command=close)
        home.place(x=60,y=17)

        u_label=Label(window2,text="New Username",font=("bold",17),fg='#3D426B',bg='#7FFFD4',)
        u_label.place(x=625,y=250)
        p_label=Label(window2,text="New Password",font=("bold",17),fg='#3D426B',bg='#7FFFD4')
        p_label.place(x=625,y=320)
        sec_label=Label(window2,text="Enter class and section (Eg:12-G or 3-B)",font=('bold',17),fg='#3D426B',bg='#7FFFD4')
        sec_label.place(x=555,y=395)

        u=Entry(window2,width=20,font=("bold",17),textvariable=u,bg='#808080',fg='white')
        u.place(x=570,y=275)
        p=Entry(window2,width=20,font=("bold",17),textvariable=p,bg='#808080',fg="white",show='*')
        p.place(x=570,y=345)
        s=Entry(window2,width=20,font=("bold",17),textvariable=s,bg='#808080',fg='white')
        s.place(x=570,y=420)
        save=Button(window2,text="Save Information",font=("Lato",17),fg='green',bg='#808080',command=teacher)
        save.place(x=600,y=480)

def teacher():
    global user,pin
    user = str(u.get())
    pin = str(p.get())
    sec=str(s.get())
    t_data=(user,pin,sec)

    if user!='' and pin!='' and sec!='':
        try:
            crsr.execute('''INSERT INTO teach_table VALUES (?,?,?)''',t_data)
            window2.destroy()
            main()
            connection.commit()
        except:
            inv=messagebox.showinfo("Error!","Invalid Details")
            invu=Entry(window2,width=20,font=("bold",17),textvariable=u,bg='pink',fg='white')
            invu.place(x=570,y=275)
            invp=Entry(window2,width=20,font=("bold",17),bg='#808080')
            invp.place(x=570,y=345)
            invs=Entry(window2,width=20,font=("bold",17),textvariable=s,bg='pink',fg='white')
            invs.place(x=570,y=420)
            retry_button= Button(window2,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close3)                        
            retry_button.place(x=590,y=480)
    else:
        inv=messagebox.showinfo("Error!","Invalid Details")
        invu=Entry(window2,width=20,font=("bold",17),textvariable=u,bg='pink',fg='white')
        invu.place(x=570,y=275)
        invp=Entry(window2,width=20,font=("bold",17),bg='pink')
        invp.place(x=570,y=345)
        invs=Entry(window2,width=20,font=("bold",17),textvariable=s,bg='pink',fg='white')
        invs.place(x=570,y=420)
        retry_button= Button(window2,text='RETRY',font=("bold",17),width=15,bg='black',fg='green',command=close3)                        
        retry_button.place(x=590,y=480)

def close():
    window2.destroy()
    main()

def close1():
    window.destroy()
    main()

def close2():
    window3.destroy()
    main()

def close3():
    window2.destroy()
    create()

def close4():
    window3.destroy()
    attendance()

def close5():
    window4.destroy()
    main()

def close6():
    window4.destroy()
    avgatt()
main()
window.mainloop()