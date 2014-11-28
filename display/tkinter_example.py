import time

from simplecv.api import Image
import ImageTk  # This has to be installed from the system repos
import Tkinter

Tkinter.Tk()

image = Image('http://i.imgur.com/FTKqh.jpg')  # load the simplecv logo from the web
photo = ImageTk.PhotoImage(image.get_pil())
label = Tkinter.Label(image=photo)
label.image = photo  # keep a reference!
label.pack()  # show the image
time.sleep(5)
