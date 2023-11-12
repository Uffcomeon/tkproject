
from tkinter import *
from tkinter import ttk


# welcome window
def splash_screen():
    splash_root = Tk()
    #splash_root.configure(bg='cyan')
    width = (
        splash_root.winfo_screenwidth()
    )  # to make the welcome window the size of the user's screen
    height = splash_root.winfo_screenheight()
    splash_root.geometry(f"{width}x{height}")
    splash_label = Label(
        splash_root, text="WELCOME", font=("newspaper", 50)
    )  # text on the welcome screen
    splash_label.place(relx = 0.5, 
                   rely = 0.5,
                   anchor = 'center')
    

    return splash_root


# Subject Selection Screen
def s():
       window_sub=Tk()
       window_sub.geometry('300x300')
       l1=Label(window_sub,text='Type down the subject you wish to add',font=('arial',10))
       l1.place(x=20,y=20)
       l2=Label(window_sub,text='Enter duration',font=('arial',10))
       l2.place(x=20,y=80)
       sub=StringVar()
       duration=StringVar()
       entry1=Entry(window_sub,textvar=sub)
       entry1.place(x=40,y=50)
       entry2=Entry(window_sub,textvar=duration)
       entry2.place(x=40,y=100)
       def p():
            Sub=sub.get()
       def dur():
           Dur=dur.get()

            
       def quit():
            exit()
    
       subbutton=Button(window_sub,text='Add',fg='white',bg='red',command=p)
       subbutton.place(x=40,y=200)
       subbutton2=Button(window_sub,text='Quit',fg='white',bg='red',command=quit)
       subbutton2.place(x=80,y=200)
       window_sub.mainloop()



# Teacher Selection Screen
def t():
    window2 = Tk()
    window2.title("Add Teachers")
    window2.geometry("400x250")
    l2 = Label(window2, text="Name:")
    l2.pack()
    l2.place(x=20, y=5)
    e = Entry(window2, width=50)
    e.pack
    e.place(x=80, y=5)
    submit = ttk.Button(window2, text="SUBMIT")
    submit.place(x=120, y=80)


# Prepare the root window
# Define the root window

#main window
def root_window():
    root = Tk()
    root.title("Automated timetable maker")
    width = root.winfo_screenwidth()  # to make window the size of the user's screen
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")
    root.minsize(900, 400)
    sub = ttk.Button(root, text="ADD SUBJECT", command=s)
    sub.place(x=1, y=2)
    teacher = ttk.Button(root, text="ADD TEACHER", command=t)
    teacher.place(x=150, y=5)
    

    #window for the information window
    def info_window():
        iw = Tk()
        iw.title("How to operate")
        iw.geometry("500x500")
        iw_label = Label(
        iw, text="information to be added")
        iw_label.place(relx = 0.5, 
                   rely = 0.5,
                   anchor = 'center')

    # information icon
    prof_button = PhotoImage(file=r"C:\Users\ITS\Desktop\i_btn.png", height=30)
    prof_label = (
        Button(
            root,
            text="info",
            image=prof_button,
            # Change this function to the thing you want to show for information
            command=info_window
        )
        .pack(side=TOP)
        .place(x=500, y=100)
    )

    return root
 
    
        


def run_mainloop():  
    splash_root.destroy()
    root = root_window()
    root.mainloop()
    SECOND = 1000 


SECOND = 1000 
splash_root = splash_screen()
splash_root.after( 1 * SECOND, run_mainloop)
    
