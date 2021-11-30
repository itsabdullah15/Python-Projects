from tkinter import *
from tkinter import ttk     #combo box
from googletrans import Translator,LANGUAGES

def change(text='type',src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)   

root = Tk()     #Object name
root.title("Abdullah Translator")
root.geometry("500x700")
root.config(bg='Red')

#Translator Heading label
lab_txt = Label(root,text="Translator",font=("Time New Roman",20,"bold"),bg="white")   #Label
lab_txt.place(x=100, y=40, height=50, width=300)         #Translator label size

frame = Frame(root).pack(side=BOTTOM)

#Source Text Heading label
lab_txt = Label(root,text="Source Text",font=("Time New Roman",15,"bold"),fg="Black",bg="yellow")   #Label
lab_txt.place(x=100, y=100, height=30, width=300)

#Source Text writing label code
Sor_txt = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=150,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=50,y=320,height=40,width=65)
comb_sor.set("Hindi")

button_change = Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=200,y=320,height=40,width=65)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=350,y=320,height=40,width=65)
comb_dest.set("English")

#Dest Label Heading
lab_txt = Label(root,text="Dest Text",font=("Time New Roman",15,"bold"),fg="Black",bg="yellow")  
lab_txt.place(x=100, y=430, height=30, width=300)

#Dest Labal Text
dest_txt= Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD) 
dest_txt.place(x=10,y=470,height=130,width=480)









root.mainloop()        #for showing box