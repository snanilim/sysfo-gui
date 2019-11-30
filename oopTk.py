import tkinter as tk

class MainView(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            print(F)
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')
            # tk.canvas(self, height=400, width=400)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        print('cont', cont)
        print('self.frames', self.frames)
        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="page 1", command=lambda: controller.show_frame(PageOne))
        button.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Inner Page")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = MainView()
app.mainloop()
