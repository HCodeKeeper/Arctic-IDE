from dependencies import *
import gui_config as cf

console_window = None


class Console_window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Developer console")
        self.configure(
            bg="black"
        )
        self.geometry(f"{cf.Console_window.WIDTH}x{cf.Console_window.HEIGHT}")
        self.console = Console(self)
        self.console.grid(row=1, column=1)
    


class Console(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(
            width=cf.ConsoleField.WIDTH,
            height=cf.ConsoleField.HEIGHT,
            bg="black",
            fg="#10cc02",
            font=('Helvetica',14,'bold')
        )
    

    def insert_output(self, output_data): #data: string
        self.insert(tk.END, output_data)
        return True


def create_console(parent, output_data=""):
    global console_window
    console_window = Console_window(parent)
    console_window.console.insert_output(output_data=output_data)