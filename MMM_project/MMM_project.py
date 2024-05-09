from tkinter import *
from tkinter import messagebox
import math


def click_action():
    # if vmasa.get().isnumeric() == TRUE and vopor_powietrza.get().isnumeric() == TRUE and vkat_wystrzalu.get().isnumeric() == TRUE and vpredkosc_pocz.get().isnumeric() == TRUE :
    blad = FALSE
    try: m = float (vmasa.get())
    except ValueError: blad = TRUE
    try: k = float (vopor_powietrza.get())
    except ValueError: blad = TRUE
    try: a = float (vkat_wystrzalu.get())
    except ValueError: blad = TRUE
    try: rad = float ((k/180)*math.pi)
    except ValueError: blad = TRUE
    try: v = float (vpredkosc_pocz.get())
    except ValueError: blad = TRUE
    
    if blad == FALSE:
     
    


        """OBLICZENIA"""
        b = float (k/m)
        Vox = float (v*math.cos(rad))
        g = float (9.81)
        Voy = float (v*math.sin(rad))
        x_t = float (0)
        y_t = float (0)
        t = int (0)

        while y_t >= 0:
            """os_x = t
            os_y1 = x_t
            os_y2 = x_t"""
            x_t = (Vox/b)*(1 - math.exp(-b*t))
            y_t = (((Voy/b)+(g/b))*(1 - math.exp(-b*t))) - ((g*t)/b)
            print (t)
            print (y_t)
            print(x_t)
            t = t + 1

            
            
        print("KONIEC !!")


        print(m)
        print(k)
        print(a)
        print(rad)
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
        print("LOL!")




root = Tk()
root.title("MMM")
root.geometry("900x800")
text_label = Label(root, font=15, text="Wprowadź parametry")
masa = Label(root, font=40, text="Masa  [kg]")
opor_powietrza = Label(root, font=40, text="Opór powietrza [kg/s]")
kat_wystrzalu = Label(root, font=40, text="Kąt wystrzału [°]")
predkosc_pocz = Label(root, font=40, text="Prędkość początkowa [m/s]")
text_label.pack()

masa.place(x=0,y=50,height=50,width=150)
vmasa = Entry(root, width=10)
vmasa.insert(END, '0')
vmasa.place(x=10,y=100,height=25,width=130)

opor_powietrza.place(x=230,y=50,height=50,width=180)
vopor_powietrza = Entry(root,width=10) 
vopor_powietrza.insert(END, '0')
vopor_powietrza.place(x=240,y=100,height=25,width=130)

kat_wystrzalu.place(x=460,y=50,height=50,width=150)
vkat_wystrzalu = Entry(root,width=10)
vkat_wystrzalu.insert(END, '0')
vkat_wystrzalu.place(x=470,y=100,height=25,width=130)

predkosc_pocz.place(x=670,y=50,height=50,width=250)
vpredkosc_pocz = Entry(root,width=10)
vpredkosc_pocz.insert(END, '0')
vpredkosc_pocz.place(x=700,y=100,height=25,width=130)

Button(root, text="Zatwierdź", font=40, width=10, command=click_action).place(x=385,y=150,height=50,width=150)


root.mainloop()

