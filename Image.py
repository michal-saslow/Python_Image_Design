import math
import random
from tkinter import Tk, filedialog
import cv2
import imageio
from gevent import os
from nltk.corpus import abc


class MyImage:

    def __init__(self, name_window, image_path):
        self.nameWindow = name_window
        self.image_path = image_path
        self.ix = -1
        self.iy = -1
        self.txt = ""
        self.action = None
        self.img = imageio.imread(image_path)
        width = int(self.img.shape[1] / 8)
        height = int(self.img.shape[0] / 8)
        resized_image = cv2.resize(self.img, (width, height))
        self.img = resized_image
        self.original_img = self.img
        self.show()

    def change_mouse(self):
        if self.action == 'cut':
            cv2.setMouseCallback(self.nameWindow, self.cut_image)
        elif self.action == 'add_text':
            cv2.setMouseCallback(self.nameWindow, self.add_text)
        elif self.action == 'add_triangle':
            cv2.setMouseCallback(self.nameWindow, self.add_triangle)
        elif self.action == 'add_rectangle':
            cv2.setMouseCallback(self.nameWindow, self.add_rectangle)
        elif self.action == 'add_circle':
            cv2.setMouseCallback(self.nameWindow, self.add_circle)
        else:
            cv2.setMouseCallback(self.nameWindow, lambda *args: None)

    def set_action(self, action):
        self.action = action
        self.change_mouse()

    def set_txt(self, txt):
        self.txt = txt

    def cut_image(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            x1, x2 = sorted([self.ix, x])
            y1, y2 = sorted([self.iy, y])
            cropped_image = self.img[y1:y2, x1:x2]
            self.img = cropped_image
            self.show()

    def black_white(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imshow(self.nameWindow, self.img)

    def reverse(self, flag):
        self.img = cv2.flip(self.img, flag)
        cv2.imshow(self.nameWindow, self.img)

    def get_old(self):
        self.img = self.original_img
        cv2.imshow(self.nameWindow, self.img)

    def add_frame(self):
        border_color = (0, 128, 255)
        self.img = cv2.copyMakeBorder(self.img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=border_color)
        cv2.imshow(self.nameWindow, self.img)

    def add_text(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.putText(self.img, self.txt, (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (200, 180, 255), 2)
            cv2.imshow(self.nameWindow, self.img)

    def add_triangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            new_x = random.randint(min(x, self.ix), max(x, self.ix)) + int(abs(self.ix - x) / 4)
            new_y = random.randint(min(y, self.iy), max(y, self.iy)) + int(abs(self.iy - y) / 4)
            cv2.line(self.img, (self.ix, self.iy), (x, y), (255, 255, 255), 2)
            cv2.line(self.img, (self.ix, self.iy), (new_x, new_y), (255, 255, 255), 2)
            cv2.line(self.img, (new_x, new_y), (x, y), (255, 255, 255), 2)
            cv2.imshow(self.nameWindow, self.img)

    def add_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.img, (self.ix, self.iy), (x, y), (170, 150, 0), 5)
            cv2.imshow(self.nameWindow, self.img)

    def add_circle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.ix = x
            self.iy = y
        elif event == cv2.EVENT_LBUTTONUP:
            radius = math.sqrt((x - self.ix) ** 2 + (y - self.iy) ** 2)
            cv2.circle(self.img, (self.ix, self.iy), int(radius / 2), (255, 0, 150), 2)
            cv2.imshow(self.nameWindow, self.img)

    def show(self):
        if self.img is not None and self.img.shape[0] > 0 and self.img.shape[1] > 0:
            cv2.imshow(self.nameWindow, self.img)
            self.change_mouse()
        else:
            print("Error: Image not loaded successfully.")
        # if self.img is not None and self.img.shape[0] > 0 and self.img.shape[1] > 0:
        # cv2.imshow("window", self.img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    #  else:
    #  print("Error: Image is not valid.")

    def save_image(self):

        root = Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])

        if file_path:
            if not file_path.lower().endswith('.jpg') and not file_path.lower().endswith('.jpeg'):
                file_path += '.jpg'

            try:
                imageio.imwrite(file_path, self.img)
                if os.path.isfile(file_path):
                    print("התמונה נשמרה בהצלחה במיקום שנבחר")

                else:
                    print("שגיאה: התמונה לא נשמרה במיקום שנבחר")
            except Exception as e:
                print(f"שגיאה בשמירת התמונה: {e}")
        else:
            print("לא נבחר מיקום לשמירת התמונה")
