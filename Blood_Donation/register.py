from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from DatabaseHelper import *


def create_user(en1,en2,en3,en5,en6,en7,en8):
    user = en5.get()
    name=en1.get()
    age=en2.get()
    phone_no=en3.get()
    weight=en7.get()
    pwd = en6.get()
    disease=en8.get()

    params = (name,age,phone_no,user, pwd,weight,disease)
    query = "Insert into blood_info(FULLNAME,AGE,PHONE,USERNAME,PWD,WEIGHT,DISEASE) Values(%s,%s,%s,%s,SHA(%s),%s,%s)"
    DatabaseHelper.execute_query(query, params)
    messagebox.showinfo('Success!', f'User with username {user} created successfully. Please login again.')

root = Tk()
root.title("Blood donor system")
root.geometry('1000x1000')

f = Frame(root, height=1000, width=1000, bg="pink")
f.pack(fill=X)

lbl0 = Label(root, text="Registration Form", font=("Calibri", 30, "bold", "italic"), bg="pink")
lbl0.place(x=550, y=30)

lbl1 = Label(root, text="Full Name :", font=("Times New Roman", 16), bg="pink")
lbl1.place(x=500, y=150, height=40, width=100)
en1 = Entry(root)
en1.place(x=620, y=150, height=32, width=250)

lbl2 = Label(root, text="Age :", font=("Times New Roman", 16), bg="pink")
lbl2.place(x=500, y=210, height=40, width=100)
en2 = Entry(root)
en2.place(x=620, y=210, height=32, width=250)

lbl3 = Label(root, text="Gender :", font=("Times New Roman", 16), bg="pink")
lbl3.place(x=500, y=270, height=40, width=100)
r1 = Radiobutton(root, text="Male", font=("Calibri", 16), bg="pink", variable=vars, value=1)
r1.place(x=620, y=275, height=29)
r2 = Radiobutton(root, text="Female", font=("Calibri", 16), bg="pink", variable=vars, value=2)
r2.place(x=730, y=275, height=29)
r3 = Radiobutton(root, text="Others", font=("Calibri", 16), bg="pink", variable=vars, value=3)
r3.place(x=860, y=275, height=29)

lbl4 = Label(root, text="Contact Number :", font=("Times New Roman", 16), bg="pink")
lbl4.place(x=440, y=330, height=40, width=150)
en3 = Entry(root)
en3.place(x=620, y=330, height=32, width=250)

# lbl5 = Label(root, text="Blood group:", font=("Times New Roman", 16), bg="pink")
# lbl5.place(x=460, y=390, height=40, width=140)
# en4 = Entry(root)
# en4.place(x=620, y=390, height=32, width=250)


lbl6 = Label(root, text="Username :", font=("Times New Roman", 16), bg="pink")
lbl6.place(x=500, y=450, height=40, width=100)
en5 = Entry(root)
en5.place(x=620, y=450, height=32, width=250)

lbl7 = Label(root, text="Password :", font=("Times New Roman", 16), bg="pink")
lbl7.place(x=500, y=510, height=40, width=100)
en6 = Entry(root, show="*")
en6.place(x=620, y=510, height=32, width=250)

lbl8 = Label(root, text="Weight(in kgs) :", font=("Times New Roman", 16), bg="pink")
lbl8.place(x=450, y=570, height=40, width=150)
en7 = Entry(root)
en7.place(x=620, y=570, height=32, width=250)

lbl9 = Label(root, text="Disease :", font=("Times New Roman", 16), bg="pink")
lbl9.place(x=470, y=630, height=40, width=150)
en8 = Entry(root)
en8.place(x=620, y=637, height=32, width=250)



b1 = Button(f, text="Sign up", font=("Times New Roman", 16), height=1, width=8,command=lambda: create_user(en1,en2,en3,en5,en6,en7,en8))
b1.place(x=660, y=700)

# b1 = Button(f, text="Back", font=("Times New Roman", 16), height=1, width=8)
# b1.place(x=430, y=640)

lb15 = Label(root, text="Blood Group:", font=("Times new Roman", 16), height=1, width=8, bg='pink')
lb15.place(x=460, y=390, height=40, width=150)

options = StringVar()
options.set("blood groups")
dropdown = OptionMenu(root, options, '(A+)', '(A-)', '(B+)', '(O+)', '(O-)', '(AB+)', '(AB-)').place_configure(
    width=250, x=620, y=400)



def show():
    print(options.get())


f.pack_propagate(0)
root.mainloop()