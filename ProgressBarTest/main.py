from tkinter    import *
from tkinter.ttk import *
import time

def download():
    size = 100
    downloaded = 0
    speed = 2
    while (downloaded < size):
        time.sleep(0.05)
        downloaded+=speed
        bar["value"] += speed
        percent.set(str(int((downloaded/size)* 100))+" %" )
        done.set(str(downloaded)+" out of "+str(size)+"  downloaded")
        window.update_idletasks()

window=Tk()


percent=StringVar()
done=StringVar()

Label(text="Dowload progress").pack()
window.geometry("600x100")
bar=Progressbar(window,length=500,orient=HORIZONTAL)

bar.pack()
Button(text="Download",command=download).pack()
Label(text="percent completed",textvariable=percent).pack()
Label(text="Tasks completed",textvariable=done).pack()
window.mainloop()

