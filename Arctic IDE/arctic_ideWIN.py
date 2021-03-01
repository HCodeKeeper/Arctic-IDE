from dependencies import *
import time
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
        self.currentTabNumber = None #has to be object Tab() from self.tabs

        self.CreateTab()
    
    def GetCurrentTab(self):
        if self.tabs:
            self.currentTabNumber = self.tabControl.index(self.tabControl.select())
        else:
            self.currentTabNumber = None
        return self.currentTabNumber


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
        tabControl


class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)

        self.contentList = self.GetContent()
        self.content = ''.join(self.contentList)

        self.tabCounter = 0

        # Vertical (y) Scroll Bar
        self.yscrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL)

        self.configure(
            font=cf.Font.fontTuple,
            width=cf.TextFieldGeometry.WIDTH,
            height=cf.TextFieldGeometry.HEIGHT,
            yscrollcommand=self.yscrollbar.set
            )
        
        self.yscrollbar.config(command=self.yview)

    
    def GetContent(self, omit=None):
        content = self.get("1.0", tk.END)
        content = content[0:-1] #\n charachter always is spawned by default
        def update():
            self.contentList = list(content) if not omit else content.split(omit)
            self.content = ''.join(self.contentList)
        update()
        return self.contentList

    
    def AutomaticTabThrowing(self):
        self.GetContent()
        if len(self.content) >= 2:
            if self.content[-1] == '\n' and self.content[-2] == ':':
                self.tabCounter += 1
                self.insert('end', "\t"*self.tabCounter)
                return "Tab was thrown"
        return None


if __name__ == '__main__':
    program = GUI()
    while True:
        if program.GetCurrentTab() != None:
            print(program.tabs[program.currentTabNumber].textField.AutomaticTabThrowing())
        program.update_idletasks()
        program.update()
        time.sleep(0.01)
