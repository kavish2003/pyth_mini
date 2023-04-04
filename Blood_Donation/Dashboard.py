import datetime
from tkinter import *
from DatabaseHelper import *
root=Tk()
root.title("Dashboard")
root.geometry("1500x1000")
root.configure(bg="pink")


# dash_title = Label( text = "Dashboard",width=20,height=1,font="Courier 30 bold",bg="pink").place(x = 500,y = 2)
lbl0 = Label(root, text="Dashboard",width=65,height=2 ,bg="brown",fg="white" , font=("Calibri", 35, "bold", "italic"),anchor=CENTER)
lbl0.place(x=0, y=0)
dash_name_label=Label( text = "Name",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 110)

dash_bld_grp_label=Label( text = "Blood Group",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 170)
dash_phn_no_label=Label( text = "Phone no.",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 230)
dash_gndr_label=Label( text = "Gender",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 290)
dash_wgt_label=Label( text = "Weight",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 350)
dash_age_label=Label( text = "Age",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 410)
dash_un_label=Label( text = "Username",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 470)
dash_dis_label=Label( text = "Disease",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 0,y = 530)

# DatabaseHelper.get_data()

dash_name_from_db=Label( text = "kavish",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 100)
dash_bld_grp_label_db=Label( text = "O+",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 160)
dash_phn_no_label_db=Label( text = "90222",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 220)
dash_gndr_label_db=Label( text = "Male",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 280)
dash_wgt_label_db=Label( text = "50",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 340)
dash_age_label_db=Label( text = "19",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 400)
dash_un_label_db=Label( text = "kavish",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 460)
dash_dis_label_db=Label( text = "Low haemoglobin",width=15,height=1,font="Courier 24 italic",bg="pink").place(x = 270,y = 520)


dash_prev_label=Label( text = "Last Blood Donated ",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 600,y = 230)
dash_session_exp=Label( text = "Days left",width=15,height=1,font="Poppins 24 bold",bg="pink").place(x = 900,y = 230)

btn = Button(root, text = 'Reregister',bg="orange",command = root.destroy).place(x=950,y=300)

eg_date= datetime.datetime.today().date()
today = datetime.datetime.today().date()
if eg_date + datetime.timedelta(days=2)>today:
    pass #date not expired
else:
    pass    #expired




root.iconbitmap("blood2.ico")
root.mainloop()
