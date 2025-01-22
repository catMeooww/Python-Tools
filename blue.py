from tkinter import *
import random

infos = [
    "fucking you with this",
    "lolololol you lose this",
    "getting into your ass",
    "saying you are bad"
]

window = Tk()
window.attributes("-fullscreen", True)
window.title('HAHAHAHAHoHOHAHOHAHo')
blue = Frame(window,bg='#0098ff',width=1500,height=800)
blue.place(x=0,y=0)

sad = Label(blue,fg="white",bg="#0098ff",text=":(",font=("Arial",70))
sad.place(x=100,y=100)

infoLabels = []

infoLabels.append(Label(blue,fg="white",bg="#0098ff",text="Your PC ran into a problem and needs to restart. We're",font=("Arial",25)))
infoLabels.append(Label(blue,fg="white",bg="#0098ff",text=f"just {random.choice(infos)}, and then we'll restart for",font=("Arial",25)))
infoLabels.append(Label(blue,fg="white",bg="#0098ff",text="not you.",font=("Arial",25)))
infoLabels.append(Label(blue,fg="white",bg="#0098ff",text=r"-1000% complete",font=("Arial",20)))

for i,label in enumerate(infoLabels):
    label.place(x=100,y=250+i*50)

qr = Label(blue,fg="#0098ff",bg="white",text="#",font=("Arial",20),width=6,height=3)
qr.place(x=100,y=500)

miniInfo = Label(blue,fg="white",bg="#0098ff",text="For more information about this issue and possible fixes, visit https://catmeooww.github.io/CatMeooww")
miniInfo2 = Label(blue,fg="white",bg="#0098ff",text="Do not press WIN key.")
miniInfo.place(x=220,y=510)
miniInfo2.place(x=220,y=540)

window.mainloop()