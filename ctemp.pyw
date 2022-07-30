"""
Example showing for tkinter and ttk:
  -- ttk.Label
  -- ttk.Button
  -- ttk.Frame
  -- Associating a Button with a CALLBACK function

Authors: David Mutchler and his colleagues
         at Rose-Hulman Institute of Technology.
"""
import AIVirtualMouse as avm
# import tkinter
#from tkinter import Tk
# import random
# import os
# from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk
from VirtualPainter import main as paint
import subprocess
import packaging

root = Tk()
def vir():
   avm.main()
    #print('hellllllllll')
def main():
    # Root (main) window
    # root = tkinter.Tk()
    # root.title('AI')
    #
    # # Frame
    # frame1 = ttk.Frame(root)
    # frame1.grid()
    # logo = Image.open(os.path.join(r'S:\minor_sem_6\ai-virtual-mouse\handz.jpg'))
    # logo = ImageTk.PhotoImage(logo)
    # logo_label = ttk.label(image=logo)
    # logo_label.image = logo
    # logo_label.grid(column=1, row=0)
    #
    # # Label
    # label = ttk.Label(frame1, text='This is a Label above a Button')
    # label.grid()
    #
    # # Two buttons
    # change_title_button = ttk.Button(frame1,
    #                                  text='Virtual Mouse',command=avm.main)
    # change_title_button.grid()
    # #hange_title_button['command'] = lambda: aivm
    #
    # quit_button = ttk.Button(frame1, text='Quit')
    # quit_button.grid()
    # quit_button['command'] = lambda: close_window(root)
    #
    # # Another Label, with its text set another way
    # label2 = ttk.Label(frame1)
    # label2['text'] = 'Later, we will put Labels BESIDE Buttons'
    # label2.grid()
    #
    # root.mainloop()
    # Import module


    # Create object


    # Adjust size
    root.geometry("750x550")

    # label = Label(root)
    # img = Image.open(r"S:\minor_sem_6\ai-virtual-mouse\handz.jpg")
    # label.img = ImageTk.PhotoImage(img)
    # label['image'] = label.img
    #
    # label.pack()
    frame = Frame(root)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="news")
    grid = Frame(frame)
    grid.grid(sticky="news", column=0, row=7, columnspan=2)
    frame.rowconfigure(7, weight=1)
    frame.columnconfigure(0, weight=1)

    image = ImageTk.PhotoImage(Image.open(r"S:\minor_sem_6\ai-virtual-mouse\handz.jpg"))
    img_label = Label(image=image)
    img_label.grid(row=0, columnspan=2, pady=10,sticky="news")
    # label = Label(root, text="Welcome", font='system 18 bold')
    # label.grid(row=1, columnspan=2, pady=5)

    button = Button(root,text="Control Mouse", fg="green", font='TkDefaultFont 16 bold',
                       height="4",command = vir)
    button.grid(row=2, column=0, pady=20, padx=10,sticky="news")
    button3 = Button(root, text="Virtual Painter", fg="green", font='TkDefaultFont 16 bold',
                     height="4", command=paint)
    button3.grid(row=4, column=0, pady=20, padx=10,sticky="news")
    # button2 = Button(root,text="Exit", fg="green", font='TkDefaultFont 12 bold',
    #                    height="4",command = close_window)
    # button2.grid(row=2, column=4, pady=20, padx=10)

    label = Label(root, text="Made with ❤ and ☕ © 2022", font='arial 10')
    label.grid(row=6, columnspan=2, pady=5)
    root.mainloop()

    # # Create Frame
    # frame1 = Frame(root, bg="#88cffa")
    # frame1.pack(pady=20)
    #
    # # Add buttons
    # button1 = Button(frame1, text="Exit")
    # button1.pack(pady=20)
    # button1.grid(row=725, column=0, pady=20, padx=10)
    #
    # button2 = Button(frame1, text="Start")
    # button2.pack(pady=20)
    #
    # button3 = Button(frame1, text="Reset")
    # button3.pack(pady=20)

    # Execute tkinter
    root.mainloop()


#def aivm():
    #avm.main()


def vir_win():
    Window = Tk.Toplevel()
    canvas = Tk.Canvas(Window, height=750, width=500)
    canvas.pack()
def paint_win():
    pass

def change_title(root):
    # Make a new 8-letter title chosen randomly from 'A' to 'Z'.
    new_title = ''
    for k in range(8):  # @UnusedVariable
        new_title = new_title + chr(ord('A') + random.randrange(26))

    root.title(new_title)


def close_window(root=root):
    root.destroy()


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------

if __name__ == "__main__":
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    main()



