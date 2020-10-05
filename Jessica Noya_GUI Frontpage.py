import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, TOP


window = tk.Tk()
window.title("Fusion Gene GUI")
window.geometry('800x600')
window['bg'] = '#49A'

frames = [
    tk.PhotoImage(file="C:\\Users\\jessi\\Desktop\\Capstone\\Project Code\\DNAGif.gif", format='gif -index %i' % i)
    for i in range(50)]


def update(ind):
    frame = frames[ind]
    ind += 1

    if ind > 49:  # With this condition it will play gif infinitely
        ind = 0
    label.configure(image=frame)
    window.after(100, update, ind)


label = Label(window)
label.pack()
window.after(0, update, 0)


# Reference: https://www.geeksforgeeks.org/python-askopenfile-function-in-tkinter/
def open_file():
    file = askopenfile(mode='r', filetypes=[('Python Files', '*.BAM')])
    if file is not None:
        content = file.read()
        print(content)


btn = Button(window, text='Import BAM File', command=lambda: open_file())
btn.pack(side=TOP, pady=70)

window.mainloop()