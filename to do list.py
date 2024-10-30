import tkinter
from tkinter import *
from tkinter import messagebox
import pickle
from pickle import *

root=tkinter.Tk()
root.title("To-Do list")

def add_task():
    task=entry.get()
    if task!="":
        listbox.insert(tkinter.END,task)
        entry.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!",message="You must enter a task")
def delete_task():
    try:
        task_index=listbox.curselection()[0]
        listbox.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="You must select a task")
def load_task():
    try:
        tasks=pickle.load(open("Task.dat","rb"))
        listbox.delete(0,tkinter.END)
        for task in tasks:
            listbox.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="File task.dat is not found")
def save_task():
    tasks=listbox.get()(0,listbox.size())
    pickle.dump(tasks,open("Tasks.dat","wb"))

frame=tkinter.Frame(root)
frame.pack()
scrollbar=tkinter.Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox=tkinter.Listbox(frame,height=20,width=50)
listbox.pack(side=tkinter.RIGHT)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


entry=tkinter.Entry(root,width=50)
entry.pack()
add_button=tkinter.Button(root,text="Add task",width=40,command=add_task)
add_button.pack()
delete_button=tkinter.Button(root,text="Delete task",width=40,command=delete_task)
delete_button.pack()
load_button=tkinter.Button(root,text="Load task",width=40,command=load_task)
load_button.pack()
save_button=tkinter.Button(root,text="Save task",width=40,command=save_task)
save_button.pack()


root.mainloop()
