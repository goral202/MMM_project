from tkinter import *
from tkinter import messagebox

def click_action():
    if vmasa.get().isnumeric() == TRUE and vopor_powietrza.get().isnumeric() == TRUE and vkat_wystrzalu.get().isnumeric() == TRUE and vpredkosc_pocz.get().isnumeric() == TRUE :
        m = int (vmasa.get())
        b = int (vopor_powietrza.get())
        k = int (vkat_wystrzalu.get())
        v = int (vpredkosc_pocz.get())
        print(m)
        print(b)
        print(k)
        print(v)
        print("Wow!")
    else:
        vmasa.delete(0, END)
        vmasa.insert(END, '0')
        vopor_powietrza.delete(0, END)
        vopor_powietrza.insert(END, '0')
        vkat_wystrzalu.delete(0, END)
        vkat_wystrzalu.insert(END, '0')
        vpredkosc_pocz.delete(0, END)
        vpredkosc_pocz.insert(END, '0')
        messagebox.showerror('Informacja', 'Źle wprowadzone dane')
        print("LOLW!")




root = Tk()
root.title("MMM")
root.geometry("900x800")
text_label = Label(root, font=10, text="Wprowadź parametry")
masa = Label(root, font=40, text="Masa  [kg]")
opor_powietrza = Label(root, font=40, text="Opór powietrza")
kat_wystrzalu = Label(root, font=40, text="Kąt wystrzału [°]")
predkosc_pocz = Label(root, font=40, text="Prędkość początkowa [m/s]")
text_label.pack()

masa.place(x=0,y=50,height=50,width=150)
vmasa = Entry(root, width=10)
vmasa.insert(END, '0')
vmasa.place(x=10,y=100,height=25,width=130)

opor_powietrza.place(x=230,y=50,height=50,width=150)
vopor_powietrza = Entry(root,width=10) 
vopor_powietrza.insert(END, '0')
vopor_powietrza.place(x=240,y=100,height=25,width=130)

kat_wystrzalu.place(x=460,y=50,height=50,width=150)
vkat_wystrzalu = Entry(root,width=10)
vkat_wystrzalu.insert(END, '0')
vkat_wystrzalu.place(x=470,y=100,height=25,width=130)

predkosc_pocz.place(x=670,y=50,height=50,width=210)
vpredkosc_pocz = Entry(root,width=10)
vpredkosc_pocz.insert(END, '0')
vpredkosc_pocz.place(x=700,y=100,height=25,width=130)

Button(root, text="Zatwierdź", font=40, width=10, command=click_action).place(x=385,y=150,height=50,width=150)


root.mainloop()