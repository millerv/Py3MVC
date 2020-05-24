from tkinter import *
import TestGui
import TestModel

class TestController:
    '''
    The TestController class manages communication between view(gui) and model.

    Args:

    Attributes:
        arg (model): contains the functions needed for this project.
        arg (view): contains the GUI information needed for this project.
    '''
    def __init__(self):
        self.root = Tk()

        self.model = TestModel.MyModel()
        self.view = TestGui.MyFrame(self)

        self.root.mainloop()

    def buttonPressed1(self, event=None): # pylint: disable=unused-argument
        ft = self.view.feetEntry.get()
        result = str(self.model.calculate(float(ft)))
        self.view.temp.set(result)

if __name__ == "__main__":
    c = TestController()
