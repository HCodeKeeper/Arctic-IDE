from dependencies import *
##import char_pix_converter as fontConverter


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.icon = tk.PhotoImage(file='icon.png')
        self.iconphoto(False, self.icon)

        self.geometry(self.SpawnInCenter(specs.specs["monitor"]["width"], specs.specs["monitor"]["height"]))
        self.title("Arctic IDE")
        self.tabControl = ttk.Notebook(self)
        self.tabControl.grid(row=0, column=0)
        self.tabs = []
        self.currentTab = None #has to be object Tab() from self.tabs

        '''
        tk.Grid.rowconfigure(self, Tab.gridPosiotion[0], weight=1)
        tk.Grid.columnconfigure(self, Tab.gridPosiotion[1], weight=1)
        '''
        self.CreateTab()
    

    def SpawnInCenter(self, mWidth, mHeight):
        return f"{cf.Geometry.width}x{cf.Geometry.height}+{(mWidth - cf.Geometry.width)//2}+{(mHeight-cf.Geometry.height)//2}"



    def CreateTab(self, title=None):
        if not title:
           title = f"File-{len(self.tabs)+1}"
        self.tabs.append(Tab(tabControl=self.tabControl, title=title))


class Tab(ttk.Frame):

    gridPosiotion = (3,0)

    def __init__(self, tabControl, title):
        super().__init__(tabControl)
        tabControl.add(self, text=title)
        self.textField = TextField(self)
        self.textField.grid(row=Tab.gridPosiotion[0], column=Tab.gridPosiotion[1], sticky=tk.NW)


class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)

        # Vertical (y) Scroll Bar
        self.yscrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL)

        self.configure(
            font=cf.Font.fontTuple,
            width=cf.TextFieldGeometry.WIDTH,
            height=cf.TextFieldGeometry.HEIGHT,
            yscrollcommand=self.yscrollbar.set
            )
        
        self.yscrollbar.config(command=self.yview)

    
    def ThrowTab(self):
        self.insert('end', "\t")

if __name__ == '__main__':
    program = GUI()
    program.mainloop()