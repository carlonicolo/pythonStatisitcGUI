from tkinter import *
from tkinter.ttk import *

from plotdata import regression_plot
from stats import stats_columns


class Application(Frame):
    def __init(self, master=None):
        super().__init__(master)
        self.master = master


root = Tk()
app = Application(master=root)
app.mainloop()