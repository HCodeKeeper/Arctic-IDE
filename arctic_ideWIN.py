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
        self.currentTabIndex = None #has to be object Tab() from self.tabs # old
        self.currentTab = None

        self.CreateTab()
    
    def GetCurrentTab(self):
        if self.tabs:
            self.currentTabIndex = self.tabControl.index(self.tabControl.select())
            self.currentTab = self.tabs[self.currentTabIndex]
        else:
            self.currentTabIndex = None
            self.currentTab = None
        return self.currentTabIndex


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
        self.isTab = False

        # Vertical (y) Scroll Bar
        self.yscrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL)

        self.configure(
            font=cf.Font.fontTuple,
            width=cf.TextFieldGeometry.WIDTH,
            height=cf.TextFieldGeometry.HEIGHT,
            yscrollcommand=self.yscrollbar.set
            )
        
        self.yscrollbar.config(command=self.yview)
        self.bind('<Return>', self._InsertTabEvent)

        self.IndLevels = [(0,0),] #To save indentation levels
        #(0, 0) where [0] => index of ":"(int) in contentList and [1] => quantity of tabs(int)

        self.currentIndLevel = self.IndLevels[-1]

    
    def GetContent(self, omit=None):
        content = self.get("1.0", tk.END)
        content = content[0:-1] #\n charachter always is spawned by default
        def update():
            self.contentList = list(content) if not omit else content.split(omit)
            self.content = ''.join(self.contentList)
        update()
        return self.contentList

    
    def GetCursorPosition(self):
        return self.index(tk.INSERT)


    def _GetLastIndLevel(self):
        self.currentIndLevel = self.IndLevels[-1]


    def _InsertTabEvent(self, event):
        if len(self.content) >= 1:
            if self.content[-1] == ':':
                self.tabCounter += 1
                self.isTab = True
                self.IndLevels.append([self.content[-1], self.IndLevels[-1][1]+1])


    def ErasingTab(self):
        if '\n' in reversedContentList and ':' in reversedContentList:
            if reversedContentList[0] == "\t":
                for char in reversedContentList[0:reversedContentList.index('\n')]:
                    if char != '\t':
                        return False
                    else:
                        continue
                if len(reversedContentList[0:reversedContentList.index('\n')]) < self.currentIndLevel[1] and self.currentIndLevel >= 1:
                    self.IndLevels.append([len(self.contentList)-1, self.IndLevels[-1][1]-1])
                        


    def ProcessTabEvents(self):
        self._GetLastIndLevel()
        reversedContentList = self.contentList[::-1]
        if self.tabCounter and self.isTab:
            self.insert('end', "\t"*self.currentIndLevel[1])
        else:
            pass
        self.isTab = False



if __name__ == '__main__':
    program = GUI()
    while True:
        if program.GetCurrentTab() != None:
            program.currentTab.textField.GetContent()
            program.currentTab.textField.ProcessTabEvents()
        program.update_idletasks()
        program.update()
        time.sleep(0.01)
