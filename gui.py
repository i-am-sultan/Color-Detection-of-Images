from color_detection import *
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

window = Tk(className=' Colour Detection')
window.geometry('1280x720')
window.configure(bg='#162B32')

def file_opener():
   filepath = filedialog.askopenfilename()
   img_path.delete(0,'end')
   img_path.insert(0,filepath)
   initialize(filepath)

label_1 = Label(window, text = 'Image Path  : ')
label_1.place(x=450,y=290)

img_path = Entry(window,width=50)
img_path.place(x=550,y=290)

btn = Button(window, text ='Browse',command = lambda : file_opener())
btn.place(x=665,y=320)
btn.place(x=665,y=320)

window.mainloop()
