from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import Image


class Window:
    def __init__(self):
        self.win = Tk()
        self.win.title("~ photo ~")
        self.img = None
        self.path = None
        self.effect = None
        self.txt_input = None
        self.shape = None
        self.txt = None
        self.win.geometry("860x400")
        self.title = Label(self.win, text="~ photo Designer ~", font=("Chiller", 40), width=20, fg="lightblue")
        self.chooseBtn = Button(self.win, text='choose image 📷', pady=10, width=20, font=("Chiller", 20),
                                bg="lightgray", activebackground="lightblue", command=self.open_img)
        self.cutBtn = Button(self.win, text="Cut 🛠", pady=10, bg="lightgray", width=20, font=("Chiller", 20),
                             activebackground="lightblue", command=self.cut)
        self.addTextBtn = Button(self.win, text="add text ✏", pady=10, width=20, font=("Chiller", 20), bg="lightgray",
                                 activebackground="lightblue", command=self.add_text_o)
        self.drawShapeBtn = Button(self.win, text="draw shape 🔴 🟥 🔺", width=20, font=("Chiller", 20), pady=10,
                                   bg="lightgray", activebackground="lightblue", command=self.add_shape)
        self.saveBtn = Button(self.win, text="save as 📥", pady=10, bg="lightgray", font=("Chiller", 20), width=20,
                              activebackground="lightblue", command=self.save)
        self.effects = Button(self.win, text="effects 🧮", pady=10, bg="lightgray", font=("Chiller", 20), width=20,
                              activebackground="lightblue", command=self.e)
        self.exitBtn = Button(self.win, text="Exit ❌", pady=1, bg="lightgray", font=("Chiller", 20),
                              activebackground="lightblue", command=self.quit)
        self.name = Label(self.win, text="made by michal saslow 😋 ", font=("Chiller", 20), width=20, fg="lightblue")

        self.positions()
        self.win.mainloop()

    def positions(self):
        self.title.grid(row=0, column=1)
        self.exitBtn.grid(row=0, column=2, padx=10, pady=10)
        self.chooseBtn.grid(row=1, column=0, padx=10, pady=10)
        self.addTextBtn.grid(row=1, column=2, padx=10, pady=10)
        self.cutBtn.grid(row=2, column=0)
        self.drawShapeBtn.grid(row=2, column=2)
        self.effects.grid(row=1, column=1, padx=10, pady=10)
        self.saveBtn.grid(row=2, column=1, padx=10, pady=10)
        self.name.grid(row=4, column=1, pady=30)

    def open_img(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.path = file_path
            self.img = Image.MyImage("image", file_path)

    def quit(self):
        self.win.quit()

    def cut(self):
        if self.img:
            self.img.set_action('cut')

    def add_text_o(self):
        if self.path:
            self.img.set_action("add_text")
            self.set_window_txt()

    def set_window_effects(self):
        self.effect = Toplevel()
        self.effect.title("Effects")
        self.effect.geometry("250x360")

        button_black_white = Button(self.effect, text="Black and white ⬜⬛", width=25,
                                    command=self.b_r,
                                    bg="lightblue",
                                    font=("Chiller", 15, "bold"))
        button_reverse_side = Button(self.effect, text=" revers-side 🔄", width=25,
                                     bg="lightblue",
                                     command=self.reverse_side,
                                     font=("Chiller", 15, "bold"))
        button_reverse_up = Button(self.effect, text="reverse-up 🔃️️", width=25,
                                   bg="lightblue",
                                   command=self.reverse_up,
                                   font=("Chiller", 15, "bold"))
        button_reverse_up_side = Button(self.effect, text="reverse_up_side 🔄🔃️", width=25,
                                        bg="lightblue",
                                        command=self.reverse_side_up,
                                        font=("Chiller", 15, "bold"))
        button_original = Button(self.effect, text="original 🔵", width=25, command=self.original, bg="lightblue",
                                 font=("Chiller", 15, "bold"))
        button_frame = Button(self.effect, text="frame 🔳", width=25, command=self.frame, bg="lightblue",
                              font=("Chiller", 15, "bold"))

        button_black_white.grid(row=0, column=1, padx=15, pady=10)
        button_frame.grid(row=1, column=1, padx=15, pady=10)
        button_reverse_side.grid(row=2, column=1, padx=15, pady=10)
        button_reverse_up.grid(row=3, column=1, padx=15, pady=10)
        button_reverse_up.grid(row=4, column=1, padx=15, pady=10)
        button_reverse_up_side.grid(row=5, column=1, padx=15, pady=10)
        button_original.grid(row=6, column=1, padx=15, pady=10)

    def set_window_txt(self):
        self.txt = Toplevel()
        self.txt.title("Add Text")
        self.txt.geometry("300x150")

        label = Label(self.txt, text="Add text", font=("Chiller", 30), width=20, fg="lightblue")
        label.grid(row=0, column=1)

        self.txt_input = Entry(self.txt, font=("Chiller", 10))
        self.txt_input.grid(row=1, column=1)

        button = Button(self.txt, text="Add", command=self.in_txt, fg="lightblue",
                        font=("Helvetica", 12, "bold"))
        button.grid(row=2, column=1, padx=10, pady=10)

        self.txt.mainloop()

    def set_window_shape(self):
        self.shape = Toplevel()
        self.shape.title("chose shape")
        self.shape.geometry("200x200")

        button_rectangle = Button(self.shape, text="rectangle 🟥", width=20, command=self.add_rectangle_o,
                                  bg="lightblue",
                                  font=("Chiller", 15, "bold"))
        button_circle = Button(self.shape, text="circle 🔴", width=20, command=self.add_circle_o, bg="lightblue",
                               font=("Chiller", 15, "bold"))
        button_triangle = Button(self.shape, text="triangle 🔺", width=20, command=self.add_triangle_o, bg="lightblue",
                                 font=("Chiller", 15, "bold"))

        button_rectangle.grid(row=0, column=1, padx=15, pady=10)
        button_triangle.grid(row=1, column=1, padx=15, pady=10)
        button_circle.grid(row=2, column=1, padx=15, pady=10)

    def in_txt(self):
        self.img.set_txt(self.txt_input.get())
        self.txt.destroy()

    def frame(self):
        self.img.add_frame()
        self.effect.destroy()

    def b_r(self):
        self.img.black_white()
        self.effect.destroy()

    def original(self):
        self.img.get_old()
        self.effect.destroy()

    def reverse_side(self):
        self.img.reverse(1)
        self.effect.destroy()

    def reverse_up(self):
        self.img.reverse(0)
        self.effect.destroy()

    def reverse_side_up(self):
        self.img.reverse(-1)
        self.effect.destroy()

    def e(self):
        if self.path:
            self.set_window_effects()

    def add_triangle_o(self):
        self.img.set_action("add_triangle")
        self.shape.destroy()

    def add_rectangle_o(self):
        self.img.set_action("add_rectangle")
        self.shape.destroy()

    def add_circle_o(self):
        self.img.set_action("add_circle")
        self.shape.destroy()

    def add_shape(self):
        if self.path:
            self.set_window_shape()

    def save(self):
        if self.path:
            self.img.save_image()
            self.quit()


w = Window()
