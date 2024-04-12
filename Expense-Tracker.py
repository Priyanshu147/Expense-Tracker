import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import psycopg2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


conn = psycopg2.connect(
    database="Expense Tracker",
    user="use your sql server user name",
    host="localhost",
    password="use your sql server password",
    port=5432,
)

app = ctk.CTk()
ctk.set_default_color_theme("green")
app.geometry("3200x2000")
app._fg_color = "#F5F5F5"


def second_page(frame1,userid):
    def submit():
        get_amount=amount_entry.get()
        get_expensse_type=expense_type_combobox.get()
        get_date=date_entry.get()
        get_comments=comment_entry.get()
        show_data=get_amount+" "+get_expensse_type+ " "+get_date+ " "+get_comments
        txt_box.configure(state="normal")
        txt_box.insert(ctk.END,"\n \n" + show_data)
        txt_box.configure(state="disabled")
        cur = conn.cursor()
        cur.execute("insert into expense (userid,date,expense_type,amount,comment) values (%s, %s, %s,%s,%s)",
                (userid, get_date,get_expensse_type,float(get_amount),get_comments),)
    
        conn.commit()
      
    
    def data():
        # frame6.grid_remove()
        labels = ["Food & Dining", "Transportation", "Housing", "Entertainment","Other"]
        cur = conn.cursor()
        cur.execute("SELECT * FROM expense WHERE userid = %s", (userid,))
        rows = cur.fetchall()
        conn.commit()
        Food_Dining=0
        Transportation=0
        Housing=0	
        Entertainment=0
        Other=0
        Income=0
        total_expense=0
        for i in rows:
            
            if(i[2]=="Food & Dining"):
                Food_Dining+=i[3]
                total_expense+=i[3]
            elif(i[2]=="Transportation"):
                Transportation+=i[3]
                total_expense+=i[3]
            elif(i[2]=="Housing"):
                Housing+=i[3]
                total_expense+=i[3]
            elif(i[2]=="Other"):
                Other+=i[3]
                total_expense+=i[3]
            elif(i[2]=="Entertainment"):
                Entertainment+=i[3]
                total_expense+=i[3]
            elif(i[2]=="Income"):
                Income+=i[3]
    
        sizes = [Food_Dining,Transportation,Housing,Entertainment,Other]
        colors = ["gold", "yellowgreen", "lightcoral", "lightskyblue","Mediumorchid"]
        explode = (0, 0.1, 0, 0,0)  # explode 2nd slice

        # Plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct="%1.1f%%",
            shadow=True,
            startangle=140,
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        fig.patch.set_facecolor("#F5F5F5")

        plt.title("Pie Chart Example")

        # Embedding plot in Tkinter window
        canvas = FigureCanvasTkAgg(
            fig,
            master=frame6,
        )
        canvas.draw()
        canvas.get_tk_widget().place(x=10, y=10)

        categories = ["Food & Dining", "Transportation", "Housing", "Entertainment","Other","Income"]
        values = [Food_Dining,Transportation,Housing,Entertainment,Other,Income]

        # Plot
        fig, ax = plt.subplots(figsize=(8, 6))  # Larger figure size
        ax.bar(categories, values, color="skyblue")

        plt.title("Bar Plot Example")
        plt.xlabel("Categories")
        plt.ylabel("Values")

        # Set background color of the figure
        fig.patch.set_facecolor("#F5F5F5")

        # Embedding plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=frame6)
        canvas.draw()
        canvas.get_tk_widget().place(x=650, y=10)
        income_label = ctk.CTkLabel(
        master=frame7,
        text="Total Income",
        font=("Ubuntu", 30),
        text_color="#000000"
            )
        income_label.place(x=20, y=20)
        income_label = ctk.CTkLabel(
        master=frame7,
        text=Income,
        font=("Ubuntu", 30),
        text_color="#000000"
            )
        income_label.place(x=20, y=80)
        

        expense_label = ctk.CTkLabel(
        master=frame7,
        text="Total Expense",
        font=("Ubuntu", 30),
        text_color="#000000"
            )
        expense_label.place(x=280, y=20)
        expense_label = ctk.CTkLabel(
        master=frame7,
        text=total_expense,
        font=("Ubuntu", 30),
        text_color="#000000"
            )
        expense_label.place(x=280, y=80)
        
    frame1.destroy()
    frame3 = ctk.CTkFrame(app, width=3200, height=2000, fg_color="#F5F5F5")
    frame3.place(x=0, y=0)
    img1 = ImageTk.PhotoImage(Image.open("background.jpg").resize((3200, 2000)))
    img1_place = ctk.CTkLabel(master=frame3, image=img1, text="")
    img1_place.pack()
    frame4 = ctk.CTkFrame(
        frame3, width=570, height=800, fg_color="#F5F5F5", border_width=5
    )
    frame4.place(x=100, y=100)
    main_label = ctk.CTkLabel(
        master=frame4,
        text="Expense Tracker Information",
        font=("Ubuntu", 30),
        text_color="#000000",
    )
    main_label.place(x=20, y=20)
    txt_box=ctk.CTkTextbox(master=frame4,border_width=5,height=460,width=460,fg_color="#F5F5F5",font=("Ubuntu", 20),text_color="#000000")
    
    txt_box.place(x=20,y=70)
    txt_box.configure(state="disabled")
    amount = ctk.CTkLabel(
        master=frame4,
        text="Amount",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    amount.place(x=25, y=550)

    amount_entry = ctk.CTkEntry(
        master=frame4,
        width=220,
        placeholder_text="Amount",
    )
    amount_entry.place(x=20, y=585)
    expense_type = ctk.CTkLabel(
        master=frame4,
        text="expense type/Income",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    expense_type.place(x=330, y=550)

    expense_type_combobox = ctk.CTkComboBox(master=frame4,values=["Food & Dining", "Transportation","Housing","Entertainment","Other","Income"],)
    expense_type_combobox.pack()
    expense_type_combobox.place(x=330,y=585)
    date = ctk.CTkLabel(
        master=frame4,
        text="Date",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    date.place(x=25, y=635)

    date_entry = ctk.CTkEntry(
        master=frame4,
        width=220,
        placeholder_text="dd/mm/yyyy",

    )
    date_entry.insert(0,'05/04/2024')
    date_entry.place(x=20, y=665)
    comment = ctk.CTkLabel(
        master=frame4,
        text="Comments",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    comment.place(x=330, y=635)

    comment_entry = ctk.CTkEntry(
        master=frame4,
        width=220,
        placeholder_text="comments",
    )
    comment_entry.place(x=330, y=665)
    submit = ctk.CTkButton(
        master=frame4,
        width=220,
        text="Submit ",
        corner_radius=6,
        fg_color="#6600FF",
        command=submit
    )
    submit.pack()
    submit.place(x=180, y=730)
    

    frame5 = ctk.CTkFrame(
        frame3, width=800, height=800, fg_color="#F5F5F5", border_width=5
    )
    frame5.place(x=700, y=100)
    frame6 = ctk.CTkFrame(
        frame5, width=740, height=350, fg_color="#F5F5F5", border_width=5
    )
    frame6.place(x=30, y=30)
    data_btn = ctk.CTkButton(
        master=frame5,
        width=220,
        text="Data",
        corner_radius=6,
        fg_color="#6600FF",
        command=data,
    )
    data_btn.pack()
    data_btn.place(x=300, y=400)
    frame7 = ctk.CTkFrame(
        frame5, width=740, height=300, fg_color="#F5F5F5", border_width=5
    )
    frame7.place(x=30, y=450)
    data()



def signUp_page(frame1):
    frame1.destroy()
    def go_first_page():
        first_page()
    def submit():  # Check Login Info
        get_userid = userid_entry.get()
        get_name = name_entry.get()
        get_password = password_entry.get()

        cur = conn.cursor()
        cur.execute("SELECT userid FROM userinfo;")
        rows = cur.fetchall()
        conn.commit()
        check = True
        if get_userid == "" or get_password == "" or get_name == "":
            check = False
        for i in rows:
            if i[0] == get_userid:
                tk.messagebox.showerror("Sign Up", "User id is aleraady taken")
                check = False
                break
        if check == True:
            cur.execute(
                "insert into userinfo (userid,password,user_name) values (%s, %s, %s)",
                (get_userid, get_password, get_password),
            )
            conn.commit()
            second_page(frame1,get_userid)
        else:
            tk.messagebox.showerror("Sign Up info", "Invalid credentials")

    frame1 = ctk.CTkFrame(app, width=3200, height=2000, fg_color="#F5F5F5")
    frame1.pack()
    img1 = ImageTk.PhotoImage(Image.open("download.jpg").resize((3200, 2000)))
    img1_place = ctk.CTkLabel(master=frame1, image=img1, text="")
    img1_place.pack()

    img2 = ImageTk.PhotoImage(Image.open("side.png").resize((800, 1200)))
    img2_place = ctk.CTkLabel(master=frame1, image=img2, text="")
    img2_place.place(x=30, y=370)

    main_label = ctk.CTkLabel(
        master=frame1,
        text="Take control of your expenses, unlock financial freedom",
        font=("Comic Sans MS", 50),
        text_color="#000000",
    )
    main_label.place(relx=0.1, rely=0.1)

    frame2 = ctk.CTkFrame(
        frame1,
        width=320,
        height=450,
        corner_radius=20,
        fg_color="#F5F5F5",
        border_width=5,
    )

    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    l2 = ctk.CTkLabel(
        master=frame2, text="Sign Up", font=("Ubuntu", 30), text_color="#000000"
    )
    l2.place(x=120, y=40)
    username = ctk.CTkLabel(
        master=frame2,
        text="Username",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    username.place(x=55, y=85)
    userid_entry = ctk.CTkEntry(
        master=frame2, width=220, placeholder_text="Username", corner_radius=26
    )

    userid_entry.place(x=50, y=110)

    name = ctk.CTkLabel(
        master=frame2,
        text="Name",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    name.place(x=55, y=145)
    name_entry = ctk.CTkEntry(
        master=frame2, width=220, placeholder_text="Name", corner_radius=26
    )

    name_entry.place(x=50, y=180)
    password = ctk.CTkLabel(
        master=frame2,
        text="Password",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    password.place(x=50, y=215)

    password_entry = ctk.CTkEntry(
        master=frame2,
        width=220,
        placeholder_text="Password",
        show="*",
        corner_radius=26,
    )
    password_entry.place(x=50, y=250)
    button1 = ctk.CTkButton(
        master=frame2,
        width=220,
        text="Submit",
        corner_radius=6,
        fg_color="#6600FF",
        command=submit,
    )
    button1.pack()
    button1.place(x=50, y=295)

    button2 = ctk.CTkButton(
        master=frame2,
        width=220,
        text="Log In ",
        corner_radius=6,
        fg_color="#6600FF",
        command=go_first_page,
    )
    button2.pack()
    button2.place(x=50, y=340)


def first_page():
    
    def submit():  # Check Login Info
        get_userid = entry1.get()
        get_password = entry2.get()

        cur = conn.cursor()
        cur.execute("SELECT userid,password FROM userinfo;")
        rows = cur.fetchall()
        conn.commit()
        check = False
        if get_userid == "" or get_password == "" :
            check = False
        for i in rows:
            if i[0] == get_userid and i[1]==get_password:
                check = True
                break
        if check == True:
            second_page(frame1,get_userid)
        else:
            tk.messagebox.showerror("Login info", "Invalid credentials")

    def signUp_page_call():
        signUp_page(frame1)

    frame1 = ctk.CTkFrame(app, width=3200, height=2000, fg_color="#F5F5F5")
    frame1.pack()
    img1 = ImageTk.PhotoImage(Image.open("background.jpg").resize((3200, 2000)))
    img1_place = ctk.CTkLabel(master=frame1, image=img1, text="")
    img1_place.pack()

    img2 = ImageTk.PhotoImage(Image.open("side.png").resize((800, 1200)))
    img2_place = ctk.CTkLabel(master=frame1, image=img2, text="")
    img2_place.place(x=30, y=370)

    main_label = ctk.CTkLabel(
        master=frame1,
        text="Take control of your expenses, unlock financial freedom",
        font=("Comic Sans MS", 50),
        text_color="#000000",
    )
    main_label.place(relx=0.1, rely=0.1)

    frame2 = ctk.CTkFrame(
        frame1,
        width=320,
        height=350,
        corner_radius=20,
        fg_color="#F5F5F5",
        border_width=5,
    )

    frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    l2 = ctk.CTkLabel(
        master=frame2, text="Log in", font=("Ubuntu", 30), text_color="#000000"
    )
    l2.place(x=120, y=40)
    l3 = ctk.CTkLabel(
        master=frame2,
        text="UserId",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    l3.place(x=55, y=85)
    entry1 = ctk.CTkEntry(
        master=frame2, width=220, placeholder_text="Username", corner_radius=26
    )

    entry1.place(x=50, y=110)
    l4 = ctk.CTkLabel(
        master=frame2,
        text="Password",
        font=("Century Gothic", 15),
        text_color="#000000",
    )
    l4.place(x=55, y=140)

    entry2 = ctk.CTkEntry(
        master=frame2,
        width=220,
        placeholder_text="Password",
        show="*",
        corner_radius=26,
    )
    entry2.place(x=50, y=165)

    button1 = ctk.CTkButton(
        master=frame2,
        width=220,
        text="Login",
        corner_radius=6,
        fg_color="#6600FF",
        command=submit,
    )
    button1.pack()
    button1.place(x=50, y=240)

    button2 = ctk.CTkButton(
        master=frame2,
        width=220,
        text="New User ",
        corner_radius=6,
        fg_color="#6600FF",
        command=signUp_page_call,
    )
    button2.pack()
    button2.place(x=50, y=300)

first_page()

app.mainloop()
