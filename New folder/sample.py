from   tkinter import *
root=Tk() 
def popup():
    states1=[check_var.get() for check_var in check_vars]
    print(states1)
    a=Label(root,text="".join(states1))
    a.pack()
check_vars=[]
list1=['malayalam','hindi','english']  
for i in list1:
    
    check_var = IntVar()
    check_vars.append(check_var)
    checkbutton = Checkbutton(root,text = i,variable=check_var)
    checkbutton.pack(pady=5)
print(check_vars)
submit=Button(root,text="submit",command=popup)   
submit.pack()


# radio button

radio_var = StringVar(value="Option 1")
radio_button1 = Radiobutton(root, text="Option 1", variable=radio_var,value="Option 1")
radio_button1.pack()
radio_button2 = Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio_button2.pack()


#menu


menu_bar =Menu(root)
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()