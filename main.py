import tkinter
import os

main_window = tkinter.Tk()

def cam():
    print("Openning Webcam..")
    os.system("Webcam.py")
    print("Exitting...")

def add():
    print("Openning Webcam..")
    os.system("Record.py")
    print("Exitting...")

def train():
    print("Tranning..")
    os.system("Train.py")
    print("Exitting...")

def main():
    print("Openning Webcam..")
    os.system("Recognizer.py")
    print("Exitting...")

label1 = tkinter.Label(main_window, text="Face Recognizer")
label2 = tkinter.Label(main_window, text="----------------")
button1 = tkinter.Button(main_window, text="Open Camera",command=cam)
button2 = tkinter.Button(main_window, text="Add Face",command=add)
button3 = tkinter.Button(main_window, text="Training Data",command=train)
button4 = tkinter.Button(main_window, text="Recognizer",command=main)
label3 = tkinter.Label(main_window, text="----------------")
button5 = tkinter.Button(main_window, text="EXIT",command=main_window.destroy)

label1.pack()
label2.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
label3.pack()
button5.pack()

main_window.mainloop()