from tkinter import *
import sqlite3 as db



mw=Tk()
mw.title("APS ASSIGNMENT SET-3")
#mw.geometry("680x480-8-200")
mw.config(bg="white")

conn=db.connect('Database.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS DATA
(
    date_inc TEXT,    
    date_cmc TEXT,
    fax_no TEXT,
    st_no TEXT,
    cg_no TEXT,
    d_re1 TEXT,
    d_r2 TEXT,
    ie TEXT,
    vat TEXT,
    d_r3 TEXT,
    d_r4 TEXT,
    buv TEXT,
    twn TEXT,
    dis TEXT,
    sta TEXT,
    pin TEXT,
    coun TEXT,
    p_ad TEXT,
    p_twn TEXT,
    p_dis TEXT,
    p_sta TEXT,
    p_pin TEXT,
    p_coun TEXT

)''')

c.close()
conn.commit()
conn.close()



def submit():
    print("Date of Incorporation", date_incvar.get())
    print("Date of Commencement of Bussiness", date_cmcvar.get())
    print("Fax NO.", fax_novar.get())
    print("Sales Tax Reg NO.", st_novar.get())
    print("CST/CGST Reg.NO", cg_novar.get())
    print("Date of Reg.",d_re1var.get())
    print("Date of Reg.",d_r2var.get())
    print("IE CODE", ievar.get())
    print("Vat Regn No.", vat_novar.get())
    print("Date of Registration", d_r3var.get())
    print("Date of Registration", d_r4var.get())
    print("Bussines Unit", buvar.get())
    print("CITY/TOWN", twnvar.get())
    print("District", disvar.get())
    print("State", stavar.get())
    print("PINCODE", pinvar.get())
    print("COUNTRY", counvar.get())
    
    print("Permanent Address", p_advar.get())
    print("CITY/TOWN", p_twnvar.get())
    print("District", p_disvar.get())
    print("State", p_stavar.get())
    print("PINCODE", p_pinvar.get())
    print("COUNTRY", p_counvar.get())

    conn=db.connect('Database.db')
    c=conn.cursor()
    c.execute("Insert into DATA values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
            %(date_incvar.get(), date_cmcvar.get(), fax_novar.get(), st_novar.get(), cg_novar.get(), d_re1var.get()
            , d_r2var.get(), ievar.get(), vat_novar.get(), d_r3var.get(), d_r4var.get(), buvar.get(), twnvar.get()
            , disvar.get(), stavar.get(), pinvar.get(), counvar.get(), p_advar.get(), p_twnvar.get(), p_disvar.get()
            , p_stavar.get(), p_pinvar.get(), p_counvar.get()))
    c.close()
    conn.commit()
    c.close()


cg_novar= StringVar()
d_re1var= StringVar()
d_r2var= StringVar()
date_incvar= StringVar()
date_cmcvar= StringVar()
fax_novar= StringVar()
st_novar= StringVar()
ievar= StringVar()
vat_novar= StringVar()
d_r3var= StringVar()
d_r4var= StringVar()
buvar= StringVar()
twnvar= StringVar()
disvar= StringVar()
stavar= StringVar()
pinvar= StringVar()
counvar= StringVar()
p_advar= StringVar()
p_twnvar= StringVar()
p_disvar= StringVar()
p_stavar= StringVar()
p_pinvar= StringVar()
p_counvar= StringVar()




































# lb=Label(mw, text="FOR OFFICE USE ONLY",font=('bold'), fg="red", bg="white").grid(row=0,column=0)
# lb1=Label(mw, text="DATE", bg="white").grid(row=1,column=0,sticky="w")
# en1=Entry(mw, textvariable=datevar).grid(row=1,column=1)

#idvar= StringVar()
# lb2=Label(mw, text="CUSTOMER ID", bg="white").grid(row=2,column=0,sticky="w")
# en2=Entry(mw,  textvariable=idvar).grid(row=2, column=1)

#icvar= StringVar()
# lb3=Label(mw,text="CUSTOMER IC", bg="white").grid(row=1,column=2)
# en3=Entry(mw, textvariable=icvar).grid(row=1, column=3)

#ac_novar= StringVar()
# lb4=Label(mw,text="ACCOUNT NO.", bg="white").grid(row=2,column=2)
# en4 = Entry(mw, textvariable=ac_novar).grid(row=2, column=3)

lb_n3=Label(mw,text="DATE OF INCORPORATION:", bg="white").grid(row=16,column=0)
lb_n4=Label(mw,text="DATE OF COMMENCEMENT OF BUSINESS:", bg="white").grid(row=16,column=1)
lb_n4=Label(mw,text="FAX NO.:", bg="white").grid(row=16,column=2)
enn2 = Entry(mw, textvariable=date_incvar).grid(row=17, column=0)
enn2 = Entry(mw, textvariable=date_cmcvar).grid(row=17, column=1)
enn3 = Entry(mw, textvariable=fax_novar).grid(row=17, column=2)

lb_n3=Label(mw,text="SALE TAX REGN NO.:", bg="white").grid(row=18,column=0)
lb_n4=Label(mw,text="CST/CGST REGN N0:", bg="white").grid(row=18,column=2)
enn2 = Entry(mw, textvariable=st_novar).grid(row=18, column=1)
enn3 = Entry(mw,textvariable=cg_novar).grid(row=18, column=3)

lb_n3=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=19,column=0)
lb_n4=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=19,column=2)
enn2 = Entry(mw, textvariable=d_re1var).grid(row=19, column=1)
enn3 = Entry(mw, textvariable=d_r2var).grid(row=19, column=3)

lb_n3=Label(mw,text="IE CODE:", bg="white").grid(row=20,column=0)
lb_n4=Label(mw,text="VAT REGN NO:", bg="white").grid(row=20,column=2)
enn2 = Entry(mw, textvariable=ievar).grid(row=20, column=1)
enn3 = Entry(mw, textvariable=vat_novar).grid(row=20, column=3)

lb_n3=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=21,column=0)
lb_n4=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=21,column=2)
enn2 = Entry(mw, textvariable=d_r3var).grid(row=21, column=1)
enn3 = Entry(mw, textvariable=d_r4var).grid(row=21, column=3)


lb_n3=Label(mw,text="MAILIG ADDRESS:",font=('bold'),fg="red", bg="white").grid(row=22,column=0)
lb_n3=Label(mw,text="BUSINESS UNIT:", bg="white").grid(row=22,column=1)
enn2 = Entry(mw, textvariable=buvar).grid(row=23, column=1)
lb_n3=Label(mw,text="CITY/TOWN", bg="white").grid(row=24,column=0)
lb_n3=Label(mw,text="DISTRICT", bg="white").grid(row=25,column=0)
lb_n3=Label(mw,text="STATE", bg="white").grid(row=26,column=0)
lb_n3=Label(mw,text="PINCODE", bg="white").grid(row=25,column=2)
lb_n3=Label(mw,text="COUNTRY", bg="white").grid(row=26,column=2)
enn3 = Entry(mw, textvariable=twnvar).grid(row=24, column=1)
enn3 = Entry(mw, textvariable=disvar).grid(row=25, column=1)
enn3 = Entry(mw, textvariable=stavar).grid(row=25, column=3)
enn3 = Entry(mw, textvariable=pinvar).grid(row=26, column=1)
enn3 = Entry(mw, textvariable=counvar).grid(row=26, column=3)


lb_n3=Label(mw,text="PERMANENT ADDRESS:",font=('bold'),fg="red", bg="white").grid(row=27,column=0)
lb_n3=Label(mw,text="(IF DIFFERENT FROM ABOVE)", bg="white").grid(row=27,column=1)
enn2 = Entry(mw, textvariable=p_advar).grid(row=28, column=0)
lb_n3=Label(mw,text="CITY/TOWN", bg="white").grid(row=29,column=0)
lb_n3=Label(mw,text="DISTRICT", bg="white").grid(row=30,column=0)
lb_n3=Label(mw,text="STATE", bg="white").grid(row=31,column=0)
lb_n3=Label(mw,text="PINCODE", bg="white").grid(row=30,column=2)
lb_n3=Label(mw,text="COUNTRY", bg="white").grid(row=31,column=2)
enn3 = Entry(mw, textvariable=p_twnvar).grid(row=29, column=1)
enn3 = Entry(mw, textvariable=p_disvar).grid(row=30, column=1)
enn3 = Entry(mw, textvariable=p_stavar).grid(row=30, column=3)
enn3 = Entry(mw, textvariable=p_pinvar).grid(row=31, column=1)
enn3 = Entry(mw, textvariable=p_counvar).grid(row=31, column=3)



b1=Button(mw, text="SUMMIT", padx=10, pady=5, bg="red",command= submit).grid(row=32, column=1)



mainloop()