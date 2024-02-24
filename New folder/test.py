# from tkinter import *
# root=Tk()
# root.title("calculator")

# entry=Entry(root)
# entry.grid(columnspan=4)
# def func(symbol):
#     if symbol == "=":
#         try:
#             result = eval(entry.get())
#             entry.delete(0,END)
#             entry.insert(END, str(result))
#         except:
#             entry.delete(0, END)
#             entry.insert(END, "Error")
#     elif symbol == "C":
#         entry.delete(0, END)
#     else:
#         entry.insert(END, symbol)        
# numbers=["1","2","3","-","4","5","6","+","7","8","9","C","0","/","%","="]
# rowin=1
# colin=0
# for i in numbers:
    
#        button=Button(root,text=i,command=lambda symbol=i:func(symbol))
#        button.grid(row=rowin,column=colin)
#        colin+=1
#        if colin>3:
#              colin=0
#              rowin+=1
# root.mainloop()
