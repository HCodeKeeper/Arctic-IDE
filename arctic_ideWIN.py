from dependencies import *
import time
from typing import Annotated
import file_managment as file_m
import os


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.icon = tk.PhotoImage(file='icon.png')
        self.iconphoto(False, self.icon)

        self.geometry(self.SpawnInCenter(specs.specs["monitor"]["width"], specs.specs["monitor"]["height"]))
        self.title("Arctic IDE")
        self.tabControl = ttk.Notebook(self)
        self.tabControl.grid(row=1, column=0)
        self.tabs = []
        self.currentTabIndex = None #CAN ACHIEVE 0, so it is intended to be checked with None and not False(if we need)
        self.currentTab = None

        #MenuBar
        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)

        #File Menu
        self.fileMenu = tk.Menu(self)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="Create a file", command = self.CreateTab)
        self.fileMenu.add_command(label="Open a file", command = lambda: file_m.File.open(self))
        self.fileMenu.add_command(label="Create a project")
        self.fileMenu.add_command(label="Open a project")
        self.fileMenu.add_command(label="Save", command = lambda: file_m.File.save(textSrc=self.currentTab.textField.content, _file=self.currentTab.fileObj))
        self.fileMenu.add_command(label="Save as", command = lambda: self.currentTab.UpdateFileObj(file_m.File.save_as(textSrc=self.currentTab.textField.content)))

        #View Menu
        self.viewMenu = tk.Menu(self)
        self.menuBar.add_cascade(label="View", menu=self.viewMenu)
        
        #Tools Menu
        self.toolsMenu = tk.Menu(self)
        self.menuBar.add_cascade(label="Tools", menu=self.toolsMenu)
        self.toolsMenu.add_command(label="Search in a file")

        #Help Menu
        self.helpMenu = tk.Menu(self)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
        self.helpMenu.add_command(label="Docs")
        self.helpMenu.add_command(label="Configs")

        #Front Context Frame
        self.frontContextFrame = tk.Frame(self, width=4, height=2)
        self.frontContextFrame.grid(row=0, column=0, sticky=tk.NW)

        self.btnCreateTab = tk.Button(self.frontContextFrame, text="+", bg="#99ff6e", command = self.CreateTab, width=2, height=1)
        self.btnDeleteTab = tk.Button(self.frontContextFrame, text="-", bg="#ff5e5e", command = self.DeleteTab, width=2, height=1)

        self.btnCreateTab.grid(row=0, column=0)
        self.btnDeleteTab.grid(row=0, column=1)
        #
        self.CreateTab()
    

    def GetCurrentTab(self):
        if self.tabs:
            self.currentTabIndex = self.tabControl.index(self.tabControl.select())
            self.currentTab = self.tabs[self.currentTabIndex]
        else:
            self.currentTabIndex = None
            self.currentTab = None
            return None
        return self.currentTabIndex


    def SpawnInCenter(self, mWidth, mHeight):
        return f"{cf.Geometry.width}x{cf.Geometry.height}+{(mWidth - cf.Geometry.width)//2}+{(mHeight-cf.Geometry.height)//2}"


    def CreateTab(self, title=None): ##title is never used
        if not title:
           title = f"File-{len(self.tabs)+1}"
           tab = Tab(tabControl=self.tabControl, title=title)
           self.tabs.append(tab)
        else:
            uniqueName = title
            tab = Tab(tabControl=self.tabControl, title=title)
            self.tabs.append(tab)
        return tab
    

    def DeleteTab(self, tab_index=None):
        if not tab_index:
            if self.currentTabIndex != None:
                tab_index = self.currentTabIndex
            else:
                return None
        self.tabControl.forget(self.tabs[tab_index])
        self.tabs.pop(tab_index)
        self.RenameAllTabs()


    def RenameAllTabs(self):
        if self.tabs:
            number = 0
            for tab in self.tabs:
                if not tab.uniqueName:
                    number += 1
                    self.tabControl.tab(tab, text=f"File-{number}")


class Tab(tk.Frame):
    def __init__(self, tabControl, title, uniqueName=None, fileObj=None):
        super().__init__(tabControl)
        self.uniqueName = uniqueName
        self.fileObj = fileObj
        self.tabControl= tabControl
        tabControl.add(self, text=title if not self.uniqueName else self.uniqueName)
        self.tabID = tabControl.tabs()[-1]
        self.textField = TextField(self)
        self.textField.grid(row=0, column=0, sticky=tk.NW)
    


    def _UpdateUniqueName(self, fileObj):
        if fileObj:
            self.uniqueName = os.path.basename(fileObj.name)
            self.tabControl.tab(self.tabID, text=self.uniqueName)


    def UpdateFileObj(self, fileObj):
        self.fileObj = fileObj
        self._UpdateUniqueName(self.fileObj)
    


class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(parent)

        self.contentList = self.GetContent()
        self.content = ''.join(self.contentList)

        # Vertical (y) Scroll Bar
        self.yscrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL)

        self.configure(
            font=cf.Font.fontTuple,
            width=cf.TextFieldGeometry.WIDTH,
            height=cf.TextFieldGeometry.HEIGHT,
            yscrollcommand=self.yscrollbar.set,
            tabs=("1c","2c")
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

    
    def GetCursorPosition(self) -> Annotated[str, "row, column"] :
        return self.index(tk.INSERT)

    
class MenuBarProcesses():
    pass


if __name__ == '__main__':
    program = GUI()
    while True:
        if program.GetCurrentTab() != None:
            program.currentTab.textField.GetContent()
        program.update_idletasks()
        program.update()
        time.sleep(0.01)
