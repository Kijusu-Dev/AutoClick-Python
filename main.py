from time import sleep
from tkinter import *
import time
import ctypes


class Main(Tk):
    def __init__(self):
        super().__init__()
        # Name of windows
        window = self

        colors = {
            'Background': '#161616',
            'TextColors': '#ACACAC'
        }

        self.mouse = ctypes.windll.user32
        self.state = False
        self.run = False

        self.speedClick = StringVar()
        self.amountClick = StringVar()

        self.speedClick.set(100)
        self.amountClick.set(0)

        self.timekeeper = 0
        self.x = 0

        # State False Or True

        def StateFalse():
            exit()

        def StateTrue():
            if self.state == True:
                self.state = True
                self.run = True
            else:
                self.x = 0
                self.state = True
                self.run = True

            while True:
                self.timekeeper += 1
                if self.state == True:
                    self.Amount = int(self.amountClick.get())
                    self.Speed = int(self.speedClick.get())
                    print(self.state)
                    if self.Amount == 0:
                        time.sleep(self.Speed / 1000)
                        self.mouse.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
                        self.mouse.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
                        self.x += 1
                        print("Clicked %s Times" % (self.x))

                    elif self.x < self.Amount and self.state == True:
                        time.sleep(self.Speed / 1000)
                        self.mouse.mouse_event(2, 0, 0, 0, 0)  # left mouse button down
                        self.mouse.mouse_event(4, 0, 0, 0, 0)  # left mouse button up
                        self.x += 1
                        print("Clicked %s Times" % (self.x))
                        if self.x == self.Amount:
                            self.state = False

        # Configuration windows
        window.geometry("400x370")
        window.config(background=colors['Background'])
        window.resizable(False, False)
        window.title("AutoClicking V1")

        # Design, Texts, Button, Entry
        title = Label(window, text="AutoClicking", font=('Roboto', 30, 'bold'), bg=colors['Background'],
                      fg=colors['TextColors'])
        title.pack()

        # Texts and Entry

        TextLatency = Label(window, text="Time For Latency", font=('Roboto', 10, 'bold'), bg=colors['Background'],
                            fg='#FFFFFF')
        TextLatency.place(x=130, y=80)
        LatencyEntry = Entry(window, textvariable=self.speedClick, bd=2)
        LatencyEntry.place(x=119, y=110)
        TextClick = Label(window, text="Number of Click", font=('Roboto', 10, 'bold'), bg=colors['Background'],
                          fg='#FFFFFF')
        TextClick.place(x=135, y=150)
        ClickEntry = Entry(window, textvariable=self.amountClick, bd=2)
        ClickEntry.place(x=119, y=180)

        # Button

        ButtonActivate = Button(window, text="Activate", font=('Roboto', 10, 'bold'), bg='#26751F',
                                activebackground='#2C8524', fg='#FFFFFF', activeforeground='#FFFFFF', bd=0, width=10,
                                height=2, command=StateTrue)
        ButtonActivate.place(x=50, y=250)
        ButtonDeActivate = Button(window, text="Deactivate", font=('Roboto', 10, 'bold'), bg='#C10C0C',
                                  activebackground='#CA1C1C', fg='#FFFFFF', activeforeground='#FFFFFF', bd=0, width=10,
                                  height=2, command=StateFalse)
        ButtonDeActivate.place(x=240, y=250)

        # Display windows

        window.mainloop()



Main().Test()
