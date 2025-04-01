import sqlite3
import tkinter as tk
from tkinter import *

from string import *
from tkinter import messagebox, ttk

conn = sqlite3.Connection("example.db")

def contact():
        # root.destroy()
        r = Tk()
        r.geometry("1200x1200")

        global ee1, ee2, ee3, ee4, ee5, aa, bb, cc, dd, ee
        aa = StringVar()
        bb = StringVar()
        cc = StringVar()
        dd = StringVar()
        ee = StringVar()

        gg = Frame(r, height=768, width=670, bg="blue")
        gg.place(x=2, y=2)
        lbl1 = Label(r, text="Address", font=("helvetica", 20),
                     fg="white", bg="blue").place(x=100, y=200)
        lbl2 = Label(r, text="Lovely Professional University, Phagwara, Punjab", font=(
            "helvetica", 10), fg="white", bg="blue").place(x=100, y=250)
        lbl3 = Label(r, text="Lets Talk", font=("helvetica", 20),
                     fg="white", bg="blue").place(x=100, y=300)
        lbl4 = Label(r, text="+1800 123 8879", font=("helvetica", 10),
                     fg="green", bg="blue").place(x=100, y=350)
        lbl5 = Label(r, text="General Support", font=(
            "helvetica", 20), fg="white", bg="blue").place(x=100, y=400)
        lbl6 = Label(r, text="vstravels@gmail.com", font=("helvetica",
                     10), fg="green", bg="blue").place(x=100, y=450)
        hh = Frame(r, height=768, width=870, bg="white")
        hh.place(x=670, y=2)
        lab1 = Label(r, text="Send Us A Message", font=(
            "helvetica", 40), bg="white").place(x=770, y=50)
        lab2 = Label(r, text="TELL US YOUR NAME *",
                     font=("helvetica", 15), bg="white").place(x=770, y=170)

        ee1 = Entry(r, textvariable=aa).place(
            x=770, y=210, width=350, height=13)

        lab3 = Label(r, text="ENTER YOUR EMAIL *",
                     font=("helvetica", 15), bg="white").place(x=770, y=260)
        ee3 = Entry(r, textvariable=cc, width="20").place(
            x=770, y=300, width=350, height=13)
        lab4 = Label(r, text="ENTER PHONE NUMBER *",
                     font=("helvetica", 15), bg="white").place(x=770, y=350)
        ee4 = Entry(r, textvariable=dd).place(
            x=770, y=390, width=350, height=13)
        lab5 = Label(r, text="MESSAGE", font=("helvetica", 15),
                     bg="white").place(x=770, y=440)
        ee5 = Entry(r, textvariable=ee, font=("helvetica", 15)
                    ).place(x=770, y=480, width=600, height=80)

        def files():

            first_name = aa.get()

            email = cc.get()
            phone_no = dd.get()
            le = len(phone_no)
            message_ = ee.get()

            if (first_name == "" and email == "" and phone_no == "" and message_ == ""):
                messagebox.showinfo("Warning", "Please fill all entries")
            elif (first_name.isalpha() == False):
                messagebox.showinfo("warning", "Name cannot contain numbers")
            elif (le != 10 or phone_no.isalpha == False):
                messagebox.showinfo("Warning", "Invalid number")
            elif (phone_no.startswith("0") or phone_no.startswith("1") or phone_no.startswith("2") or phone_no.startswith("3") or phone_no.startswith("4") or phone_no.startswith("5")):
                messagebox.showerror("Warning ", "INVALID NUMBER")
            elif "@" not in email:
                messagebox.showinfo("Error", "Invalid Email")
            elif ".com" not in email:
                messagebox.showinfo("Error", "Invalid Email")
            else:
                f8 = open("Travel1.txt", "a")
                f8.write(first_name+" ")

                f8.write(email+"\n")
                f8.write(phone_no+"\n")
                f8.write(message_+"\n\n")
                f8.close()
                messagebox.showinfo("Congratulations",
                                    "Message Successfully received !")
                r.destroy()
                # home()

        bt = Button(r, text="SEND MESSAGE", font=("helvetica", 12),
                    bg="green", command=files).place(x=950, y=600)

        def homm():
            r.destroy()
            # home()

        Button(r, text="Home", command=homm, font=(
            "helvetica", 12), bg="green").place(x=1000, y=680)
        r.mainloop()