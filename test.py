from arctic_ideWIN import * #intended to be placed in package

def _generateTabs(n_ext=1):
    if n_ext >= 1:
        for n in range(n_ext):
            program.CreateTab()


def GetTabInfo(_Sum=True, CurNum=True, CurTab=True, CurTabContent=True):
    message = ""
    
    _sum = f"Summary of tabs: {program.tabs}."
    curNum = f"Current tab number: {program.currentTabNumber}"

    if program.currentTabNumber:
        curTab = f"Current tab: {program.tabs[program.currentTabNumber]}"
        curTabContent = f"-> Content: {program.tabs[program.currentTabNumber].content}"
    else:
        curTab = "Current tab: doesn't exist"
        curTabContent = "Current tab's content: doesn't exist"
    
    if _Sum:
        message += _sum + '\n'
    
    if CurNum:
        message += curNum + '\n'
    
    if CurTab:
        message += curTab + '\n'

    if CurTabContent:
        message += curTabContent
    
    return message

if __name__ == '__main__':
    program = GUI()
    _generateTabs(20)
    program.tabs[0].textField.insert("1.0", "brbrbr brbrbrb    brbrb\n")
    while True:
        print(program.tabs[0].textField.GetContent())
        print(program.GetCurrentTab()) #
        program.update_idletasks()
        program.update()