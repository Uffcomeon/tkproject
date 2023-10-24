#TIMETABLE PROJECT-THIS SHIT SUCKS! PIKA-PIKA!--EVEN MY PIKACHU AGREES:)
from tkinter import *
from tkinter import ttk
root=Tk()
root.title('Automated timetable maker')
root.geometry('900x400')
root.minsize(900,400)
def s():
    window=Tk()
    window.title('subject selection')
    window.geometry('400x250')
    l1=Label(window,text='select your subject from the below drop down list')
    l1.place(x=20,y=5)
    i=StringVar()
    list1=['Maths','Physics','Chemistry','Biology','Computer science']
    sub=OptionMenu(window,i,*list1)
    i.set('select subject')
    sub.config(width=15)
    sub.place(x=50,y=50)
    
sub=ttk.Button(root,text='ADD SUBJECT',command=s)
sub.place(x=1,y=2)
teacher=ttk.Button(root,text='ADD TEACHER')
teacher.place(x=150,y=5)
profile=ttk.Button(root,text='INFO') #PLS CHANGE THE SHAPE TO THAT OF A CIRCLE
profile.place(x=800,y=2)
root.mainloop()
