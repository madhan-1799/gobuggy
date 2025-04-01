import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import webbrowser
import sv_ttk

from about_page import *
from cancel_page import *
from contact_page import *
from feedback_page import *
from services_page import *
from show_booking import *
from payment_page import *
from contact_page import *

conn = sqlite3.Connection("example.db")

conn.execute('''CREATE TABLE IF NOT EXISTS TEST3(
             ORIGIN TEXT NOT NULL,
             DEST TEXT NOT NULL,
             NAME TEXT NOT NULL,
             DAY TEXT,
             MONTH TEXT,
             YEAR TEXT,
             GENDER TEXT,
             TIMING TEXT,
             MOBILE TEXT NOT NULL,
             PAIDTHROUGH TEXT NOT NULL,
             AMOUNTPAID TEXT NOT NULL);''')

conn.execute('''CREATE TABLE IF NOT EXISTS FEEDBACKT(
             NAME TEXT NOT NULL,
             GENDER TEXT,
             MOBILE TEXT NOT NULL,
             BOOKINGEXPERIENCE TEXT NOT NULL,
             CUSTOMERSERVICE TEXT NOT NULL,
             CALLSERVICE  TEXT NOT NULL,
             PAYMENTEXPERIENCE TEXT NOT NULL);''')


def home():
    conn = sqlite3.Connection("example.db")
    root = Tk()
    sv_ttk.set_theme("dark")
    root.geometry('1200x1200')
    root.title("Book-A-Bus")

    swidth = root.winfo_screenwidth()
    sheight = root.winfo_screenheight()

    bon = Label(root, text="Book-A-Bus", font=("Arial Rounded MT Bold", 40, "bold"), bd=0).place(x=400, y=10)
    label_me = tk.Label(root, bg='black').place(x=0, y=80, width=swidth, height=70)

    about_button = tk.Button(root, text="About", bd=0, fg='white', font=("Helvetica", 15), bg='#1c1c1c', activebackground='#4a4a4a', command=about)
    about_button.place(x=10, y=100, width=150, height=40)

    services_button = tk.Button(root, text="Services", bd=0, fg='white', font=("Helvetica", 15), bg='#1c1c1c', activebackground='#4a4a4a', command=service)
    services_button.place(x=150, y=100, width=150, height=40)

    feedback_button = tk.Button(root, text="Feedback", bd=0, fg='white', font=("Helvetica", 15), bg='#1c1c1c', activebackground='#4a4a4a', command=feed)
    feedback_button.place(x=290, y=100, width=150, height=40)

    show_booking = tk.Button(root, text="Show Bookings", bd=0, fg='white', font=("Helvetica", 15), bg='#1c1c1c', activebackground='#4a4a4a', command=showbok)
    show_booking.place(x=440, y=100, width=150, height=40)

    cancel_button = tk.Button(root, text="Cancel", bd=0, fg='white', font=("Helvetica", 15), bg='#1c1c1c', activebackground='#4a4a4a', command=cancel)
    cancel_button.place(x=590, y=100, width=150, height=40)

    book_frame = tk.Frame(root, bg="grey", width="1100", height="700").place(x=50, y=200)
    book_head_label = tk.Message(root, text="Book Your Tickets", width="500", bd=0, bg="grey", font=("Helvetica", 30)).place(x=420, y=220)

    from_input = StringVar()
    to_input = StringVar()
    name_input = StringVar()
    gender_input = StringVar()
    mobile_input = StringVar()
    year_input = StringVar()
    month_input = StringVar()
    day_input = StringVar()
    time_input = StringVar()

    label_from = tk.Label(root, text="From", font=("Helvetica", 15), bg='grey').place(x=110, y=350)
    e1 = ttk.Combobox(root, textvariable=from_input, values=['Block-14', 'AB-5', 'AB-3', 'KMC', 'Student Plaza', 'MIT-Gate-1'])
    e1.place(x=110, y=400, height="40", width="450")

    label_to = tk.Label(root, text="To", font=("Helvetica", 15), bg='grey').place(x=110, y=450)
    e2 = ttk.Combobox(root, values=['Block-14', 'AB-5', 'AB-3', 'KMC', 'Student Plaza', 'MIT-Gate-1'], textvariable=to_input)
    e2.place(x=110, y=500, height="40", width="450")

    year = list(range(2022, 2030))
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    day = list(range(1, 31))

    label_dat = tk.Label(root, text="Year", font=("Helvetica", 10)).place(x=110, y=580, width=60, height=40)
    e3 = ttk.Combobox(root, values=year, textvariable=year_input).place(x=180, y=580, width=60, height=40)

    label_dat = tk.Label(root, text="Month", font=("Helvetica", 10)).place(x=280, y=580, width=60, height=40)
    e4 = ttk.Combobox(root, values=month, textvariable=month_input).place(x=340, y=580, width=60, height=40)

    label_dat = tk.Label(root, text="Day", font=("Helvetica", 10)).place(x=440, y=580, width=60, height=40)
    e5 = ttk.Combobox(root, values=day, textvariable=day_input).place(x=500, y=580, width=60, height=40)

    label_nameof = tk.Label(root, text="Name of the passenger:", font=("Helvetica", 15), bg='grey').place(x=700, y=350)
    e_name = tk.Entry(root, textvariable=name_input).place(x=700, y=400, width=420, height=40)

    label_gender = tk.Label(root, text='Gender', bg='grey', font=("Helvetica", 15)).place(x=700, y=450)
    e_gender = ttk.Combobox(root, textvariable=gender_input, values=['Male', 'Female', 'Others']).place(x=700, y=500, height=40, width=420)

    label_mob = tk.Label(root, text="Mobile Number : ", font=("Helvetica", 15), bg='grey').place(x=700, y=550)
    e_mob = tk.Entry(root, textvariable=mobile_input).place(x=700, y=600, width=420, height=40)

    label_timing = tk.Label(root, text="Choose the Time", bg="grey", font=("Helvetica", 15)).place(x=110, y=650)
    timing_a = ttk.Combobox(root, values=['12:00 am', '6:00 am', '9:00 am', '12:00 pm', '3:00 pm', '6:00 pm', '9:00 pm'], textvariable=time_input)
    timing_a.place(x=110, y=700, height=40, width=450)

    def pay():
        sv_ttk.set_theme("dark")
        a = from_input.get()
        b = to_input.get()
        c = name_input.get()
        d = gender_input.get()
        e = mobile_input.get()
        le = len(e)
        f = year_input.get()
        g = month_input.get()
        h = day_input.get()
        i = time_input.get()
        if a == '' or b == '' or c == '' or d == '' or e == '' or f == '' or g == '' or h == '' or i == '':
            messagebox.showinfo("Warning!", "Please Enter the required Fields !")
            home()
        elif a == b:
            messagebox.showinfo("Destination and Arrival cannot be the same!")
            home()
        elif le > 10 or le < 10:
            messagebox.showinfo("Warning", "Invalid Number")
        else:
            # Pricing logic
            price = 1000  # You can adjust the price logic as needed

            # Payment page layout
            roop = tk.Tk()
            roop.title("Payment")
            roop.geometry('800x600')
            roop.configure(bg="#222324")
            Label(roop, text="Payment Gateway", font=("Helvetica", 30, "bold"), bg="#222324", fg="white").pack(pady=20)

            # Payment method
            def paywith():
                p = "CASH"
                dat = (a, b, c, h, g, f, d, i, e, p, price)
                conn.execute('''INSERT INTO TEST3('ORIGIN','DEST','NAME','DAY','MONTH','YEAR','GENDER','TIMING','MOBILE','PAIDTHROUGH','AMOUNTPAID') VALUES(?,?,?,?,?,?,?,?,?,?,?)''', dat)
                conn.commit()
                roop.destroy()
                messagebox.showinfo("Booking Confirmed", "Your Booking has been Confirmed.")
                home()

            # Payment methods
            ttk.Button(roop, text="Pay with Cash", command=paywith).pack(pady=10)
            ttk.Button(roop, text="Pay with Credit Card", command=paywith).pack(pady=10)
            ttk.Button(roop, text="Pay with UPI", command=paywith).pack(pady=10)

    ttk.Button(root, text="Proceed", command=pay).place(x=500, y=750, height="50", width="200")
    root.mainloop()


home()
